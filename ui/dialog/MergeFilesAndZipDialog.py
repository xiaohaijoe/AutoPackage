# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MergeFilesAndZipDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MergeFilesAndZipDialog(object):
    def setupUi(self, MergeFilesAndZipDialog):
        MergeFilesAndZipDialog.setObjectName("MergeFilesAndZipDialog")
        MergeFilesAndZipDialog.resize(618, 378)
        self.gridLayout_2 = QtWidgets.QGridLayout(MergeFilesAndZipDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileRadio = QtWidgets.QRadioButton(MergeFilesAndZipDialog)
        self.fileRadio.setChecked(True)
        self.fileRadio.setObjectName("fileRadio")
        self.horizontalLayout.addWidget(self.fileRadio)
        self.dirRadio = QtWidgets.QRadioButton(MergeFilesAndZipDialog)
        self.dirRadio.setObjectName("dirRadio")
        self.horizontalLayout.addWidget(self.dirRadio)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(MergeFilesAndZipDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.originBtn = QtWidgets.QPushButton(MergeFilesAndZipDialog)
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
        self.gridLayout.addWidget(self.originBtn, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 3)
        self.label = QtWidgets.QLabel(MergeFilesAndZipDialog)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.listView = QtWidgets.QListView(MergeFilesAndZipDialog)
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.setObjectName("listView")
        self.gridLayout_2.addWidget(self.listView, 2, 0, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(MergeFilesAndZipDialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.zipEdit = QtWidgets.QLineEdit(MergeFilesAndZipDialog)
        self.zipEdit.setObjectName("zipEdit")
        self.horizontalLayout_2.addWidget(self.zipEdit)
        self.zipBtn = QtWidgets.QPushButton(MergeFilesAndZipDialog)
        self.zipBtn.setAutoDefault(False)
        self.zipBtn.setObjectName("zipBtn")
        self.horizontalLayout_2.addWidget(self.zipBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 3)
        self.cancelBtn = QtWidgets.QPushButton(MergeFilesAndZipDialog)
        self.cancelBtn.setAutoDefault(False)
        self.cancelBtn.setObjectName("cancelBtn")
        self.gridLayout_2.addWidget(self.cancelBtn, 4, 1, 1, 1)
        self.confirmBtn = QtWidgets.QPushButton(MergeFilesAndZipDialog)
        self.confirmBtn.setObjectName("confirmBtn")
        self.gridLayout_2.addWidget(self.confirmBtn, 4, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)

        self.retranslateUi(MergeFilesAndZipDialog)
        QtCore.QMetaObject.connectSlotsByName(MergeFilesAndZipDialog)

    def retranslateUi(self, MergeFilesAndZipDialog):
        _translate = QtCore.QCoreApplication.translate
        MergeFilesAndZipDialog.setWindowTitle(_translate("MergeFilesAndZipDialog", "Dialog"))
        self.fileRadio.setText(_translate("MergeFilesAndZipDialog", "文件"))
        self.dirRadio.setText(_translate("MergeFilesAndZipDialog", "文件夹"))
        self.label_2.setText(_translate("MergeFilesAndZipDialog", "文件类型"))
        self.originBtn.setText(_translate("MergeFilesAndZipDialog", "添加"))
        self.label.setText(_translate("MergeFilesAndZipDialog", "已选文件"))
        self.label_4.setText(_translate("MergeFilesAndZipDialog", "压缩到文件"))
        self.zipBtn.setText(_translate("MergeFilesAndZipDialog", "选择"))
        self.cancelBtn.setText(_translate("MergeFilesAndZipDialog", "取消"))
        self.confirmBtn.setText(_translate("MergeFilesAndZipDialog", "确认"))

