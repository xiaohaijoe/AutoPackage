import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog

from ui.dialog.CopyFileToPathDialog import Ui_CopyFileToPathDialog
from util import ScreenUtil


class CopyFileToPathDialog(QtWidgets.QDialog, Ui_CopyFileToPathDialog):

    def __init__(self,config, command = None):
        super(CopyFileToPathDialog, self).__init__()
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
        self.setWindowTitle("复制文件到文件夹")
        self.originBtn.clicked.connect(self.on_open_origin)  # 打开源文件
        self.destBtn.clicked.connect(self.on_open_dest)  # 打开源文件
        self.confirmBtn.clicked.connect(self.on_confirm)
        self.cancelBtn.clicked.connect(self.reject)

        width, height = ScreenUtil.get_screen_size()
        self.resize(width*0.5, self.height())

    # 打开源文件
    def on_open_origin(self):
        filename,_ = QtWidgets.QFileDialog.getOpenFileName(self,'请选择要上传的文件',self.originPath)
        if filename != '':
            self.set_full_dest_path(filename,self.destEdit.text())
            self.originEdit.setText(filename)

    # 打开目标目录
    def on_open_dest(self):
        filename = QtWidgets.QFileDialog.getExistingDirectory(self, "请选择要统计的文件夹", self.destPath)
        if filename != '':
            self.set_full_dest_path(self.originEdit.text(), filename)

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
        if ext[1] == "":
            # 如果没有扩展名，则认为是文件夹
            if dest[1] == "":
                # 没有"/"后缀
                destPath = dest[0] + "/" + origin[1]
            else:
                # 有"/"后缀
                destPath = ext[0] + "/" + origin[1]
        else:
            # 如果有扩展名，则认为是文件
            destPath = dest[0] + "/" + origin[1]
        self.destEdit.setText(destPath)
