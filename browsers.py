from pywinauto import Application, Desktop
import re

def yt_link(text):
    text = str(text)
    rexp = "(?:youtube\.com|youtu\.be)\/"
    res = re.search(rexp, text)
    return res

def ff_urls():
    try:
        firefox = Application(backend="uia").connect(title_re='.*Firefox.*', found_index=0, timeout=5)
    except:
        firefox = None
        print("[ytdl] ERROR: Firefox is not running")
        input()
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
    return [url for url in urls if yt_link(url)]

def ch_urls():
    try:
        chrome = Application(backend="uia").connect(title_re='.*Chrome.*', found_index=0, timeout=5)
    except:
        chrome = None
        print("[ytdl] ERROR: Chrome is not running")
        input()
    return []