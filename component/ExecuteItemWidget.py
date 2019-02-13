
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from ui.widget.ExecuteItemWidget import Ui_ExecuteItemWidget
class ExecuteItemWidget(QtWidgets.QWidget,Ui_ExecuteItemWidget):

    def __init__(self, list, index, executeSignals):
        super(ExecuteItemWidget, self).__init__()
        self.setupUi(self)

        self.item = list[index]
        self.index = index
        self.nameLabel.setText(str(self.index+1)+". "+self.item['name'])
        self.detailLabel.setText(self.item['detail'])
        # s = self.item['detail']
        # s = str(s).replace('\n', '<br>')
        # self.detailLabel.setText('<div style="line-height:30px;font-size:20px;">'+ s + '</div>')

        self.setLayout(self.gridLayout)
        self.removeBtn.clicked.connect(self.on_remove)
        self.editBtn.clicked.connect(self.on_edit)
        self.moveUpBtn.clicked.connect(self.on_move_up)
        self.moveDownBtn.clicked.connect(self.on_move_down)
        self.executeSignals = executeSignals

    def on_remove(self):
        button = QMessageBox.question(self, "提示", "是否移除该命令？",
                                      QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
        if button == QMessageBox.Ok:
            self.executeSignals[0].emit(self.index)
        else:
            pass

    def on_edit(self):
        self.executeSignals[3].emit(self.index)
        pass

    def on_move_up(self):
        self.executeSignals[1].emit(self.index)
        pass

    def on_move_down(self):
        self.executeSignals[2].emit(self.index)
        pass