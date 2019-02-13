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
        TernimalCommandDialog.resize(685, 130)
        self.gridLayout_2 = QtWidgets.QGridLayout(TernimalCommandDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(TernimalCommandDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.terminalCommandEdit = QtWidgets.QLineEdit(TernimalCommandDialog)
        self.terminalCommandEdit.setObjectName("terminalCommandEdit")
        self.gridLayout.addWidget(self.terminalCommandEdit, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelBtn = QtWidgets.QPushButton(TernimalCommandDialog)
        self.cancelBtn.setAutoDefault(False)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.confirmBtn = QtWidgets.QPushButton(TernimalCommandDialog)
        self.confirmBtn.setObjectName("confirmBtn")
        self.horizontalLayout.addWidget(self.confirmBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        self.retranslateUi(TernimalCommandDialog)
        QtCore.QMetaObject.connectSlotsByName(TernimalCommandDialog)

    def retranslateUi(self, TernimalCommandDialog):
        _translate = QtCore.QCoreApplication.translate
        TernimalCommandDialog.setWindowTitle(_translate("TernimalCommandDialog", "Dialog"))
        self.label.setText(_translate("TernimalCommandDialog", "执行命令"))
        self.cancelBtn.setText(_translate("TernimalCommandDialog", "取消"))
        self.confirmBtn.setText(_translate("TernimalCommandDialog", "确认"))

