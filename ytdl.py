import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QFileDialog
from PySide2.QtCore import QThread
from main_window import Ui_MainWindow

from downloader import Downloader
from threading import Thread


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__(self)
        self.setupUi(self)

        self.dl = Downloader()
        self.thread = Thread(target=self.dl.run, daemon=True)
        self.thread.start()

        self.lineEdit_file_path.setText(self.dl.output_path)
        self.lineEdit_file_path.textEdited.connect(self.dl.output)
        self.firefox_button.clicked.connect(self.dl.from_firefox)
        self.firefox_button.clicked.connect(self.dl.from_chrome)

        self.dl.added_row.connect(self.add_row)
        self.dl.dl_hook.connect(self.update_row)
        self.dl.removed_row.connect(self.remove_row)

    def update_row(self, i=0):
        self.table_dl.setItem(i, 0, QTableWidgetItem(self.dl.downloads[i].title))
        self.table_dl.setItem(i, 1, QTableWidgetItem(self.dl.downloads[i].size))
        self.table_dl.setItem(i, 2, QTableWidgetItem(self.dl.downloads[i].speed))
        self.table_dl.setItem(i, 3, QTableWidgetItem(self.dl.downloads[i].eta))
        self.table_dl.setItem(i, 4, QTableWidgetItem(self.dl.downloads[i].status))
        self.table_dl.resizeColumnsToContents()

    def add_row(self):
        i = len(self.dl.downloads)-1
        self.table_dl.insertRow(i)
        self.update_row(i)

    def remove_row(self):
        self.table_dl.removeRow(len(self.dl.downloads))


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec_()

mainWindow.dl.close()
