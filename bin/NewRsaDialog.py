# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewRsaDialog.ui'
#
# Created: Mon Apr 28 12:53:33 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NewRsaDialog(object):
    def setupUi(self, NewRsaDialog):
        NewRsaDialog.setObjectName(_fromUtf8("NewRsaDialog"))
        NewRsaDialog.resize(369, 340)
        self.gridLayout = QtGui.QGridLayout(NewRsaDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.newrsakey = QtGui.QSpinBox(NewRsaDialog)
        self.newrsakey.setSuffix(_fromUtf8(" bytes"))
        self.newrsakey.setMinimum(1024)
        self.newrsakey.setMaximum(65536)
        self.newrsakey.setSingleStep(256)
        self.newrsakey.setProperty("value", 2048)
        self.newrsakey.setObjectName(_fromUtf8("newrsakey"))
        self.gridLayout.addWidget(self.newrsakey, 0, 2, 1, 1)
        self.newrsakeyr = QtGui.QRadioButton(NewRsaDialog)
        self.newrsakeyr.setChecked(True)
        self.newrsakeyr.setObjectName(_fromUtf8("newrsakeyr"))
        self.gridLayout.addWidget(self.newrsakeyr, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.fromfiler = QtGui.QRadioButton(NewRsaDialog)
        self.fromfiler.setObjectName(_fromUtf8("fromfiler"))
        self.gridLayout.addWidget(self.fromfiler, 2, 0, 1, 1)
        self.newrsakeyd = QtGui.QDial(NewRsaDialog)
        self.newrsakeyd.setMaximumSize(QtCore.QSize(24, 24))
        self.newrsakeyd.setMinimum(1024)
        self.newrsakeyd.setMaximum(65536)
        self.newrsakeyd.setSingleStep(256)
        self.newrsakeyd.setPageStep(1024)
        self.newrsakeyd.setProperty("value", 2048)
        self.newrsakeyd.setObjectName(_fromUtf8("newrsakeyd"))
        self.gridLayout.addWidget(self.newrsakeyd, 0, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.label = QtGui.QLabel(NewRsaDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(NewRsaDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.actioni = QtGui.QLabel(self.groupBox)
        self.actioni.setMinimumSize(QtCore.QSize(25, 25))
        self.actioni.setMaximumSize(QtCore.QSize(25, 25))
        self.actioni.setText(_fromUtf8(""))
        self.actioni.setObjectName(_fromUtf8("actioni"))
        self.gridLayout_2.addWidget(self.actioni, 1, 2, 1, 1)
        self.keyid = QtGui.QLineEdit(self.groupBox)
        self.keyid.setReadOnly(True)
        self.keyid.setObjectName(_fromUtf8("keyid"))
        self.gridLayout_2.addWidget(self.keyid, 1, 1, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.groupBox)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_2.addWidget(self.textEdit, 2, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.textEdit_2 = QtGui.QTextEdit(self.groupBox)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout_2.addWidget(self.textEdit_2, 3, 1, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 4)
        self.fromfile = QtGui.QLineEdit(NewRsaDialog)
        self.fromfile.setEnabled(False)
        self.fromfile.setObjectName(_fromUtf8("fromfile"))
        self.gridLayout.addWidget(self.fromfile, 2, 2, 1, 1)
        self.fromfileb = QtGui.QToolButton(NewRsaDialog)
        self.fromfileb.setEnabled(True)
        self.fromfileb.setObjectName(_fromUtf8("fromfileb"))
        self.gridLayout.addWidget(self.fromfileb, 2, 3, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(NewRsaDialog)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 4)
        self.security = QtGui.QProgressBar(NewRsaDialog)
        self.security.setEnabled(True)
        self.security.setMaximum(10000)
        self.security.setProperty("value", 7500)
        self.security.setObjectName(_fromUtf8("security"))
        self.gridLayout.addWidget(self.security, 1, 1, 1, 3)
        self.action = QtGui.QPushButton(NewRsaDialog)
        self.action.setObjectName(_fromUtf8("action"))
        self.gridLayout.addWidget(self.action, 3, 0, 1, 4)

        self.retranslateUi(NewRsaDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewRsaDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewRsaDialog.reject)
        QtCore.QObject.connect(self.newrsakey, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.newrsakeyd.setValue)
        QtCore.QObject.connect(self.newrsakeyd, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.newrsakey.setValue)
        QtCore.QObject.connect(self.newrsakeyr, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.newrsakeyd.setEnabled)
        QtCore.QObject.connect(self.newrsakeyr, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.newrsakey.setEnabled)
        QtCore.QObject.connect(self.fromfiler, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.fromfileb.setEnabled)
        QtCore.QObject.connect(self.fromfiler, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.fromfile.setEnabled)
        QtCore.QObject.connect(self.newrsakeyr, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.security.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(NewRsaDialog)

    def retranslateUi(self, NewRsaDialog):
        NewRsaDialog.setWindowTitle(QtGui.QApplication.translate("NewRsaDialog", "New RSA", None, QtGui.QApplication.UnicodeUTF8))
        self.newrsakeyr.setText(QtGui.QApplication.translate("NewRsaDialog", "New RSA key", None, QtGui.QApplication.UnicodeUTF8))
        self.fromfiler.setText(QtGui.QApplication.translate("NewRsaDialog", "From existing file", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NewRsaDialog", "Security", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("NewRsaDialog", "Key", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NewRsaDialog", "Public key", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NewRsaDialog", "Key id", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("NewRsaDialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.fromfileb.setText(QtGui.QApplication.translate("NewRsaDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.security.setFormat(QtGui.QApplication.translate("NewRsaDialog", "%p%", None, QtGui.QApplication.UnicodeUTF8))
        self.action.setText(QtGui.QApplication.translate("NewRsaDialog", "Create", None, QtGui.QApplication.UnicodeUTF8))

