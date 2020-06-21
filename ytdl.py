import os
import sys

import subprocess
import re
from pywinauto import Application

import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        print(msg)

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'D:/Music/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    path = os.path.dirname(sys.executable)
elif __file__:
    path = os.path.dirname(__file__)
else:
    path = None
    print("[ytdl] ERROR: Couldn't find path")
    input()
    exit(-1)


def get_firefox_urls():
    try:
        firefox = Application(backend="uia").connect(title_re='.*Firefox.*', found_index=0, timeout=5)
    except:
        firefox = None
        print("[ytdl] ERROR: Firefox is not running")
        input()
        exit(-1)

    wd = firefox.windows()[0]
    tabs = wd.children()
    urls = []
    for tab in tabs:
        try:
            s = tab.children()[0].children()[0]
            url = s.legacy_properties()["Value"]
            urls.append(url)
        except:
            continue
    return urls


def yt_link(text):
    text = str(text)
    rexp = "(?:youtube\.com|youtu.be)\/" \
           "(?:[\w\-]+\?v=|embed\/|v\/)?" \
           "([\w\-]+)" \
           ".*$"
    res = re.search(rexp, text)
    return res


def dl(urls):
    yt_urls = [url for url in urls if yt_link(url)]
    procs = []
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(yt_urls)

    print(f"[ytdl] Downloaded {len(yt_urls)} files successfully")


dl(get_firefox_urls())
