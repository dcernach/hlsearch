# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Tue May  7 15:43:20 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(902, 697)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(902, 697))
        mainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(mainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.searchEdit = QtGui.QLineEdit(self.centralwidget)
        self.searchEdit.setObjectName(_fromUtf8("searchEdit"))
        self.gridLayout.addWidget(self.searchEdit, 1, 0, 1, 1)
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.gridLayout.addWidget(self.searchButton, 1, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 2)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(mainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionFolder = QtGui.QAction(mainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFolder.setIcon(icon)
        self.actionFolder.setObjectName(_fromUtf8("actionFolder"))
        self.menuFile.addAction(self.actionFolder)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionFolder)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.searchEdit.setPlaceholderText(QtGui.QApplication.translate("mainWindow", "Creature name...", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("mainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("mainWindow", "Source", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("mainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("mainWindow", "Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("mainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("mainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFolder.setText(QtGui.QApplication.translate("mainWindow", "Search Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFolder.setToolTip(QtGui.QApplication.translate("mainWindow", "Folder to search in", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFolder.setStatusTip(QtGui.QApplication.translate("mainWindow", "Folder to search in", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFolder.setShortcut(QtGui.QApplication.translate("mainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
