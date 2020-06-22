import youtube_dl
import winsound

class Download:
    def __init__(self, url):
        self.info_dict = None

        self.url = url
        self.title = "..."
        self.percent = 0
        self.speed = 0
        self.size = "..."
        self.left = "..."
        self.eta = "..."
        self.status = "Pending"

class MyLogger(object):
    def debug(self, msg):
        print(msg)
    def warning(self, msg):
        print(msg)
    def error(self, msg):
        print(msg)

class Downloader:
    def __init__(self):
        self.downloads = []
        try:
            with open("output.txt", "r") as f:
                self.output_path = f.readline()
        except:
            self.output_path = "C:/Music/"

        self.ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': self.output_path + "%(title)s.%(ext)s",
            'addmetadata': True,
            'nooverwrites': True,
            'no_color': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'logger': MyLogger(),
            'progress_hooks': [],
        }

        self.done = True

    def run(self):
        while True:
            if self.downloads:
                self.done = False
                dl = self.downloads[0]
                with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                    ydl.download([dl.url])
                self.downloads.pop(0)
            elif not self.done:
                winsound.MessageBeep(-1)
                self.done = True

    def add(self, url):
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)

        entries = info_dict.get('entries')
        if entries:
            for entrie in entries:
                dl = Download(url)
                dl.info_dict = entrie
                dl.title = entrie['title']
                self.downloads.append(dl)
        else:
            dl = Download(url)
            dl.info_dict = info_dict
            dl.title = info_dict['title']
            self.downloads.append(dl)


    def hook(self, d):
        dl = self.downloads[0]
        dl.status = d['status']
        if d['status'] == 'downloading':
            dl.speed = d['_speed_str']
            dl.percent = d['_percent_str']
            dl.size = d.get('_total_bytes_str') or d.get('_total_bytes_estimate_str')
            dl.eta = d['_eta_str']
        if d['status'] == 'finished':
            dl.status = "converting"

    def output(self, path):
        self.output_path = path
        self.ydl_opts["outtmpl"] = path + "%(title)s.%(ext)s"

    def set_hook(self, hook):
        self.ydl_opts['progress_hooks'].append(hook)

    def close(self):
        with open("output.txt", "w") as f:
            f.write(self.output_path)