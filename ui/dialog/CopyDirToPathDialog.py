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
        CopyDirToPathDialog.resize(1006, 163)
        self.gridLayoutWidget = QtWidgets.QWidget(CopyDirToPathDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 961, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.originBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.originBtn.setObjectName("originBtn")
        self.gridLayout.addWidget(self.originBtn, 0, 2, 1, 1)
        self.originEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.originEdit.setObjectName("originEdit")
        self.gridLayout.addWidget(self.originEdit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.destEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.destEdit.setObjectName("destEdit")
        self.gridLayout.addWidget(self.destEdit, 1, 1, 1, 1)
        self.destBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.destBtn.setObjectName("destBtn")
        self.gridLayout.addWidget(self.destBtn, 1, 2, 1, 1)
        self.confirmBtn = QtWidgets.QPushButton(CopyDirToPathDialog)
        self.confirmBtn.setGeometry(QtCore.QRect(520, 110, 91, 32))
        self.confirmBtn.setObjectName("confirmBtn")
        self.cancelBtn = QtWidgets.QPushButton(CopyDirToPathDialog)
        self.cancelBtn.setGeometry(QtCore.QRect(427, 110, 91, 32))
        self.cancelBtn.setObjectName("cancelBtn")

        self.retranslateUi(CopyDirToPathDialog)
        QtCore.QMetaObject.connectSlotsByName(CopyDirToPathDialog)

    def retranslateUi(self, CopyDirToPathDialog):
        _translate = QtCore.QCoreApplication.translate
        CopyDirToPathDialog.setWindowTitle(_translate("CopyDirToPathDialog", "Dialog"))
        self.originBtn.setText(_translate("CopyDirToPathDialog", "选择"))
        self.label.setText(_translate("CopyDirToPathDialog", "源文件夹目录"))
        self.label_2.setText(_translate("CopyDirToPathDialog", "复制到目录"))
        self.destBtn.setText(_translate("CopyDirToPathDialog", "选择"))
        self.confirmBtn.setText(_translate("CopyDirToPathDialog", "确认"))
        self.cancelBtn.setText(_translate("CopyDirToPathDialog", "取消"))

