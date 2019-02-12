# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CopyFileToPathDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CopyFileToPathDialog(object):
    def setupUi(self, CopyFileToPathDialog):
        CopyFileToPathDialog.setObjectName("CopyFileToPathDialog")
        CopyFileToPathDialog.resize(1000, 181)
        self.gridLayoutWidget = QtWidgets.QWidget(CopyFileToPathDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 961, 91))
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
        self.confirmBtn = QtWidgets.QPushButton(CopyFileToPathDialog)
        self.confirmBtn.setGeometry(QtCore.QRect(423, 130, 91, 32))
        self.confirmBtn.setObjectName("confirmBtn")
        self.cancelBtn = QtWidgets.QPushButton(CopyFileToPathDialog)
        self.cancelBtn.setGeometry(QtCore.QRect(330, 130, 91, 32))
        self.cancelBtn.setObjectName("cancelBtn")

        self.retranslateUi(CopyFileToPathDialog)
        QtCore.QMetaObject.connectSlotsByName(CopyFileToPathDialog)

    def retranslateUi(self, CopyFileToPathDialog):
        _translate = QtCore.QCoreApplication.translate
        CopyFileToPathDialog.setWindowTitle(_translate("CopyFileToPathDialog", "Dialog"))
        self.originBtn.setText(_translate("CopyFileToPathDialog", "选择"))
        self.label.setText(_translate("CopyFileToPathDialog", "源文件路径"))
        self.label_2.setText(_translate("CopyFileToPathDialog", "复制到目录"))
        self.destBtn.setText(_translate("CopyFileToPathDialog", "选择"))
        self.confirmBtn.setText(_translate("CopyFileToPathDialog", "确认"))
        self.cancelBtn.setText(_translate("CopyFileToPathDialog", "取消"))

