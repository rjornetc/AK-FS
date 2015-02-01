# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GetRsaDialogShow.ui'
#
# Created: Thu May 15 15:44:23 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GetRsaDialogShow(object):
    def setupUi(self, GetRsaDialogShow):
        GetRsaDialogShow.setObjectName(_fromUtf8("GetRsaDialogShow"))
        GetRsaDialogShow.resize(422, 256)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GetRsaDialogShow.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(GetRsaDialogShow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.key_pem = QtGui.QTextEdit(GetRsaDialogShow)
        self.key_pem.setMinimumSize(QtCore.QSize(414, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier 10 Pitch"))
        font.setPointSize(8)
        self.key_pem.setFont(font)
        self.key_pem.setReadOnly(True)
        self.key_pem.setObjectName(_fromUtf8("key_pem"))
        self.gridLayout.addWidget(self.key_pem, 0, 0, 1, 1)
        self.key_pem_copy = QtGui.QPushButton(GetRsaDialogShow)
        self.key_pem_copy.setEnabled(False)
        self.key_pem_copy.setObjectName(_fromUtf8("key_pem_copy"))
        self.gridLayout.addWidget(self.key_pem_copy, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(GetRsaDialogShow)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(GetRsaDialogShow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GetRsaDialogShow.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GetRsaDialogShow.reject)
        QtCore.QObject.connect(self.key_pem, QtCore.SIGNAL(_fromUtf8("selectionChanged()")), self.key_pem.selectAll)
        QtCore.QObject.connect(self.key_pem, QtCore.SIGNAL(_fromUtf8("copyAvailable(bool)")), self.key_pem_copy.setEnabled)
        QtCore.QObject.connect(self.key_pem_copy, QtCore.SIGNAL(_fromUtf8("clicked()")), self.key_pem.copy)
        QtCore.QMetaObject.connectSlotsByName(GetRsaDialogShow)

    def retranslateUi(self, GetRsaDialogShow):
        GetRsaDialogShow.setWindowTitle(QtGui.QApplication.translate("GetRsaDialogShow", "RSA Key", None, QtGui.QApplication.UnicodeUTF8))
        self.key_pem_copy.setText(QtGui.QApplication.translate("GetRsaDialogShow", "Copy", None, QtGui.QApplication.UnicodeUTF8))

