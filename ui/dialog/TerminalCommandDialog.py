# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TerminalCommandDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TernimalCommandDialog(object):
    def setupUi(self, TernimalCommandDialog):
        TernimalCommandDialog.setObjectName("TernimalCommandDialog")
        TernimalCommandDialog.resize(1000, 130)
        self.gridLayoutWidget = QtWidgets.QWidget(TernimalCommandDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 961, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.terminalCommandEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.terminalCommandEdit.setObjectName("terminalCommandEdit")
        self.gridLayout.addWidget(self.terminalCommandEdit, 0, 1, 1, 1)
        self.confirmBtn = QtWidgets.QPushButton(TernimalCommandDialog)
        self.confirmBtn.setGeometry(QtCore.QRect(513, 80, 91, 32))
        self.confirmBtn.setObjectName("confirmBtn")
        self.cancelBtn = QtWidgets.QPushButton(TernimalCommandDialog)
        self.cancelBtn.setGeometry(QtCore.QRect(420, 80, 91, 32))
        self.cancelBtn.setObjectName("cancelBtn")

        self.retranslateUi(TernimalCommandDialog)
        QtCore.QMetaObject.connectSlotsByName(TernimalCommandDialog)

    def retranslateUi(self, TernimalCommandDialog):
        _translate = QtCore.QCoreApplication.translate
        TernimalCommandDialog.setWindowTitle(_translate("TernimalCommandDialog", "Dialog"))
        self.label.setText(_translate("TernimalCommandDialog", "执行命令"))
        self.confirmBtn.setText(_translate("TernimalCommandDialog", "确认"))
        self.cancelBtn.setText(_translate("TernimalCommandDialog", "取消"))

