from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog

from ui.dialog.OpenTerminalDialog import Ui_OpenTerminalDialog

class OpenTerminalDialog(QtWidgets.QDialog, Ui_OpenTerminalDialog):

    def __init__(self,config, command = None):
        super(OpenTerminalDialog, self).__init__()
        self.setupUi(self)
        self.init_ui()
        self.config = config

        self.destPath = self.config["destPath"]
        if command:
            self.destPath = command['destPath']
        self.destEdit.setText(self.destPath)
        self.status = False

    def init_ui(self):
        self.setWindowTitle("在指定目录打开终端")
        self.destBtn.clicked.connect(self.on_open_dest)  # 打开源文件
        self.confirmBtn.clicked.connect(self.on_confirm)
        self.cancelBtn.clicked.connect(self.reject)


    # 打开源文件
    def on_open_dest(self):
        filename = QtWidgets.QFileDialog.getExistingDirectory(self, "请选择要移除的文件夹", self.destPath)
        if filename != '':
            self.destEdit.setText(filename)

    def get_data(self):
        return self.status, self.destEdit.text()

    def on_confirm(self):
        if self.destEdit.text() != '':
            self.status = True
            self.close()
        else:
            QMessageBox.warning(self, '提示', '路径不能为空!')
