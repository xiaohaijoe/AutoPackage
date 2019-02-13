# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CopyDirToPathDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CopyDirToPathDialog(object):
    def setupUi(self, CopyDirToPathDialog):
        CopyDirToPathDialog.setObjectName("CopyDirToPathDialog")
        CopyDirToPathDialog.resize(715, 163)
        self.gridLayout_2 = QtWidgets.QGridLayout(CopyDirToPathDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.originBtn = QtWidgets.QPushButton(CopyDirToPathDialog)
        self.originBtn.setAutoDefault(False)
        self.originBtn.setObjectName("originBtn")
        self.gridLayout.addWidget(self.originBtn, 0, 2, 1, 1)
        self.originEdit = QtWidgets.QLineEdit(CopyDirToPathDialog)
        self.originEdit.setObjectName("originEdit")
        self.gridLayout.addWidget(self.originEdit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(CopyDirToPathDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(CopyDirToPathDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.destEdit = QtWidgets.QLineEdit(CopyDirToPathDialog)
        self.destEdit.setObjectName("destEdit")
        self.gridLayout.addWidget(self.destEdit, 1, 1, 1, 1)
        self.destBtn = QtWidgets.QPushButton(CopyDirToPathDialog)
        self.destBtn.setAutoDefault(False)
        self.destBtn.setObjectName("destBtn")
        self.gridLayout.addWidget(self.destBtn, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelBtn = QtWidgets.QPushButton(CopyDirToPathDialog)
        self.cancelBtn.setAutoDefault(False)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.confirmBtn = QtWidgets.QPushButton(CopyDirToPathDialog)
        self.confirmBtn.setObjectName("confirmBtn")
        self.horizontalLayout.addWidget(self.confirmBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        self.retranslateUi(CopyDirToPathDialog)
        QtCore.QMetaObject.connectSlotsByName(CopyDirToPathDialog)

    def retranslateUi(self, CopyDirToPathDialog):
        _translate = QtCore.QCoreApplication.translate
        CopyDirToPathDialog.setWindowTitle(_translate("CopyDirToPathDialog", "Dialog"))
        self.originBtn.setText(_translate("CopyDirToPathDialog", "选择"))
        self.label.setText(_translate("CopyDirToPathDialog", "源文件夹目录"))
        self.label_2.setText(_translate("CopyDirToPathDialog", "复制到目录"))
        self.destBtn.setText(_translate("CopyDirToPathDialog", "选择"))
        self.cancelBtn.setText(_translate("CopyDirToPathDialog", "取消"))
        self.confirmBtn.setText(_translate("CopyDirToPathDialog", "确认"))

