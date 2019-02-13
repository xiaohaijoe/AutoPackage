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
        OpenTerminalDialog.resize(491, 117)
        self.gridLayout_2 = QtWidgets.QGridLayout(OpenTerminalDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(OpenTerminalDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.destBtn = QtWidgets.QPushButton(OpenTerminalDialog)
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
        self.destEdit = QtWidgets.QLineEdit(OpenTerminalDialog)
        self.destEdit.setObjectName("destEdit")
        self.gridLayout.addWidget(self.destEdit, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelBtn = QtWidgets.QPushButton(OpenTerminalDialog)
        self.cancelBtn.setAutoDefault(False)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.confirmBtn = QtWidgets.QPushButton(OpenTerminalDialog)
        self.confirmBtn.setObjectName("confirmBtn")
        self.horizontalLayout.addWidget(self.confirmBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        self.retranslateUi(OpenTerminalDialog)
        QtCore.QMetaObject.connectSlotsByName(OpenTerminalDialog)

    def retranslateUi(self, OpenTerminalDialog):
        _translate = QtCore.QCoreApplication.translate
        OpenTerminalDialog.setWindowTitle(_translate("OpenTerminalDialog", "Dialog"))
        self.label.setText(_translate("OpenTerminalDialog", "终端目录"))
        self.destBtn.setText(_translate("OpenTerminalDialog", "选择"))
        self.cancelBtn.setText(_translate("OpenTerminalDialog", "取消"))
        self.confirmBtn.setText(_translate("OpenTerminalDialog", "确认"))

