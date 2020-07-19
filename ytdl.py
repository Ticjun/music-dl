import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QPalette, QColor
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog
from main_window import Ui_MainWindow

from downloader import Downloader
from threading import Thread


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.dl = Downloader()
        Thread(target=self.dl.run, daemon=True).start()

        # Menu
        self.dark_theme.triggered.connect(self.dark_mode)
        self.dark = False


        # Browse
        self.lineEdit_file_path.setText(self.dl.output_path)
        self.lineEdit_file_path.textEdited.connect(self.dl.output)
        self.lineEdit_file_path.textEdited.connect(self.dl.output)
        self.browse_button.clicked.connect(self.browse)

        # Buttons
        self.firefox_button.clicked.connect(self.dl.from_firefox)
        self.chrome_button.clicked.connect(self.dl.from_chrome)
        self.text_button.clicked.connect(self.from_text) # Intercept signal to add str

        # Logic
        self.dl.added_row.connect(self.add_row)
        self.dl.dl_hook.connect(self.update_row)
        self.dl.removed_row.connect(self.remove_row)

    def update_row(self, i=0):
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

    def dark_mode(self):
        self.dark = not self.dark
        if self.dark:
            app.setPalette(dark_palette)
        else:
            app.setPalette(app.style().standardPalette())


app = QApplication(sys.argv)

app.setStyle('Fusion')
dark_palette = QPalette()
dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
dark_palette.setColor(QPalette.WindowText, Qt.white)
dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
dark_palette.setColor(QPalette.ToolTipText, Qt.white)
dark_palette.setColor(QPalette.Text, Qt.white)
dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ButtonText, Qt.white)
dark_palette.setColor(QPalette.BrightText, Qt.red)
dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, Qt.black)





mainWindow = MainWindow()
mainWindow.show()
app.exec_()

mainWindow.dl.close()
