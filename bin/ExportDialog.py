# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExportDialog.ui'
#
# Created: Tue Apr 22 23:31:49 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ExportDialog(object):
    def setupUi(self, ExportDialog):
        ExportDialog.setObjectName(_fromUtf8("ExportDialog"))
        ExportDialog.resize(307, 117)
        self.gridLayout = QtGui.QGridLayout(ExportDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.filenameLabel = QtGui.QLabel(ExportDialog)
        self.filenameLabel.setObjectName(_fromUtf8("filenameLabel"))
        self.gridLayout.addWidget(self.filenameLabel, 2, 0, 1, 1)
        self.exportfileLabel = QtGui.QLabel(ExportDialog)
        self.exportfileLabel.setObjectName(_fromUtf8("exportfileLabel"))
        self.gridLayout.addWidget(self.exportfileLabel, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ExportDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 4)
        self.colectionLabel = QtGui.QLabel(ExportDialog)
        self.colectionLabel.setObjectName(_fromUtf8("colectionLabel"))
        self.gridLayout.addWidget(self.colectionLabel, 1, 0, 1, 1)
        self.exportfileLineedit = QtGui.QLineEdit(ExportDialog)
        self.exportfileLineedit.setObjectName(_fromUtf8("exportfileLineedit"))
        self.gridLayout.addWidget(self.exportfileLineedit, 0, 2, 1, 1)
        self.colectionCombobox = QtGui.QComboBox(ExportDialog)
        self.colectionCombobox.setObjectName(_fromUtf8("colectionCombobox"))
        self.gridLayout.addWidget(self.colectionCombobox, 1, 2, 1, 2)
        self.importfileToolbutton = QtGui.QToolButton(ExportDialog)
        self.importfileToolbutton.setObjectName(_fromUtf8("importfileToolbutton"))
        self.gridLayout.addWidget(self.importfileToolbutton, 0, 3, 1, 1)
        self.filenameCombobox = QtGui.QComboBox(ExportDialog)
        self.filenameCombobox.setObjectName(_fromUtf8("filenameCombobox"))
        self.gridLayout.addWidget(self.filenameCombobox, 2, 2, 1, 2)

        self.retranslateUi(ExportDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ExportDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ExportDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExportDialog)

    def retranslateUi(self, ExportDialog):
        ExportDialog.setWindowTitle(QtGui.QApplication.translate("ExportDialog", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.filenameLabel.setText(QtGui.QApplication.translate("ExportDialog", "File name", None, QtGui.QApplication.UnicodeUTF8))
        self.exportfileLabel.setText(QtGui.QApplication.translate("ExportDialog", "Export file", None, QtGui.QApplication.UnicodeUTF8))
        self.colectionLabel.setText(QtGui.QApplication.translate("ExportDialog", "Colection", None, QtGui.QApplication.UnicodeUTF8))
        self.importfileToolbutton.setText(QtGui.QApplication.translate("ExportDialog", "...", None, QtGui.QApplication.UnicodeUTF8))

