# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpenTerminalDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OpenTerminalDialog(object):
    def setupUi(self, OpenTerminalDialog):
        OpenTerminalDialog.setObjectName("OpenTerminalDialog")
        OpenTerminalDialog.resize(1000, 132)
        self.gridLayoutWidget = QtWidgets.QWidget(OpenTerminalDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 961, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.destBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.destBtn.sizePolicy().hasHeightForWidth())
        self.destBtn.setSizePolicy(sizePolicy)
        self.destBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.destBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.destBtn.setSizeIncrement(QtCore.QSize(0, 0))
        self.destBtn.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setKerning(True)
        self.destBtn.setFont(font)
        self.destBtn.setAutoDefault(False)
        self.destBtn.setFlat(False)
        self.destBtn.setObjectName("destBtn")
        self.gridLayout.addWidget(self.destBtn, 0, 2, 1, 1)
        self.destEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.destEdit.setObjectName("destEdit")
        self.gridLayout.addWidget(self.destEdit, 0, 1, 1, 1)
        self.confirmBtn = QtWidgets.QPushButton(OpenTerminalDialog)
        self.confirmBtn.setGeometry(QtCore.QRect(513, 80, 91, 32))
        self.confirmBtn.setObjectName("confirmBtn")
        self.cancelBtn = QtWidgets.QPushButton(OpenTerminalDialog)
        self.cancelBtn.setGeometry(QtCore.QRect(420, 80, 91, 32))
        self.cancelBtn.setObjectName("cancelBtn")

        self.retranslateUi(OpenTerminalDialog)
        QtCore.QMetaObject.connectSlotsByName(OpenTerminalDialog)

    def retranslateUi(self, OpenTerminalDialog):
        _translate = QtCore.QCoreApplication.translate
        OpenTerminalDialog.setWindowTitle(_translate("OpenTerminalDialog", "Dialog"))
        self.label.setText(_translate("OpenTerminalDialog", "终端目录"))
        self.destBtn.setText(_translate("OpenTerminalDialog", "选择"))
        self.confirmBtn.setText(_translate("OpenTerminalDialog", "确认"))
        self.cancelBtn.setText(_translate("OpenTerminalDialog", "取消"))

