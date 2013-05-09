__appname__ = "HLSearch"
__module__ = "main"

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui import mainWindow, htmlDialog
import os
import re
from herolab import HeroLabIndex, HeroLab


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
        self.tableWidget.cellDoubleClicked.connect(self.table_widget_doubleclicked)

    def load_initial_settings(self):
        """Setup the initial values"""
        self.settings = QSettings(QSettings.NativeFormat, QSettings.UserScope, "Tarsis", "HLSearch")
        folder = self.settings.value('search_folder').toString()

        if folder == '':
            folder = os.getcwd()

        self.search_folder = folder
        self.tableWidget.setColumnCount(4)
        self.tableWidget.hideColumn(0)

        self.tableWidget.setColumnWidth(1, 300)
        self.tableWidget.setColumnWidth(2, 200)
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
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.searchThread.search_folder = self.search_folder
        self.searchThread.search_text = str(self.searchEdit.text())
        self.searchThread.start()

    def entry_found(self, source, filename, name, summary):
        if self.tableWidget.rowCount() < self.row + 1:
            self.tableWidget.setRowCount(self.row + 1)

        self.tableWidget.setItem(self.row, 0, QTableWidgetItem(filename))
        self.tableWidget.setItem(self.row, 1, QTableWidgetItem(source))
        self.tableWidget.setItem(self.row, 2, QTableWidgetItem(name))
        self.tableWidget.setItem(self.row, 3, QTableWidgetItem(summary))
        self.row += 1

    def search_finished(self):
        self.searchButton.setDisabled(False)
        if self.errors and not self.actionWarnings.isChecked():
            QMessageBox.warning(self, __appname__ + " Errors", self.errors)

        if self.tableWidget.rowCount() < 1:
            QMessageBox.information(self, __appname__ + " No Results", "No search results found")

        self.tableWidget.setSortingEnabled(True)

    def search_error(self, error):
        self.errors += error

    def table_widget_doubleclicked(self, row, _):
        filename = self.tableWidget.item(row, 0).text()
        source = self.tableWidget.item(row, 1).text()

        heroLab = HeroLab(self.search_folder, source, filename)
        if heroLab.html != '':
            htmlDialog = HtmlDialog(self)
            htmlDialog.show_html(heroLab.html)
        else:
            QMessageBox.warning(self, __appname__ + " Error", "Could not find HTML in file")


class SearchThread(QThread):

    entryFoundSignal = pyqtSignal(str, str, str, str)
    searchFinishedSignal = pyqtSignal()
    searchErrorSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(SearchThread, self).__init__(parent)

    def run(self):
        """Here we'll search through the files and pass the output up"""

        heroLabIndex = HeroLabIndex(self.search_folder)

        for entry in heroLabIndex.get_creatures():
            if re.search(self.search_text, entry["name"], re.IGNORECASE):
                self.entryFoundSignal.emit(entry["source"], entry["filename"], entry["name"], entry["summary"])

        for bad_file in heroLabIndex.bad_files:
            self.searchErrorSignal.emit("Could not open file %s\n" % bad_file)

        self.searchFinishedSignal.emit()


class HtmlDialog(QDialog, htmlDialog.Ui_htmlDialog):

    def __init__(self, parent):
        super(HtmlDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(__appname__ + " Statblock")

    def show_html(self, html):
        self.webView.setHtml(html)
        self.show()


def main():
    QCoreApplication.setApplicationName("HLSearch")
    QCoreApplication.setApplicationVersion("0.2")
    QCoreApplication.setOrganizationName("Tarsis")
    QCoreApplication.setOrganizationDomain("tarsis.org")

    app = QApplication(sys.argv)
    program = Main()
    program.show()
    app.exec_()

if __module__ == "main":
    main()
