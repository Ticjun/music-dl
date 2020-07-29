import youtube_dl
import time
import browsers
import re

from threading import Thread
from dataclasses import dataclass
from typing import Dict
from PySide2.QtCore import QObject, Signal, Slot

from config import cfg

@dataclass
class Download:
    url: str
    info_dict: Dict

    output_path: str = ""
    title: str = ""
    percent: str = ""
    speed: str = ""
    size: str = ""
    left: str = ""
    eta: str = ""
    status: str = "queued"


class MyLogger(object):
    def debug(self, msg):
        print(msg)
    def warning(self, msg):
        print(msg)
    def error(self, msg):
        print(msg)

def yt_link(text):
    if not text:
        return None
    rexp = ("(?:youtube\.com|youtu\.be)\/"
            "(?:[\w\-]+\?v=|embed\/|v\/)?"
            "([\w\-]+)")
    res = re.search(rexp, text)
    if res is not None:
        return text
    return None

class Downloader(QObject):
    downloads = []
    WAIT_TIME = 10

    added_row = Signal()
    dl_hook = Signal()
    removed_row = Signal()
    terminal_write = Signal(str)

    def __init__(self):
        super().__init__()
        self.output_path = cfg.data["output_path"]
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': self.output_path + "/%(title)s.%(ext)s",
            'addmetadata': True,
            'nooverwrites': True,
            'no_color': True,
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'logger': MyLogger(),
            'progress_hooks': [self.hook],
        }

    def run(self):
        while True:
            if self.downloads:
                dl = self.downloads[0]
                with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                    try:
                        ydl.download([dl.url])
                        self.downloads.pop(0)
                        self.removed_row.emit()
                    except:
                        print(f"Couldn't download {self.downloads[0].title} retrying last (check your internet connection)")
                        self.downloads[0].status = "retry"
                        self.downloads[0].speed = ""
                        self.downloads = self.downloads[1:] + [self.downloads[0]]
            else:
                time.sleep(10)

    def add_to_queue(self, urls):
        for url in [url for url in urls if yt_link(url)]:
            with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                try:
                    info_dict = ydl.extract_info(url, download=False)
                except:
                    print(f"Couldn't add {url} to queue")

            entries = info_dict.get('entries')

            if entries:
                for entry in entries:
                    dl = Download(f"https://www.youtube.com/watch?v={entry['id']}", entry)
                    dl.title = entry['title']
                    dl.output_path = f"{self.output_path}/{dl.title}.mp3"

                    self.downloads.append(dl)
                    self.added_row.emit()
            else:
                dl = Download(url, info_dict)
                dl.title = info_dict['title']
                dl.output_path = f"{self.output_path}/{dl.title}.mp3"
                self.downloads.append(dl)
                self.added_row.emit()

    def from_firefox(self):
        urls = browsers.ff_urls()
        Thread(target=self.add_to_queue, daemon=True, args=(urls,)).start()

    def from_chrome(self):
        urls = browsers.ch_urls()
        Thread(target=self.add_to_queue, daemon=True, args=(urls,)).start()

    def from_text(self, text):
        urls = text.split("\n")
        Thread(target=self.add_to_queue, daemon=True, args=(urls,)).start()

    def hook(self, d):
        dl = Downloader.downloads[0]
        dl.status = d['status']
        if d['status'] == 'downloading':
            dl.speed = d['_speed_str']
            dl.percent = d['_percent_str']
            dl.size = d.get('_total_bytes_str') or d.get('_total_bytes_estimate_str')
            dl.eta = d['_eta_str']
        if d['status'] == 'finished':
            dl.status = "converting"
        self.dl_hook.emit()

    def output(self, path):
        cfg.data["output_path"] = path
        self.ydl_opts["outtmpl"] = path + "/%(title)s.%(ext)s"
