import json

from component import CopyFileToPathDialog, CopyDirToPathDialog, RemoveFileDialog, RenameFileDialog, \
    MergeFilesAndZipDialog, OpenTerminalDialog, TerminalCommandDialog
from util.Constant import Constant


class CommandManager:
    def __init__(self):
        self.commandList = Constant.COMMAND_LIST
        self.config = self.load_config_file()
        self.history = []
        self.currentExecuteList = []
        self.executeSaveName = ""
        self.executeSaveList = []
        if "executeSaveList" in self.config:
            self.executeSaveList = self.config["executeSaveList"]
        if "history" in self.config:
            self.history = self.config["history"]
        if "currentExecuteList" in self.config:
            self.currentExecuteList = self.config["currentExecuteList"]
        if "executeSaveName" in self.config:
            self.executeSaveName = self.config["executeSaveName"]

    # 读取指令文件
    # def load_command_file(self):
        # config_file = "./command.json"
        # fo = open(config_file, 'r', encoding='utf-8')
        # return json.load(fo)

    # 读取指令文件
    def load_config_file(self):
        config_file = "./config.json"
        fo = open(config_file, 'r', encoding='utf-8')
        return json.load(fo)

    # 保存指令集
    def save_execute_list_by_name(self, name):
        config_file = "./config.json"
        item = {
            "name": name,
            "list": self.currentExecuteList
        }
        # 判断是否有重复命名
        existIndex = None
        for i in range(len(self.executeSaveList)):
            a = self.executeSaveList[i]
            if a["name"] == item["name"]:
                existIndex = i
                break
        if existIndex != None:
            del self.executeSaveList[existIndex]
        self.executeSaveList.insert(0, item)
        self.executeSaveList = self.executeSaveList[:10]
        self.executeSaveName = name
        self.config["executeSaveList"] = self.executeSaveList
        self.config["executeSaveName"] = name
        fo = open(config_file, 'w', encoding='utf-8')
        print(json.dumps(self.config), file=fo)

    # 自动保存当前指令集
    def auto_save_current_execute_list(self):
        config_file = "./config.json"
        self.config["currentExecuteList"] = self.currentExecuteList
        self.config["executeSaveName"] = self.executeSaveName
        fo = open(config_file, 'w', encoding='utf-8')
        print(json.dumps(self.config), file=fo)

    def handle_execute(self, command, edit=False):
        c = command['command']
        status = False
        if c == Constant.COMM_COPY_FILE_TO_DIR:
            status = self.on_copy_file_to_dir(command, edit)
        elif c == Constant.COMM_COPY_DIR_TO_DIR:
            status = self.on_copy_dir_to_dir(command, edit)
        elif c == Constant.COMM_REMOVE_FILE:
            status = self.on_remove_file(command, edit)
        elif c == Constant.COMM_RENAME_FILE:
            status = self.on_rename_file(command, edit)
        elif c == Constant.COMM_MERGE_FILES_AND_ZIP_TO_DEST_DIR:
            status = self.on_merge_files_and_zip(command, edit)
        elif c == Constant.COMM_OPEN_TERMINAL_TO_DEST_PATH:
            status = self.on_open_terminal_by_dest_path(command, edit)
        elif c == Constant.COMM_EXECUTE_TERMINAL_COMMAND:
            status = self.on_execute_terminal_command(command, edit)
        return status, command

    # 添加命令
    def add_execute(self, command):
        status, command = self.handle_execute(command)
        if status:
            self.currentExecuteList.append(command)
        return self.currentExecuteList

    # 清空命令
    def clear_execute_list(self):
        self.currentExecuteList = []
        self.executeSaveName = ""
        return self.currentExecuteList

    # 切换指令集
    def on_execute_save_selected(self, index):
        item = self.executeSaveList[index]
        self.executeSaveName = item["name"]
        self.currentExecuteList = item["list"]
        return self.executeSaveName, self.currentExecuteList

    # 编辑命令
    def on_execute_item_edit(self, index):
        command = self.currentExecuteList[index]
        status, command = self.handle_execute(command, True)
        if status:
            self.currentExecuteList[index] = command
        return self.currentExecuteList

    # 打开复制文件到文件夹对话框
    def on_copy_file_to_dir(self, command, edit=False):
        c = None
        if edit:
            c = command
        v = CopyFileToPathDialog(self.get_default_config_by_command(command), c)  # 建立对话框实例
        v.exec_()
        if v.close():
            status, originPath, destPath = v.get_data()
            if status:
                command["originPath"] = originPath
                command["destPath"] = destPath
                command["detail"] = '文件：' + originPath + '\n复制到：' + destPath
            return status
        return False

    # 打开复制文件夹到文件夹对话框
    def on_copy_dir_to_dir(self, command, edit=False):
        c = None
        if edit:
            c = command
        v = CopyDirToPathDialog(self.get_default_config_by_command(command), c)  # 建立对话框实例
        v.exec_()
        if v.close():
            status, originPath, destPath = v.get_data()
            if status:
                command["originPath"] = originPath
                command["destPath"] = destPath
                command["detail"] = '文件夹：' + originPath + '\n复制到"' + destPath
            return status
        return False

    # 移除文件/文件夹
    def on_remove_file(self, command, edit=False):
        c = None
        if edit:
            c = command
        v = RemoveFileDialog(self.get_default_config_by_command(command), c)  # 建立对话框实例
        v.exec_()
        if v.close():
            status, fileType, originPath = v.get_data()
            if status:
                command["fileType"] = fileType
                command["originPath"] = originPath
                command["detail"] = '移除文件/文件夹：' + originPath
            return status
        return False

    # 重命名文件/文件夹
    def on_rename_file(self, command, edit=False):
        c = None
        if edit:
            c = command
        v = RenameFileDialog(self.get_default_config_by_command(command), c)  # 建立对话框实例
        v.exec_()
        if v.close():
            status, fileType, originPath, renamePath, rename = v.get_data()
            if status:
                command["fileType"] = fileType
                command["originPath"] = originPath
                command["renamePath"] = renamePath
                command["rename"] = rename
                command["detail"] = '文件/文件夹：' + originPath + "\n重命名为：" + renamePath
            return status
        return False

    # 合并文件并压缩到指定文件
    def on_merge_files_and_zip(self, command, edit=False):
        c = None
        if edit:
            c = command
        v = MergeFilesAndZipDialog(self.get_default_config_by_command(command), c)  # 建立对话框实例
        v.exec_()
        if v.close():
            status, filesPath, zipPath, lastPath = v.get_data()
            if status:
                command["filesPath"] = filesPath
                command["zipPath"] = zipPath
                command["lastPath"] = lastPath
                detail = "源文件路径：\n"
                for path in filesPath:
                    detail += path + "\n"
                detail += "压缩到：" + zipPath
                command["detail"] = detail
            return status
        return False

    # 在指定目录打开终端
    def on_open_terminal_by_dest_path(self, command, edit=False):
        c = None
        if edit:
            c = command
        v = OpenTerminalDialog(self.get_default_config_by_command(command), c)  # 建立对话框实例
        v.exec_()
        if v.close():
            status, destPath = v.get_data()
            if status:
                command["destPath"] = destPath
                command["detail"] = "终端路径：" + destPath
            return status
        return False

    # 执行终端命令
    def on_execute_terminal_command(self, command, edit=False):
        c = None
        if edit:
            c = command
        v = TerminalCommandDialog(self.get_default_config_by_command(command), c)  # 建立对话框实例
        v.exec_()
        if v.close():
            status, terminalCommand = v.get_data()
            if status:
                command["terminalCommand"] = terminalCommand
                command["detail"] = "执行终端命令：" + terminalCommand
            return status
        return False

    # 获取默认配置
    def get_default_config_by_command(self, command):
        c = command['command']
        if c in self.history:
            return self.history[c]

        if c == Constant.COMM_COPY_FILE_TO_DIR:
            return {
                "originPath": "",
                "destPath": "./"
            }
        elif c == Constant.COMM_COPY_DIR_TO_DIR:
            return {
                "originPath": "./",
                "destPath": "./"
            }
        elif c == Constant.COMM_REMOVE_FILE:
            return {
                "fileType": 1,
                "originPath": ""
            }
        elif c == Constant.COMM_RENAME_FILE:
            return {
                "fileType": 1,
                "originPath": "",
                "renamePath": "",
                "rename": ""
            }
        elif c == Constant.COMM_MERGE_FILES_AND_ZIP_TO_DEST_DIR:
            return {
                "lastPath": "./",
                "filesPath": [],
                "zipPath": ""
            }
        elif c == Constant.COMM_OPEN_TERMINAL_TO_DEST_PATH:
            return {
                "destPath": "./"
            }
        elif c == Constant.COMM_EXECUTE_TERMINAL_COMMAND:
            return {
                "terminalCommand": ""
            }
