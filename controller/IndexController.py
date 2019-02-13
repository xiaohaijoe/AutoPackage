import copy
import time

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QInputDialog, QLineEdit

from component import ExecuteItemWidget
from manager import CommandManager, ExecuteCommandManager
from ui.layout.index import Ui_indexWindow
from util import Constant, ScreenUtil


class IndexController(QtWidgets.QMainWindow, Ui_indexWindow):
    removeSignal = QtCore.pyqtSignal(int)                   # 移除item信号量
    moveUpSignal = QtCore.pyqtSignal(int)                   # 上移item信号量
    moveDownSignal = QtCore.pyqtSignal(int)                 # 下移item信号量
    editSignal = QtCore.pyqtSignal(int)                     # 编辑item信号量
    autoSaveSignal = QtCore.pyqtSignal()                    # 自动保存信号量
    currentExecuteUpdateSignal = QtCore.pyqtSignal(list)    # 更新新执行命令集信号量
    spinnerUpdateSignal = QtCore.pyqtSignal()               # 更新下拉选择框信号量
    executeProgressSignal = QtCore.pyqtSignal(object)           # 执行进度信号量

    def __init__(self):
        super(IndexController,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("智慧城交通事业部自动打包上传工具V1.0")
        self.commandManager = CommandManager()

        self.newExecuteListBtn.clicked.connect(self.on_new_execute_list)                        # 新建指令集按钮
        self.saveBtn.clicked.connect(self.on_execute_list_save)                                 # 保存按钮
        self.mergeSubmitBtn.clicked.connect(self.on_merge_execute)                              # 合并执行按钮
        self.singleSubmitBtn.clicked.connect(self.on_single_execute)                            # 逐条执行按钮
        self.continueBtn.clicked.connect(self.on_executing_continue)                            # 继续执行按钮
        self.stopBtn.clicked.connect(self.on_executing_stop)                                    # 停止执行按钮
        self.executeSavedSpinner.currentIndexChanged.connect(self.on_execute_save_selected)     # 已保存命令集

        self.init_ui()
        self.init_command_list_view(self.commandManager.commandList)                            # 初始化命令集
        self.init_execute_list_view(self.commandManager.currentExecuteList)                     # 初始化执行命令集
        self.init_save_execute_list_view(self.commandManager.executeSaveList)                   # 初始化保存命令集
        self.init_save_label_view(self.commandManager.executeSaveName)                          # 初始化执行命令集名称
        self.init_execute_progress_list_view()                                                  # 初始化执行进度集

    def init_ui(self):
        width, height = ScreenUtil.get_screen_size()
        self.resize(width*0.66, height*0.8)

    # 初始化保存命令集名称
    def init_save_label_view(self, name):
        if name == "":
            self.saveLabel.setText("未保存指令集")
        else:
            self.saveLabel.setText(name)

    # 初始化命令列表
    def init_command_list_view(self, list):
        commandListModel = QStringListModel()
        tempList = []
        for item in list:
            tempList.append(item['name'])
        commandListModel.setStringList(tempList)
        self.commandListView.setModel(commandListModel)
        self.commandListView.doubleClicked.connect(self.on_command_selected)

    # 初始化执行命令列表
    def init_execute_list_view(self, list):
        self.executeSignals = [
            self.removeSignal,
            self.moveUpSignal,
            self.moveDownSignal,
            self.editSignal,
            self.autoSaveSignal,
            self.currentExecuteUpdateSignal,
            self.spinnerUpdateSignal
        ]
        self.removeSignal.connect(self.on_execute_item_remove)
        self.moveUpSignal.connect(self.on_execute_item_move_up)
        self.moveDownSignal.connect(self.on_execute_item_move_down)
        self.editSignal.connect(self.on_execute_item_edit)
        self.autoSaveSignal.connect(self.on_execute_auto_save)
        self.currentExecuteUpdateSignal.connect(self.on_current_execute_update)
        self.spinnerUpdateSignal.connect(self.on_spinner_update)
        self.executeProgressSignal.connect(self.on_executing_progress)
        self.currentExecuteUpdateSignal.emit(list)

    # 初始化下拉选择框
    def init_save_execute_list_view(self, list):
        # 必须先解除信号量，否则调用clear会触发索引改变
        self.executeSavedSpinner.currentIndexChanged.disconnect()
        self.executeSavedSpinner.clear()
        self.executeSavedSpinner.addItem("请选择")
        for item in list:
            self.executeSavedSpinner.addItem(item["name"])
        self.executeSavedSpinner.currentIndexChanged.connect(self.on_execute_save_selected)

    def init_execute_progress_list_view(self):
        self.progressListModel = QStringListModel()
        self.progressListModel.setStringList([])
        self.progressListView.setModel(self.progressListModel)

    def on_merge_execute(self):
        self.execute(False)
        pass

    def on_single_execute(self):
        self.execute(True)

    # isSingleExecute: False | 合并执行
    # isSingleExecute: True | 逐条执行
    def execute(self, isSingleExecute=False):
        self.progressListModel.setStringList([])
        self.executeCommandManager = ExecuteCommandManager()
        self.executeCommandManager.do_execute(self.commandManager.currentExecuteList, isSingleExecute)
        self.executeCommandManager.set_executing_progress_signal(self.executeProgressSignal)

    # 执行进度
    def on_executing_progress(self, progress):
        status = progress["status"]
        id = self.progressListModel.rowCount()
        self.progressListModel.insertRow(id)
        self.progressListModel.setData(self.progressListModel.index(id), progress["message"])
        self.progressListView.scrollToBottom()

        if status == Constant.EXECUTING_STATUS_START:
            self.reset_executing_start(progress["isSingleExecute"])
        elif status == Constant.EXECUTING_STATUS_PAUSE:
            pass
        elif status == Constant.EXECUTING_STATUS_RESUME:
            pass
        elif status == Constant.EXECUTING_STATUS_COMPLETE:
            self.reset_executing_complete()
        else:
            pass

    def reset_executing_start(self, isSingleExecute):
        if isSingleExecute:
            self.continueBtn.setEnabled(True)
            self.stopBtn.setEnabled(True)
        else:
            self.continueBtn.setEnabled(False)
            self.stopBtn.setEnabled(False)
        self.mergeSubmitBtn.setEnabled(False)
        self.singleSubmitBtn.setEnabled(False)


    # 执行完成，重置按钮
    def reset_executing_complete(self):
        self.continueBtn.setEnabled(False)
        self.stopBtn.setEnabled(False)
        self.mergeSubmitBtn.setEnabled(True)
        self.singleSubmitBtn.setEnabled(True)

    def on_executing_continue(self):
        self.executeCommandManager.resume()

    def on_executing_stop(self):
        self.executeCommandManager.stop()

    # 选中下拉选项框
    def on_execute_save_selected(self, index):
        if index >= 1:
            _, list = self.commandManager.on_execute_save_selected(index-1)
            self.currentExecuteUpdateSignal.emit(list)

    # 选中了指定命令
    def on_command_selected(self, qModelIndex):
        selectedItem = self.commandManager.commandList[qModelIndex.row()]
        item = copy.copy(selectedItem)
        list = self.commandManager.add_execute(item)
        # 更新当前命令集
        self.currentExecuteUpdateSignal.emit(list)

    # 重置执行列表
    def reset_execute_list_view(self, list):
        self.executeListWidget.clear()
        for i in range(len(list)):
            myQCustomQWidget = ExecuteItemWidget(list,i,self.executeSignals)
            myQListWidgetItem = QtWidgets.QListWidgetItem(self.executeListWidget)
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            self.executeListWidget.addItem(myQListWidgetItem)
            self.executeListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
        self.autoSaveSignal.emit()

    # 执行列表item移除
    def on_execute_item_remove(self, index):
        del self.commandManager.currentExecuteList[index]
        # 更新当前命令集
        self.currentExecuteUpdateSignal.emit(self.commandManager.currentExecuteList)
        self.autoSaveSignal.emit()

    # 执行列表item上移
    def on_execute_item_move_up(self, index):
        if index > 0:
            item = self.commandManager.currentExecuteList[index]
            del self.commandManager.currentExecuteList[index]
            self.commandManager.currentExecuteList.insert(index-1,item)
            self.currentExecuteUpdateSignal.emit(self.commandManager.currentExecuteList)
            self.autoSaveSignal.emit()

    # 执行列表item下移
    def on_execute_item_move_down(self, index):
        if index < len(self.commandManager.currentExecuteList)-1:
            item = self.commandManager.currentExecuteList[index]
            del self.commandManager.currentExecuteList[index]
            self.commandManager.currentExecuteList.insert(index+1,item)
            self.currentExecuteUpdateSignal.emit(self.commandManager.currentExecuteList)
            self.autoSaveSignal.emit()

    # 执行列表item编辑
    def on_execute_item_edit(self, index):
        list = self.commandManager.on_execute_item_edit(index)
        self.currentExecuteUpdateSignal.emit(list)
        self.autoSaveSignal.emit()

    # 清空(新建)命令
    def on_new_execute_list(self):
        list = self.commandManager.clear_execute_list()
        self.currentExecuteUpdateSignal.emit(list)
        self.autoSaveSignal.emit()

    # 点击保存按钮
    def on_execute_list_save(self):
        if self.commandManager.executeSaveName == "":
            name, okPressed = QInputDialog.getText(self, "保存命令", "请输入保存的列表名称", QLineEdit.Normal, "")
            if okPressed and name != '':
                self.commandManager.save_execute_list_by_name(name)
        else:
            self.commandManager.save_execute_list_by_name(self.commandManager.executeSaveName)
        # 更新当前命令集
        self.currentExecuteUpdateSignal.emit(self.commandManager.currentExecuteList)
        # 更新下拉选择框
        self.spinnerUpdateSignal.emit()

    # 自动保存，通过self.autoSaveSignal.emit()信号量触发
    def on_execute_auto_save(self):
        self.commandManager.auto_save_current_execute_list()

    # 更新新执行命令集,通过self.currentExecuteUpdateSignal.emit()触发
    def on_current_execute_update(self, list):
        self.reset_execute_list_view(list)
        self.init_save_label_view(self.commandManager.executeSaveName)

    # 更新下拉选择框,通过self.spinnerUpdateSignal.emit()触发
    def on_spinner_update(self):
        self.init_save_execute_list_view(self.commandManager.executeSaveList)

