# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImportDialog.ui'
#
# Created: Tue Apr 22 14:30:15 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ImportDialog(object):
    def setupUi(self, ImportDialog):
        ImportDialog.setObjectName(_fromUtf8("ImportDialog"))
        ImportDialog.resize(307, 135)
        self.gridLayout = QtGui.QGridLayout(ImportDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.keylengthLabel = QtGui.QLabel(ImportDialog)
        self.keylengthLabel.setObjectName(_fromUtf8("keylengthLabel"))
        self.gridLayout.addWidget(self.keylengthLabel, 3, 0, 1, 1)
        self.filenameLabel = QtGui.QLabel(ImportDialog)
        self.filenameLabel.setObjectName(_fromUtf8("filenameLabel"))
        self.gridLayout.addWidget(self.filenameLabel, 2, 0, 1, 1)
        self.importfileLabel = QtGui.QLabel(ImportDialog)
        self.importfileLabel.setObjectName(_fromUtf8("importfileLabel"))
        self.gridLayout.addWidget(self.importfileLabel, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ImportDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 4)
        self.colectionLabel = QtGui.QLabel(ImportDialog)
        self.colectionLabel.setObjectName(_fromUtf8("colectionLabel"))
        self.gridLayout.addWidget(self.colectionLabel, 1, 0, 1, 1)
        self.importfileLineedit = QtGui.QLineEdit(ImportDialog)
        self.importfileLineedit.setObjectName(_fromUtf8("importfileLineedit"))
        self.gridLayout.addWidget(self.importfileLineedit, 0, 2, 1, 1)
        self.colectionCombobox = QtGui.QComboBox(ImportDialog)
        self.colectionCombobox.setObjectName(_fromUtf8("colectionCombobox"))
        self.gridLayout.addWidget(self.colectionCombobox, 1, 2, 1, 2)
        self.importfileToolbutton = QtGui.QToolButton(ImportDialog)
        self.importfileToolbutton.setObjectName(_fromUtf8("importfileToolbutton"))
        self.gridLayout.addWidget(self.importfileToolbutton, 0, 3, 1, 1)
        self.filenameLineedit = QtGui.QLineEdit(ImportDialog)
        self.filenameLineedit.setObjectName(_fromUtf8("filenameLineedit"))
        self.gridLayout.addWidget(self.filenameLineedit, 2, 2, 1, 2)
        self.securityProgressbar = QtGui.QProgressBar(ImportDialog)
        self.securityProgressbar.setMinimum(16)
        self.securityProgressbar.setMaximum(32)
        self.securityProgressbar.setProperty("value", 32)
        self.securityProgressbar.setFormat(_fromUtf8(""))
        self.securityProgressbar.setObjectName(_fromUtf8("securityProgressbar"))
        self.gridLayout.addWidget(self.securityProgressbar, 4, 2, 1, 2)
        self.label = QtGui.QLabel(ImportDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.keylengthSpinbox = QtGui.QSpinBox(ImportDialog)
        self.keylengthSpinbox.setMinimum(16)
        self.keylengthSpinbox.setMaximum(32)
        self.keylengthSpinbox.setSingleStep(8)
        self.keylengthSpinbox.setProperty("value", 32)
        self.keylengthSpinbox.setObjectName(_fromUtf8("keylengthSpinbox"))
        self.gridLayout.addWidget(self.keylengthSpinbox, 3, 2, 1, 2)

        self.retranslateUi(ImportDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ImportDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ImportDialog.reject)
        QtCore.QObject.connect(self.keylengthSpinbox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.securityProgressbar.setValue)
        QtCore.QMetaObject.connectSlotsByName(ImportDialog)

    def retranslateUi(self, ImportDialog):
        ImportDialog.setWindowTitle(QtGui.QApplication.translate("ImportDialog", "Imput", None, QtGui.QApplication.UnicodeUTF8))
        self.keylengthLabel.setText(QtGui.QApplication.translate("ImportDialog", "Key length", None, QtGui.QApplication.UnicodeUTF8))
        self.filenameLabel.setText(QtGui.QApplication.translate("ImportDialog", "File name", None, QtGui.QApplication.UnicodeUTF8))
        self.importfileLabel.setText(QtGui.QApplication.translate("ImportDialog", "Import file", None, QtGui.QApplication.UnicodeUTF8))
        self.colectionLabel.setText(QtGui.QApplication.translate("ImportDialog", "Colection", None, QtGui.QApplication.UnicodeUTF8))
        self.importfileToolbutton.setText(QtGui.QApplication.translate("ImportDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ImportDialog", "Security", None, QtGui.QApplication.UnicodeUTF8))

