# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RemoveFileDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RemoveFileDialog(object):
    def setupUi(self, RemoveFileDialog):
        RemoveFileDialog.setObjectName("RemoveFileDialog")
        RemoveFileDialog.resize(669, 150)
        self.gridLayout_2 = QtWidgets.QGridLayout(RemoveFileDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(RemoveFileDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.originEdit = QtWidgets.QLineEdit(RemoveFileDialog)
        self.originEdit.setObjectName("originEdit")
        self.gridLayout.addWidget(self.originEdit, 1, 1, 1, 1)
        self.originBtn = QtWidgets.QPushButton(RemoveFileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.originBtn.sizePolicy().hasHeightForWidth())
        self.originBtn.setSizePolicy(sizePolicy)
        self.originBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.originBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.originBtn.setSizeIncrement(QtCore.QSize(0, 0))
        self.originBtn.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setKerning(True)
        self.originBtn.setFont(font)
        self.originBtn.setAutoDefault(False)
        self.originBtn.setFlat(False)
        self.originBtn.setObjectName("originBtn")
        self.gridLayout.addWidget(self.originBtn, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(RemoveFileDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileRadio = QtWidgets.QRadioButton(RemoveFileDialog)
        self.fileRadio.setChecked(True)
        self.fileRadio.setObjectName("fileRadio")
        self.horizontalLayout.addWidget(self.fileRadio)
        self.dirRadio = QtWidgets.QRadioButton(RemoveFileDialog)
        self.dirRadio.setObjectName("dirRadio")
        self.horizontalLayout.addWidget(self.dirRadio)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cancelBtn = QtWidgets.QPushButton(RemoveFileDialog)
        self.cancelBtn.setAutoDefault(False)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_2.addWidget(self.cancelBtn)
        self.confirmBtn = QtWidgets.QPushButton(RemoveFileDialog)
        self.confirmBtn.setObjectName("confirmBtn")
        self.horizontalLayout_2.addWidget(self.confirmBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.retranslateUi(RemoveFileDialog)
        QtCore.QMetaObject.connectSlotsByName(RemoveFileDialog)

    def retranslateUi(self, RemoveFileDialog):
        _translate = QtCore.QCoreApplication.translate
        RemoveFileDialog.setWindowTitle(_translate("RemoveFileDialog", "Dialog"))
        self.label.setText(_translate("RemoveFileDialog", "文件路径"))
        self.originBtn.setText(_translate("RemoveFileDialog", "选择"))
        self.label_2.setText(_translate("RemoveFileDialog", "文件类型"))
        self.fileRadio.setText(_translate("RemoveFileDialog", "文件"))
        self.dirRadio.setText(_translate("RemoveFileDialog", "文件夹"))
        self.cancelBtn.setText(_translate("RemoveFileDialog", "取消"))
        self.confirmBtn.setText(_translate("RemoveFileDialog", "确认"))

