# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GetRsaDialog.ui'
#
# Created: Thu May 15 15:45:45 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GetRsaDialog(object):
    def setupUi(self, GetRsaDialog):
        GetRsaDialog.setObjectName(_fromUtf8("GetRsaDialog"))
        GetRsaDialog.resize(512, 192)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GetRsaDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(GetRsaDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(GetRsaDialog)
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(GetRsaDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 2)
        self.newrsakeyr = QtGui.QRadioButton(GetRsaDialog)
        self.newrsakeyr.setIcon(icon)
        self.newrsakeyr.setChecked(True)
        self.newrsakeyr.setObjectName(_fromUtf8("newrsakeyr"))
        self.gridLayout.addWidget(self.newrsakeyr, 1, 1, 1, 1)
        self.fromfiler = QtGui.QRadioButton(GetRsaDialog)
        self.fromfiler.setIcon(icon)
        self.fromfiler.setObjectName(_fromUtf8("fromfiler"))
        self.gridLayout.addWidget(self.fromfiler, 2, 1, 1, 1)
        self.icon = QtGui.QLabel(GetRsaDialog)
        self.icon.setMinimumSize(QtCore.QSize(128, 128))
        self.icon.setMaximumSize(QtCore.QSize(128, 128))
        self.icon.setObjectName(_fromUtf8("icon"))
        self.gridLayout.addWidget(self.icon, 0, 0, 3, 1)

        self.retranslateUi(GetRsaDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GetRsaDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GetRsaDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GetRsaDialog)

    def retranslateUi(self, GetRsaDialog):
        GetRsaDialog.setWindowTitle(QtGui.QApplication.translate("GetRsaDialog", "Get key", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GetRsaDialog", "How do you want to get your RSA key?\n"
" If you don\'t understand the question, select \"Create a new RSA Key\"", None, QtGui.QApplication.UnicodeUTF8))
        self.newrsakeyr.setText(QtGui.QApplication.translate("GetRsaDialog", "Create a new RSA Key", None, QtGui.QApplication.UnicodeUTF8))
        self.fromfiler.setText(QtGui.QApplication.translate("GetRsaDialog", "Import from existing file", None, QtGui.QApplication.UnicodeUTF8))

