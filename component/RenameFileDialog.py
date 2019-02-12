import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog

from ui.dialog.RenameFileDialog import Ui_RenameFileDialog

class RenameFileDialog(QtWidgets.QDialog, Ui_RenameFileDialog):

    def __init__(self,config, command = None):
        super(RenameFileDialog, self).__init__()
        self.setupUi(self)
        self.init_ui()
        self.config = config

        self.originPath = self.config["originPath"]
        self.renamePath = self.config["renamePath"]
        self.rename = self.config["rename"]
        if command:
            self.originPath = command['originPath']
            self.renamePath = command['renamePath']
            self.rename = command["rename"]
            if command['fileType'] == 2:
                self.dirRadio.setChecked(True)
        self.originEdit.setText(self.originPath)
        self.renameEdit.setText(self.rename)
        self.status = False

    def init_ui(self):
        self.setWindowTitle("重命名文件/文件夹")
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

    def get_data(self):
        fileType = 1
        if self.dirRadio.isChecked():
            fileType = 2
        origin = os.path.split(self.originEdit.text())
        renamePath = origin[0] + "/" + self.renameEdit.text()
        return self.status,fileType, self.originEdit.text(), renamePath, self.renameEdit.text()

    def on_confirm(self):
        if self.originEdit.text() != '' and self.renameEdit.text() != '':
            self.status = True
            self.close()
        else:
            QMessageBox.warning(self, '提示', '路径不能为空!')

