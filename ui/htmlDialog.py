# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'htmlDialog.ui'
#
# Created: Thu May  9 09:15:26 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_htmlDialog(object):
    def setupUi(self, htmlDialog):
        htmlDialog.setObjectName(_fromUtf8("htmlDialog"))
        htmlDialog.resize(766, 661)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/user_info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        htmlDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(htmlDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView = QtWebKit.QWebView(htmlDialog)
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)

        self.retranslateUi(htmlDialog)
        QtCore.QMetaObject.connectSlotsByName(htmlDialog)

    def retranslateUi(self, htmlDialog):
        htmlDialog.setWindowTitle(QtGui.QApplication.translate("htmlDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
import icons_rc
