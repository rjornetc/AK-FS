# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GetRsaDialogCreate.ui'
#
# Created: Thu May 15 16:03:48 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GetRsaDialogCreate(object):
    def setupUi(self, GetRsaDialogCreate):
        GetRsaDialogCreate.setObjectName(_fromUtf8("GetRsaDialogCreate"))
        GetRsaDialogCreate.resize(512, 192)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GetRsaDialogCreate.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(GetRsaDialogCreate)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(GetRsaDialogCreate)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 2)
        self.security_label = QtGui.QLabel(GetRsaDialogCreate)
        self.security_label.setMaximumSize(QtCore.QSize(16777215, 22))
        self.security_label.setObjectName(_fromUtf8("security_label"))
        self.gridLayout.addWidget(self.security_label, 3, 1, 1, 1)
        self.security = QtGui.QProgressBar(GetRsaDialogCreate)
        self.security.setEnabled(True)
        self.security.setMaximum(10000)
        self.security.setProperty("value", 7500)
        self.security.setObjectName(_fromUtf8("security"))
        self.gridLayout.addWidget(self.security, 4, 1, 1, 1)
        self.keylength = QtGui.QSpinBox(GetRsaDialogCreate)
        self.keylength.setSuffix(_fromUtf8(" bytes"))
        self.keylength.setMinimum(1024)
        self.keylength.setMaximum(65536)
        self.keylength.setSingleStep(254)
        self.keylength.setProperty("value", 1024)
        self.keylength.setObjectName(_fromUtf8("keylength"))
        self.gridLayout.addWidget(self.keylength, 1, 1, 1, 1)
        self.icon = QtGui.QLabel(GetRsaDialogCreate)
        self.icon.setMinimumSize(QtCore.QSize(128, 128))
        self.icon.setMaximumSize(QtCore.QSize(128, 128))
        self.icon.setObjectName(_fromUtf8("icon"))
        self.gridLayout.addWidget(self.icon, 0, 0, 5, 1)
        self.description = QtGui.QLabel(GetRsaDialogCreate)
        self.description.setMinimumSize(QtCore.QSize(0, 0))
        self.description.setFrameShape(QtGui.QFrame.NoFrame)
        self.description.setWordWrap(True)
        self.description.setObjectName(_fromUtf8("description"))
        self.gridLayout.addWidget(self.description, 0, 1, 1, 1)
        self.keylength_slide = QtGui.QSlider(GetRsaDialogCreate)
        self.keylength_slide.setMinimum(4)
        self.keylength_slide.setMaximum(256)
        self.keylength_slide.setSingleStep(4)
        self.keylength_slide.setPageStep(8)
        self.keylength_slide.setProperty("value", 4)
        self.keylength_slide.setOrientation(QtCore.Qt.Horizontal)
        self.keylength_slide.setObjectName(_fromUtf8("keylength_slide"))
        self.gridLayout.addWidget(self.keylength_slide, 2, 1, 1, 1)

        self.retranslateUi(GetRsaDialogCreate)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GetRsaDialogCreate.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GetRsaDialogCreate.reject)
        QtCore.QMetaObject.connectSlotsByName(GetRsaDialogCreate)

    def retranslateUi(self, GetRsaDialogCreate):
        GetRsaDialogCreate.setWindowTitle(QtGui.QApplication.translate("GetRsaDialogCreate", "Create key", None, QtGui.QApplication.UnicodeUTF8))
        self.security_label.setText(QtGui.QApplication.translate("GetRsaDialogCreate", "Security", None, QtGui.QApplication.UnicodeUTF8))
        self.security.setFormat(QtGui.QApplication.translate("GetRsaDialogCreate", "%p%", None, QtGui.QApplication.UnicodeUTF8))
        self.description.setText(QtGui.QApplication.translate("GetRsaDialogCreate", "Select the new RSA key length.\n"
"The longer the key, the slower his generation but the faster the encryption of large files.", None, QtGui.QApplication.UnicodeUTF8))

