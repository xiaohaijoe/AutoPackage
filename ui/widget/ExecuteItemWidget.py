# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExecuteItemWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExecuteItemWidget(object):
    def setupUi(self, ExecuteItemWidget):
        ExecuteItemWidget.setObjectName("ExecuteItemWidget")
        ExecuteItemWidget.resize(351, 182)
        self.gridLayoutWidget = QtWidgets.QWidget(ExecuteItemWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 353, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.nameLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.nameLabel.setWordWrap(True)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout_4.addWidget(self.nameLabel)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.editBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.editBtn.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editBtn.setFont(font)
        self.editBtn.setObjectName("editBtn")
        self.horizontalLayout_5.addWidget(self.editBtn)
        self.moveDownBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.moveDownBtn.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.moveDownBtn.setFont(font)
        self.moveDownBtn.setObjectName("moveDownBtn")
        self.horizontalLayout_5.addWidget(self.moveDownBtn)
        self.moveUpBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.moveUpBtn.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.moveUpBtn.setFont(font)
        self.moveUpBtn.setObjectName("moveUpBtn")
        self.horizontalLayout_5.addWidget(self.moveUpBtn)
        self.removeBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.removeBtn.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.removeBtn.setFont(font)
        self.removeBtn.setObjectName("removeBtn")
        self.horizontalLayout_5.addWidget(self.removeBtn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.detailLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.detailLabel.setMinimumSize(QtCore.QSize(351, 0))
        self.detailLabel.setMaximumSize(QtCore.QSize(351, 16777215))
        self.detailLabel.setWordWrap(True)
        self.detailLabel.setObjectName("detailLabel")
        self.gridLayout.addWidget(self.detailLabel, 1, 0, 1, 1)

        self.retranslateUi(ExecuteItemWidget)
        QtCore.QMetaObject.connectSlotsByName(ExecuteItemWidget)

    def retranslateUi(self, ExecuteItemWidget):
        _translate = QtCore.QCoreApplication.translate
        ExecuteItemWidget.setWindowTitle(_translate("ExecuteItemWidget", "Form"))
        self.nameLabel.setText(_translate("ExecuteItemWidget", "TextLabel"))
        self.editBtn.setText(_translate("ExecuteItemWidget", "编辑"))
        self.moveDownBtn.setText(_translate("ExecuteItemWidget", "下移"))
        self.moveUpBtn.setText(_translate("ExecuteItemWidget", "上移"))
        self.removeBtn.setText(_translate("ExecuteItemWidget", "移除"))
        self.detailLabel.setText(_translate("ExecuteItemWidget", "TextLabel"))

