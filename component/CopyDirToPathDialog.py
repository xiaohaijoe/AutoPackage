import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog

from ui.dialog.CopyDirToPathDialog import Ui_CopyDirToPathDialog

class CopyDirToPathDialog(QtWidgets.QDialog, Ui_CopyDirToPathDialog):

    def __init__(self,config, command = None):
        super(CopyDirToPathDialog, self).__init__()
        self.setupUi(self)
        self.init_ui()
        self.config = config

        self.originPath = self.config["originPath"]
        self.destPath = self.config["destPath"]
        if command:
            self.originPath = command['originPath']
            self.destPath = command['destPath']
        self.originEdit.setText(self.originPath)
        self.destEdit.setText(self.destPath)
        self.status = False


    def init_ui(self):
        self.setWindowTitle("复制文件夹到文件夹")
        self.originBtn.clicked.connect(self.on_open_origin)  # 打开源文件
        self.destBtn.clicked.connect(self.on_open_dest)  # 打开源文件
        self.confirmBtn.clicked.connect(self.on_confirm)
        self.cancelBtn.clicked.connect(self.reject)


    # 打开源文件
    def on_open_origin(self):
        filename = QtWidgets.QFileDialog.getExistingDirectory(self, "请选择要复制的文件夹", self.destPath)
        if filename != '':
            self.set_full_dest_path(filename, self.destEdit.text())
            self.originEdit.setText(filename)

    # 打开目标目录
    def on_open_dest(self):
        filename = QtWidgets.QFileDialog.getExistingDirectory(self, "请选择要目标的文件夹", self.destPath)
        if filename != '':
            self.set_full_dest_path(self.originEdit.text(), filename)
            # self.destEdit.setText(filename)

    def get_data(self):
        return self.status, self.originEdit.text(), self.destEdit.text()

    def on_confirm(self):
        if self.originEdit.text() != '' and self.destEdit.text() != '':
            self.status = True
            self.close()
        else:
            QMessageBox.warning(self, '提示', '路径不能为空!')

    # 设置完整路径
    def set_full_dest_path(self, originPath, destPath):
        origin = os.path.split(originPath)
        dest = os.path.split(destPath)
        ext = os.path.splitext(destPath)
        if dest[1] == "":
            destPath = dest[0] + "/"  + origin[1]
        else:
            destPath = dest[0] + "/" + dest[1] + "/" + origin[1]
        self.destEdit.setText(destPath)