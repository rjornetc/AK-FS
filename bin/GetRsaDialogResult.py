# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GetRsaDialogResult.ui'
#
# Created: Thu May 15 15:44:38 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GetRsaDialogResult(object):
    def setupUi(self, GetRsaDialogResult):
        GetRsaDialogResult.setObjectName(_fromUtf8("GetRsaDialogResult"))
        GetRsaDialogResult.resize(613, 192)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GetRsaDialogResult.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(GetRsaDialogResult)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.key_identicon = QtGui.QLabel(GetRsaDialogResult)
        self.key_identicon.setMinimumSize(QtCore.QSize(25, 25))
        self.key_identicon.setMaximumSize(QtCore.QSize(24, 24))
        self.key_identicon.setText(_fromUtf8(""))
        self.key_identicon.setObjectName(_fromUtf8("key_identicon"))
        self.gridLayout.addWidget(self.key_identicon, 1, 3, 1, 1)
        self.rsakey_show = QtGui.QToolButton(GetRsaDialogResult)
        self.rsakey_show.setMinimumSize(QtCore.QSize(22, 22))
        self.rsakey_show.setMaximumSize(QtCore.QSize(24, 24))
        self.rsakey_show.setText(_fromUtf8(""))
        self.rsakey_show.setIcon(icon)
        self.rsakey_show.setObjectName(_fromUtf8("rsakey_show"))
        self.gridLayout.addWidget(self.rsakey_show, 1, 4, 1, 1)
        self.key_id_label = QtGui.QLabel(GetRsaDialogResult)
        self.key_id_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.key_id_label.setObjectName(_fromUtf8("key_id_label"))
        self.gridLayout.addWidget(self.key_id_label, 1, 1, 1, 1)
        self.key_id = QtGui.QLineEdit(GetRsaDialogResult)
        self.key_id.setReadOnly(True)
        self.key_id.setObjectName(_fromUtf8("key_id"))
        self.gridLayout.addWidget(self.key_id, 1, 2, 1, 1)
        self.description = QtGui.QLabel(GetRsaDialogResult)
        self.description.setMinimumSize(QtCore.QSize(0, 0))
        self.description.setFrameShape(QtGui.QFrame.NoFrame)
        self.description.setWordWrap(True)
        self.description.setObjectName(_fromUtf8("description"))
        self.gridLayout.addWidget(self.description, 0, 1, 1, 4)
        self.icon = QtGui.QLabel(GetRsaDialogResult)
        self.icon.setMinimumSize(QtCore.QSize(128, 128))
        self.icon.setMaximumSize(QtCore.QSize(128, 128))
        self.icon.setObjectName(_fromUtf8("icon"))
        self.gridLayout.addWidget(self.icon, 0, 0, 3, 1)
        self.buttonBox = QtGui.QDialogButtonBox(GetRsaDialogResult)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Discard|QtGui.QDialogButtonBox.Retry|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 5)
        self.key_id_label.setBuddy(self.key_id)

        self.retranslateUi(GetRsaDialogResult)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GetRsaDialogResult.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GetRsaDialogResult.reject)
        QtCore.QMetaObject.connectSlotsByName(GetRsaDialogResult)

    def retranslateUi(self, GetRsaDialogResult):
        GetRsaDialogResult.setWindowTitle(QtGui.QApplication.translate("GetRsaDialogResult", "Create key", None, QtGui.QApplication.UnicodeUTF8))
        self.rsakey_show.setToolTip(QtGui.QApplication.translate("GetRsaDialogResult", "Show public RSA key", None, QtGui.QApplication.UnicodeUTF8))
        self.key_id_label.setText(QtGui.QApplication.translate("GetRsaDialogResult", "Key id", None, QtGui.QApplication.UnicodeUTF8))
        self.description.setText(QtGui.QApplication.translate("GetRsaDialogResult", "This is the resulting key id and key identicon. This same identicon will be saw by anyone who import your key. You can create a new key in order to get a coolest one :D", None, QtGui.QApplication.UnicodeUTF8))

