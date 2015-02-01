# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GetRsaDialogImport.ui'
#
# Created: Thu May 15 15:45:58 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GetRsaDialogImport(object):
    def setupUi(self, GetRsaDialogImport):
        GetRsaDialogImport.setObjectName(_fromUtf8("GetRsaDialogImport"))
        GetRsaDialogImport.resize(512, 192)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GetRsaDialogImport.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(GetRsaDialogImport)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.icon = QtGui.QLabel(GetRsaDialogImport)
        self.icon.setMinimumSize(QtCore.QSize(128, 128))
        self.icon.setMaximumSize(QtCore.QSize(128, 128))
        self.icon.setObjectName(_fromUtf8("icon"))
        self.gridLayout.addWidget(self.icon, 0, 0, 2, 1)
        self.label_2 = QtGui.QLabel(GetRsaDialogImport)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(GetRsaDialogImport)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.toolButton = QtGui.QToolButton(GetRsaDialogImport)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.gridLayout.addWidget(self.toolButton, 1, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(GetRsaDialogImport)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(GetRsaDialogImport)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GetRsaDialogImport.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GetRsaDialogImport.reject)
        QtCore.QMetaObject.connectSlotsByName(GetRsaDialogImport)

    def retranslateUi(self, GetRsaDialogImport):
        GetRsaDialogImport.setWindowTitle(QtGui.QApplication.translate("GetRsaDialogImport", "Import key", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GetRsaDialogImport", "Select the new RSA key length", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("GetRsaDialogImport", "...", None, QtGui.QApplication.UnicodeUTF8))

