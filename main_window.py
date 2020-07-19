# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui',
# licensing of 'main_window.ui' applies.
#
# Created: Sun Jul 19 02:00:21 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 557)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 50))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.text_button = QtWidgets.QPushButton(self.centralwidget)
        self.text_button.setObjectName("text_button")
        self.horizontalLayout_2.addWidget(self.text_button)
        self.firefox_button = QtWidgets.QPushButton(self.centralwidget)
        self.firefox_button.setObjectName("firefox_button")
        self.horizontalLayout_2.addWidget(self.firefox_button)
        self.chrome_button = QtWidgets.QPushButton(self.centralwidget)
        self.chrome_button.setObjectName("chrome_button")
        self.horizontalLayout_2.addWidget(self.chrome_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.text_input = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_input.sizePolicy().hasHeightForWidth())
        self.text_input.setSizePolicy(sizePolicy)
        self.text_input.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.text_input.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.text_input.setObjectName("text_input")
        self.gridLayout.addWidget(self.text_input, 2, 0, 1, 1)
        self.table_dl = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.table_dl.sizePolicy().hasHeightForWidth())
        self.table_dl.setSizePolicy(sizePolicy)
        self.table_dl.setAutoFillBackground(False)
        self.table_dl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_dl.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table_dl.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_dl.setObjectName("table_dl")
        self.table_dl.setColumnCount(6)
        self.table_dl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_dl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dl.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dl.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dl.setHorizontalHeaderItem(5, item)
        self.table_dl.horizontalHeader().setVisible(True)
        self.table_dl.horizontalHeader().setCascadingSectionResizes(False)
        self.table_dl.horizontalHeader().setStretchLastSection(True)
        self.table_dl.verticalHeader().setVisible(False)
        self.table_dl.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.table_dl, 4, 0, 1, 1)
        self.terminal = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terminal.sizePolicy().hasHeightForWidth())
        self.terminal.setSizePolicy(sizePolicy)
        self.terminal.setMinimumSize(QtCore.QSize(0, 0))
        self.terminal.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.terminal.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.terminal.setObjectName("terminal")
        self.gridLayout.addWidget(self.terminal, 6, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_file_path = QtWidgets.QLabel(self.centralwidget)
        self.label_file_path.setObjectName("label_file_path")
        self.horizontalLayout.addWidget(self.label_file_path)
        self.lineEdit_file_path = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_file_path.setDragEnabled(False)
        self.lineEdit_file_path.setObjectName("lineEdit_file_path")
        self.horizontalLayout.addWidget(self.lineEdit_file_path)
        self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_button.setObjectName("browse_button")
        self.horizontalLayout.addWidget(self.browse_button)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 21))
        self.menubar.setObjectName("menubar")
        self.menuTheme = QtWidgets.QMenu(self.menubar)
        self.menuTheme.setObjectName("menuTheme")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLight_theme = QtWidgets.QAction(MainWindow)
        self.actionLight_theme.setCheckable(True)
        self.actionLight_theme.setChecked(True)
        self.actionLight_theme.setObjectName("actionLight_theme")
        self.dark_theme = QtWidgets.QAction(MainWindow)
        self.dark_theme.setCheckable(True)
        self.dark_theme.setObjectName("dark_theme")
        self.menuTheme.addAction(self.dark_theme)
        self.menubar.addAction(self.menuTheme.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Ytdl", None, -1))
        self.text_button.setText(QtWidgets.QApplication.translate("MainWindow", "From Text", None, -1))
        self.text_button.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Return", None, -1))
        self.firefox_button.setText(QtWidgets.QApplication.translate("MainWindow", "From Firefox", None, -1))
        self.chrome_button.setText(QtWidgets.QApplication.translate("MainWindow", "From Chrome", None, -1))
        self.table_dl.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "Title", None, -1))
        self.table_dl.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "Size", None, -1))
        self.table_dl.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "Speed", None, -1))
        self.table_dl.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("MainWindow", "ETA", None, -1))
        self.table_dl.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("MainWindow", "Status", None, -1))
        self.table_dl.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("MainWindow", "Output Path", None, -1))
        self.label_file_path.setText(QtWidgets.QApplication.translate("MainWindow", "File Path :", None, -1))
        self.browse_button.setText(QtWidgets.QApplication.translate("MainWindow", "Browse", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Output :", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Enter URLs :", None, -1))
        self.menuTheme.setTitle(QtWidgets.QApplication.translate("MainWindow", "Theme", None, -1))
        self.actionLight_theme.setText(QtWidgets.QApplication.translate("MainWindow", "Light theme", None, -1))
        self.dark_theme.setText(QtWidgets.QApplication.translate("MainWindow", "Dark theme", None, -1))

