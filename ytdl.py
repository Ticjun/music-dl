import PySimpleGUI as sg

import dowloader
import get

from threading import Thread

dler = dowloader.Downloader()
dlthread = Thread(target=dler.run, daemon=True)
dlthread.start()
def hook(d):
    dler.hook(d)
dler.set_hook(hook)

sg.theme('Dark Blue 3')
sg.SetOptions(element_padding=(0, 0))
headings = ['title', '%', 'speed', 'size',
            'eta', 'status']
col_widths = [43, 10, 10, 10, 10, 10]
buttons = [[sg.Button('Add', size=(10, 2))],
           [sg.Button('Firefox', size=(10, 2))],
           [sg.Button('Chrome', size=(10, 2))]]
urls = [[sg.Text('Youtube URLS (supports playlists):')],
        [sg.Multiline(size=(50, 10), key="URLS"), sg.Column(buttons)]]
terminal = [[sg.Text('Terminal')],
            [sg.Output(size=(50, 10))]]
layout = [[sg.Text('Output Folder :'), sg.Input(key="DIR", enable_events=True, default_text=dler.output_path),
           sg.FileBrowse(), sg.Text('(without file name)')],
          [sg.Column(urls), sg.Column(terminal)],
          [sg.Table(values=[], headings=headings, num_rows=10, justification='left', auto_size_columns=False, key='TABLE',
                    enable_events=False, col_widths=col_widths, row_height=22)]]

window = sg.Window('Ytdl', layout)

def val_table():
    table = []
    for dl in dler.downloads:
        values = [dl.title, dl.percent, dl.speed, dl.size,
                  dl.eta, dl.status]
        table.append(values)
    return table

while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Add':
        for url in values['URLS'].split():
            thread = Thread(target=dler.add, args=(url,), daemon=True)
            thread.start()
        window['URLS'].update("")
    if event == 'Firefox':
        for url in get.firefox_urls():
            thread = Thread(target=dler.add, args=(url,), daemon=True)
            thread.start()
    if event == 'DIR':
        dler.output(values["DIR"])
    window['TABLE'].update(val_table())
    window.refresh()
dler.close()
window.close()
