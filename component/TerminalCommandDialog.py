from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog

from ui.dialog.TerminalCommandDialog import Ui_TernimalCommandDialog

class TerminalCommandDialog(QtWidgets.QDialog, Ui_TernimalCommandDialog):

    def __init__(self,config, command = None):
        super(TerminalCommandDialog, self).__init__()
        self.setupUi(self)
        self.init_ui()
        self.config = config

        self.terminalCommand = self.config["terminalCommand"]
        if command:
            self.terminalCommand = command['terminalCommand']
        self.terminalCommandEdit.setText(self.terminalCommand)
        self.status = False

    def init_ui(self):
        self.setWindowTitle("执行终端命令")
        self.confirmBtn.clicked.connect(self.on_confirm)
        self.cancelBtn.clicked.connect(self.reject)

    def get_data(self):
        return self.status, self.terminalCommandEdit.text()

    def on_confirm(self):
        if self.terminalCommandEdit.text() != '':
            self.status = True
            self.close()
        else:
            QMessageBox.warning(self, '提示', '命令不能为空!')
