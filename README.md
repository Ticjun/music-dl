# music-dl

> Imports youtube urls from Firefox and downloads them to mp3

## Features

- [x] Dark theme
- [x] Automatically retry failed downloads
- [x] Playlists support
- [ ] Chrome imports
- [ ] Firefox win7 imports
- [ ] No redownloads of files that would have the same name after being converted to mp3 (not based on youtube-dl already downloaded urls database)

## About

Gui for command-line tool youtube-dl, using Pyside2

Tested for Win 10

Unpack the archive and launch `music-dl.exe`

## Help needed:

- Chrome imports
- Firefox win7 imports
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

- Currently in development, won't add unneeded features, feel free to request though.
- License : No License

## Credits

- youtube-dl : https://github.com/ytdl-org/youtube-dl
