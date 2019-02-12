from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog

from ui.dialog.RemoveFileDialog import Ui_RemoveFileDialog

class RemoveFileDialog(QtWidgets.QDialog, Ui_RemoveFileDialog):

    def __init__(self,config, command = None):
        super(RemoveFileDialog, self).__init__()
        self.setupUi(self)
        self.init_ui()
        self.config = config

        self.originPath = self.config["originPath"]
        if command:
            self.originPath = command['originPath']
            if command['fileType'] == 2:
                self.dirRadio.setChecked(True)
        self.originEdit.setText(self.originPath)
        self.status = False

    def init_ui(self):
        self.setWindowTitle("移除文件/文件夹")
        self.originBtn.clicked.connect(self.on_open_origin)  # 打开源文件
        self.confirmBtn.clicked.connect(self.on_confirm)
        self.cancelBtn.clicked.connect(self.reject)


    # 打开源文件
    def on_open_origin(self):
        if self.fileRadio.isChecked():
            filename,_ = QtWidgets.QFileDialog.getOpenFileName(self,'请选择要移除的文件',self.originPath)
            if filename != '':
                self.originEdit.setText(filename)
        else:
            filename = QtWidgets.QFileDialog.getExistingDirectory(self, "请选择要移除的文件夹", self.originPath)
            if filename != '':
                self.originEdit.setText(filename)

    # # 打开目标目录
    # def on_open_dest(self):
    #     filename = QtWidgets.QFileDialog.getExistingDirectory(self, "请选择要统计的文件夹", self.destPath)
    #     if filename != '':
    #         self.destEdit.setText(filename)

    def get_data(self):
        fileType = 1
        if self.dirRadio.isChecked():
            fileType = 2
        return self.status,fileType, self.originEdit.text()

    def on_confirm(self):
        if self.originEdit.text() != '':
            self.status = True
            self.close()
        else:
            QMessageBox.warning(self, '提示', '路径不能为空!')
