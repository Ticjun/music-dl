# music-dl

> Imports youtube urls from Firefox and downloads them to mp3

## Features

- [x] Dark theme
- [x] Automatically retry failed downloads
- [x] Playlists support
- [ ] Chrome imports

## About

Gui for command-line tool youtube-dl made with Pyside2

- youtube-dl : https://github.com/ytdl-org/youtube-dl

## Help needed:

- Chrome imports
- Prevent ffmpeg and youtube-dl from opening a window on Windows (due to subprocess.Popen). Dirty fix in the subprocess module: 
  ```py
  class STARTUPINFO:
        def __init__(self, *, dwFlags=0, hStdInput=None, hStdOutput=None,
                     hStdError=None, wShowWindow=0, lpAttributeList=None):
            self.dwFlags = dwFlags
            #  FIX
            self.dwFlags |= STARTF_USESHOWWINDOW
  ```

## Issues

I am currently developping this for my own private use and probably won't add any features I don't need, feel free to request though.

Contact me if this project breaks any Copyright or TOS.
