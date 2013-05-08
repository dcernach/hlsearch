__appname__ = "HLSearch"
__module__ = "main"

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui import mainWindow
import os
import re
from herolab import HeroLabIndex


class Main(QMainWindow, mainWindow.Ui_mainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(__appname__)

        self.load_initial_settings()
        self.searchThread = SearchThread()
        self.searchThread.entryFoundSignal.connect(self.entry_found)
        self.searchThread.searchFinishedSignal.connect(self.search_finished)
        self.searchThread.searchErrorSignal.connect(self.search_error)

        self.actionFolder.triggered.connect(self.action_search_folder_triggered)
        self.searchButton.clicked.connect(self.search_button_clicked)
        self.actionWarnings.triggered.connect(self.action_warnings_triggered)
        self.searchEdit.returnPressed.connect(self.search_button_clicked)
        self.actionExit.triggered.connect(self.close)

    def load_initial_settings(self):
        """Setup the initial values"""
        self.settings = QSettings(QSettings.NativeFormat, QSettings.UserScope, "Tarsis", "HLSearch")
        folder = self.settings.value('search_folder').toString()

        if folder == '':
            folder = os.getcwd()

        self.search_folder = folder
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.setColumnWidth(1, 200)
        if self.settings.contains('disable_warnings'):
            self.actionWarnings.setChecked(self.settings.value('disable_warnings').toBool())

    def action_search_folder_triggered(self):
        """Ask the user for the search folder"""

        folder = QFileDialog.getExistingDirectory(self, "Hero Lab Data Folder", self.search_folder,
                                                  QFileDialog.ShowDirsOnly)

        if folder != '':
            self.search_folder = folder
            self.settings.setValue('search_folder', folder)

    def action_warnings_triggered(self):
        self.settings.setValue('disable_warnings', self.actionWarnings.isChecked())

    def search_button_clicked(self):
        """Search through the files and display the output"""
        self.row = 0
        self.errors = ""
        self.searchButton.setDisabled(True)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.searchThread.search_folder = self.search_folder
        self.searchThread.search_text = str(self.searchEdit.text())
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
        if self.errors and not self.actionWarnings.isChecked():
            QMessageBox.warning(self, __appname__ + " Errors", self.errors)

    def search_error(self, error):
        self.errors += error


class SearchThread(QThread):

    entryFoundSignal = pyqtSignal(str, str, str)
    searchFinishedSignal = pyqtSignal()
    searchErrorSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(SearchThread, self).__init__(parent)

    def run(self):
        """Here we'll search through the files and pass the output up"""

        heroLabIndex = HeroLabIndex(self.search_folder)

        for entry in heroLabIndex.get_creatures():
            if re.search(self.search_text, entry["name"], re.IGNORECASE):
                self.entryFoundSignal.emit(entry["filename"], entry["name"], entry["summary"])

        for bad_file in heroLabIndex.bad_files:
            self.searchErrorSignal.emit("Could not open file %s\n" % bad_file)

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
