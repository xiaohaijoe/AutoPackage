# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_indexWindow(object):
    def setupUi(self, indexWindow):
        indexWindow.setObjectName("indexWindow")
        indexWindow.resize(1330, 828)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(indexWindow.sizePolicy().hasHeightForWidth())
        indexWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(indexWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.mergeSubmitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.mergeSubmitBtn.setGeometry(QtCore.QRect(1210, 730, 101, 41))
        self.mergeSubmitBtn.setObjectName("mergeSubmitBtn")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 10, 1281, 421))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.saveLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.saveLabel.setObjectName("saveLabel")
        self.horizontalLayout_5.addWidget(self.saveLabel)
        self.newExecuteListBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.newExecuteListBtn.setObjectName("newExecuteListBtn")
        self.horizontalLayout_5.addWidget(self.newExecuteListBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.executeListWidget = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.executeListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.executeListWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.executeListWidget.setObjectName("executeListWidget")
        self.gridLayout_2.addWidget(self.executeListWidget, 1, 2, 1, 1)
        self.commandListView = QtWidgets.QListView(self.gridLayoutWidget_2)
        self.commandListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.commandListView.setObjectName("commandListView")
        self.gridLayout_2.addWidget(self.commandListView, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.executeSavedSpinner = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.executeSavedSpinner.sizePolicy().hasHeightForWidth())
        self.executeSavedSpinner.setSizePolicy(sizePolicy)
        self.executeSavedSpinner.setObjectName("executeSavedSpinner")
        self.horizontalLayout_4.addWidget(self.executeSavedSpinner)
        self.saveBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveBtn.sizePolicy().hasHeightForWidth())
        self.saveBtn.setSizePolicy(sizePolicy)
        self.saveBtn.setObjectName("saveBtn")
        self.horizontalLayout_4.addWidget(self.saveBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 2, 1, 1)
        self.progressListView = QtWidgets.QListView(self.centralwidget)
        self.progressListView.setGeometry(QtCore.QRect(30, 450, 1281, 261))
        self.progressListView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.progressListView.setObjectName("progressListView")
        self.singleSubmitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.singleSubmitBtn.setGeometry(QtCore.QRect(30, 730, 101, 41))
        self.singleSubmitBtn.setObjectName("singleSubmitBtn")
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setEnabled(False)
        self.stopBtn.setGeometry(QtCore.QRect(220, 730, 91, 41))
        self.stopBtn.setObjectName("stopBtn")
        self.continueBtn = QtWidgets.QPushButton(self.centralwidget)
        self.continueBtn.setEnabled(False)
        self.continueBtn.setGeometry(QtCore.QRect(130, 730, 91, 41))
        self.continueBtn.setObjectName("continueBtn")
        indexWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(indexWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1330, 22))
        self.menubar.setObjectName("menubar")
        indexWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(indexWindow)
        self.statusbar.setObjectName("statusbar")
        indexWindow.setStatusBar(self.statusbar)

        self.retranslateUi(indexWindow)
        QtCore.QMetaObject.connectSlotsByName(indexWindow)

    def retranslateUi(self, indexWindow):
        _translate = QtCore.QCoreApplication.translate
        indexWindow.setWindowTitle(_translate("indexWindow", "MainWindow"))
        self.mergeSubmitBtn.setText(_translate("indexWindow", "合并执行"))
        self.saveLabel.setText(_translate("indexWindow", "未保存指令集"))
        self.newExecuteListBtn.setText(_translate("indexWindow", "新建指令"))
        self.label.setText(_translate("indexWindow", ">>"))
        self.label_4.setText(_translate("indexWindow", "选择指令"))
        self.label_2.setText(_translate("indexWindow", "备注：可通过根目录下config.json文件进行指令的直接修改"))
        self.label_3.setText(_translate("indexWindow", "最近保存"))
        self.saveBtn.setText(_translate("indexWindow", "保存"))
        self.singleSubmitBtn.setText(_translate("indexWindow", "逐条执行"))
        self.stopBtn.setText(_translate("indexWindow", "停止"))
        self.continueBtn.setText(_translate("indexWindow", "继续"))

