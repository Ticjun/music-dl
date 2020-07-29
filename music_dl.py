import sys

from downloader import Downloader
from threading import Thread
from config import cfg

from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog
from main_window import Ui_MainWindow
from terminal import Terminal
from dark_theme import dark_theme, light_theme

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Menu
        self.dark_theme.triggered.connect(self.on_dark_theme)
        self.theme()

        # Terminal
        self.term = Terminal()
        sys.stdout = self.term
        self.term.event.connect(self.update_terminal)

        self.dl = Downloader()
        Thread(target=self.dl.run, daemon=True).start()

        # Browse
        self.lineEdit_file_path.setText(self.dl.output_path)
        self.lineEdit_file_path.textEdited.connect(self.dl.output)
        self.lineEdit_file_path.textEdited.connect(self.dl.output)
        self.browse_button.clicked.connect(self.browse)

        # Buttons
        self.firefox_button.clicked.connect(self.dl.from_firefox)
        self.chrome_button.clicked.connect(self.dl.from_chrome)
        self.text_button.clicked.connect(self.from_text)  # Intercept signal to add str

        # Logic
        self.dl.added_row.connect(self.add_row)
        self.dl.dl_hook.connect(self.update_row)
        self.dl.removed_row.connect(self.remove_row)

    def update_row(self, i=0):
        for i in range(self.table_dl.rowCount()):
            self.table_dl.setItem(i, 0, QTableWidgetItem(self.dl.downloads[i].title))
            self.table_dl.setItem(i, 1, QTableWidgetItem(self.dl.downloads[i].size))
            self.table_dl.setItem(i, 2, QTableWidgetItem(self.dl.downloads[i].speed))
            self.table_dl.setItem(i, 3, QTableWidgetItem(self.dl.downloads[i].eta))
            self.table_dl.setItem(i, 4, QTableWidgetItem(self.dl.downloads[i].status))
            self.table_dl.setItem(i, 5, QTableWidgetItem(self.dl.downloads[i].output_path))

    def add_row(self):
        i = self.table_dl.rowCount()
        self.table_dl.insertRow(i)
        self.update_row(i)

    def remove_row(self):
        i = self.table_dl.rowCount() - 1
        self.table_dl.removeRow(i)

    def browse(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        dialog = QFileDialog()
        dialog.setOptions(options)
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        dialog.setAcceptMode(QFileDialog.AcceptOpen)

        if dialog.exec_() == QFileDialog.Accepted:
            self.dl.output(dialog.selectedFiles()[0])
            self.lineEdit_file_path.setText(self.dl.output_path)

    def from_text(self):
        self.dl.from_text(self.text_input.toPlainText())
        self.text_input.clear()

    def theme(self):
        if cfg.data["dark"]:
            dark_theme(app)
            self.dark_theme.setChecked(True)
        else:
            light_theme(app)

    def on_dark_theme(self):
        cfg.data["dark"] = not cfg.data["dark"]
        self.theme()

    def update_terminal(self, text):
        self.terminal.appendHtml(text)

app = QApplication(sys.argv)
app.setStyle('Fusion')
mainWindow = MainWindow()
mainWindow.show()
app.exec_()

cfg.save_config()
