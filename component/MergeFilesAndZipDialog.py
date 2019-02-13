import datetime

from PyQt5 import QtWidgets
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QMessageBox, QDialog
import time

from ui.dialog.MergeFilesAndZipDialog import Ui_MergeFilesAndZipDialog
from util import ScreenUtil


class MergeFilesAndZipDialog(QtWidgets.QDialog, Ui_MergeFilesAndZipDialog):

    def __init__(self,config, command = None):
        super(MergeFilesAndZipDialog, self).__init__()
        self.setupUi(self)
        self.init_ui()
        self.config = config

        self.lastPath = self.config["lastPath"]
        self.zipPath = self.config["zipPath"]
        self.filesPath = []
        if command:
            self.lastPath = command["lastPath"]
            self.filesPath = command["filesPath"]
            self.zipPath = command["zipPath"]
        self.zipEdit.setText(self.zipPath)
        self.status = False

        self.init_data()

    def init_ui(self):
        self.setWindowTitle("合并文件并压缩到指定文件")
        self.originBtn.clicked.connect(self.on_open_origin)  # 打开源文件
        self.zipBtn.clicked.connect(self.on_open_zip)  # 打开源文件
        self.confirmBtn.clicked.connect(self.on_confirm)
        self.cancelBtn.clicked.connect(self.reject)
        self.listView.clicked.connect(self.on_remove_path)

        width, height = ScreenUtil.get_screen_size()
        self.resize(width*0.5, height*0.5)

    def init_data(self):
        self.init_list_view(self.filesPath)

    # 打开源文件
    def on_open_origin(self):
        if self.fileRadio.isChecked():
            filename,_ = QtWidgets.QFileDialog.getOpenFileName(self,'请选择要移除的文件',self.lastPath)
        else:
            filename = QtWidgets.QFileDialog.getExistingDirectory(self, "请选择要移除的文件夹", self.lastPath)
        if filename != "":
            self.lastPath = filename
            self.filesPath.append(filename)
            self.init_list_view(self.filesPath)

    # 打开压缩文件
    def on_open_zip(self):
        filename = QtWidgets.QFileDialog.getExistingDirectory(self, "请选择要移除的文件夹", self.zipPath)
        if filename != "":
            filename = filename + "/" + str(int(time.time())) + ".zip"
            self.zipEdit.setText(filename)


    def init_list_view(self, list):
        listModel = QStringListModel()
        listModel.setStringList(list)
        self.listView.setModel(listModel)

    def on_remove_path(self, QModelIndex):
        if QModelIndex.row() > -1:
            button = QMessageBox.question(self, "提示", "是否删除该路径？",
                                          QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
            if button == QMessageBox.Ok:
                del self.filesPath[QModelIndex.row()]
                self.init_list_view(self.filesPath)
            else:
                pass

    def get_data(self):
        return self.status, self.filesPath, self.zipEdit.text(), self.lastPath

    def on_confirm(self):
        if len(self.filesPath) == 0:
            QMessageBox.warning(self, '提示', '路径不能为空!')
        elif self.zipEdit.text() == '':
            QMessageBox.warning(self, '提示', '压缩路径不能为空!')
        else:
            self.status = True
            self.close()