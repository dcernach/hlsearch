__appname__ = "HLSearch"
__module__ = "main"

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui import mainWindow
import os
import time


class Main(QMainWindow, mainWindow.Ui_mainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(__appname__)

        self.load_initial_settings()
        self.searchThread = SearchThread()
        self.searchThread.entryFoundSignal.connect(self.entry_found)
        self.searchThread.searchFinishedSignal.connect(self.search_finished)

        self.actionFolder.triggered.connect(self.action_search_folder_triggered)
        self.searchButton.clicked.connect(self.search_button_clicked)

    def load_initial_settings(self):
        """Setup the initial values"""
        self.settings = QSettings(QSettings.NativeFormat, QSettings.UserScope, "Tarsis", "HLSearch")
        folder = self.settings.value('search_folder').toString()

        if folder == '':
            folder = os.getcwd()

        self.search_folder = folder
        self.tableWidget.setColumnCount(3)

    def action_search_folder_triggered(self):
        """Ask the user for the search folder"""

        folder = QFileDialog.getExistingDirectory(self, "Hero Lab Data Folder", self.search_folder,
                                                  QFileDialog.ShowDirsOnly)

        if folder != '':
            self.search_folder = folder
            self.settings.setValue('search_folder', folder)

    def search_button_clicked(self):
        """Search through the files and display the output"""
        self.row = 0
        self.searchButton.setDisabled(True)
        self.searchThread.start()

    def entry_found(self, file_name, name, summary):
        if self.tableWidget.rowCount() < self.row + 1:
            self.tableWidget.setRowCount(self.row + 1)
        self.tableWidget.setItem(self.row, 0, QTableWidgetItem(file_name))
        self.tableWidget.setItem(self.row, 1, QTableWidgetItem(name))
        self.tableWidget.setItem(self.row, 2, QTableWidgetItem(summary))
        self.row += 1

    def search_finished(self):
        self.searchButton.setDisabled(False)


class SearchThread(QThread):

    entryFoundSignal = pyqtSignal(str, str, str)
    searchFinishedSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(SearchThread, self).__init__(parent)

    def run(self):
        """Here we'll search through the files and pass the output up"""

        self.entryFoundSignal.emit("testfile1.stock", "Test One", "Test summary one")
        time.sleep(1)
        self.entryFoundSignal.emit("testfile2.stock", "Test Two", "Test summary two")
        time.sleep(1)
        self.entryFoundSignal.emit("testfile3.stock", "Test Three", "Test summary three")
        time.sleep(1)

        self.searchFinishedSignal.emit()


def main():
    QCoreApplication.setApplicationName("HLSearch")
    QCoreApplication.setApplicationVersion("0.1")
    QCoreApplication.setOrganizationName("Tarsis")
    QCoreApplication.setOrganizationDomain("tarsis.org")

    app = QApplication(sys.argv)
    program = Main()
    program.show()
    app.exec_()

if __module__ == "main":
    main()
