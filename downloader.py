from PySide2.QtCore import QObject, Signal, Slot

from dataclasses import dataclass
from typing import Dict

from threading import Thread

import youtube_dl
import time
import browsers

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


class Downloader(QObject):
    downloads = []
    WAIT_TIME = 10

    added_row = Signal()
    dl_hook = Signal()
    removed_row = Signal()
    terminal_write = Signal(str)

    def __init__(self):
        super().__init__()

        try:
            with open("output.txt", "r") as f:
                self.output_path = f.readline()
        except:
            self.output_path = "C:/Music/"

        self.ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': self.output_path + "/%(title)s.%(ext)s",
            'addmetadata': True,
            'nooverwrites': True,
            'no_color': True,
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
                    ydl.download([dl.url])
                self.downloads.pop(0)
                self.removed_row.emit()
            else:
                time.sleep(1)

    def add_to_queue(self, urls):
        for url in urls:
            with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)

            entries = info_dict.get('entries')

            if entries:
                for entry in entries:
                    title = entry['title']
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
        print(urls)
        Thread(target=self.add_to_queue, daemon=True, args=(urls,)).start()

    def from_chrome(self):
        urls = browsers.ch_urls()
        print(urls)
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
        self.output_path = path
        self.ydl_opts["outtmpl"] = path + "/%(title)s.%(ext)s"

    def close(self):
        with open("output.txt", "w") as f:
            f.write(self.output_path)
