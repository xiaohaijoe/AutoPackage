import json

import _thread
import os
import time

from util import FileUtil, Constant, ProcessInstance


class ExecuteCommandManager:

    def __init__(self):
        self.isPause = False
        self.isStop = False
        pass

    def do_execute(self, executeList, isSingleExecute):
        if isSingleExecute:
            self.isPause = True
            self.isStop = False
        _thread.start_new_thread(self.on_do_execute, (executeList, isSingleExecute))

    def on_do_execute(self, executeList, isSingleExecute):
        self.executingProgressSignal.emit({
            "status" : Constant.EXECUTING_STATUS_START,
            "success" : True,
            "isSingleExecute": isSingleExecute,
            "message" : "开始执行..."
        })
        for i in range(len(executeList)):
            item = executeList[i]
            c = item["command"]
            result = None
            self.executingProgressSignal.emit({
                "status": Constant.EXECUTING_STATUS_PROGRESS,
                "success": True,
                "message": str(i + 1) + ". " + item["detail"]
            })
            if isSingleExecute:
                # 发送暂停信号
                self.executingProgressSignal.emit({
                    "status": Constant.EXECUTING_STATUS_PAUSE,
                    "success": True,
                    "message": "等待执行..."
                })
                while self.isPause:
                    time.sleep(1)
                self.isPause = True
                if self.isStop:
                    self.executingProgressSignal.emit({
                        "status": Constant.EXECUTING_STATUS_COMPLETE,
                        "success": True,
                        "message": "已停止！"
                    })
                    return
                else:
                    self.executingProgressSignal.emit({
                        "status": Constant.EXECUTING_STATUS_RESUME,
                        "success": True,
                        "message": "继续执行..."
                    })
            if c == Constant.COMM_COPY_FILE_TO_DIR:
                result = self.on_copy_file_to_dir(item)
            elif c == Constant.COMM_COPY_DIR_TO_DIR:
                result = self.on_copy_dir_to_dir(item)
            elif c == Constant.COMM_REMOVE_FILE:
                result = self.on_remove_file(item)
            elif c == Constant.COMM_RENAME_FILE:
                result = self.on_rename_file(item)
            elif c == Constant.COMM_MERGE_FILES_AND_ZIP_TO_DEST_DIR:
                result = self.on_merge_files_and_zip(item)
            elif c == Constant.COMM_OPEN_TERMINAL_TO_DEST_PATH:
                result = self.on_open_terminal_by_dest_path(item)
            elif c == Constant.COMM_EXECUTE_TERMINAL_COMMAND:
                result = self.on_execute_terminal_command(item)
            result["status"] = Constant.EXECUTING_STATUS_PROGRESS
            self.executingProgressSignal.emit(result)
            if not result["success"]:
                self.executingProgressSignal.emit({
                    "status" : Constant.EXECUTING_STATUS_COMPLETE,
                    "success": False,
                    "message": "失败！"
                })
                return
        self.executingProgressSignal.emit({
            "status": Constant.EXECUTING_STATUS_COMPLETE,
            "success": True,
            "message": "全部命令已执行完毕！"
        })


    def on_copy_file_to_dir(self, command):
        originPath = command["originPath"]
        destPath = command["destPath"]
        success = True
        message = "成功！"
        try:
            # 判断文件是否存在
            FileUtil.validate_file_exists(originPath)
            # 判断文件夹是否存在
            FileUtil.validate_folder_exists(os.path.dirname(destPath), True)
            # 复制文件到指定目录
            FileUtil.copy_file(originPath, destPath)
        except Exception as e:
            success = False
            message = str(e)
        finally:
            return {
                "success": success,
                "message": message
            }

    # 复制文件夹下的所有内容到指定文件夹下
    def on_copy_dir_to_dir(self, command):
        originPath = command["originPath"]
        destPath = command["destPath"]
        success = True
        message = "成功！"
        try:
            # 判断源文件夹是否存在
            FileUtil.validate_folder_exists(originPath, False)
            # 复制文件到指定目录
            FileUtil.copy_folder(originPath, destPath)
        except Exception as e:
            success = False
            message = str(e)
        finally:
            return {
                "success": success,
                "message": message
            }

    # 移除文件
    def on_remove_file(self, command):
        originPath = command["originPath"]
        success = True
        message = "成功！"
        try:
            # 复制文件到指定目录
            FileUtil.remove_file(originPath)
        except Exception as e:
            success = False
            message = str(e)
        finally:
            return {
                "success": success,
                "message": message
            }

    # 重命名文件
    def on_rename_file(self, command):
        originPath = command["originPath"]
        renamePath = command["renamePath"]
        success = True
        message = "成功！"
        try:
            # 复制文件到指定目录
            FileUtil.rename_file(originPath, renamePath)
        except Exception as e:
            success = False
            message = str(e)
        finally:
            return {
                "success": success,
                "message": message
            }

    def on_merge_files_and_zip(self, command):
        files = command["filesPath"]
        zipPath = command["zipPath"]
        success = True
        message = "成功！"
        try:
            # 在zipPath所在目录下，创建临时文件夹
            dir = os.path.split(zipPath)[0]
            dir = dir+"/"+str(int(time.time()))
            FileUtil.validate_folder_exists(dir, True)
            # 把源文件列表复制到临时文件下
            for file in files:
                dst = dir + "/" + os.path.split(file)[1]
                if os.path.isfile(file):
                    FileUtil.copy_file(file, dst)
                else:
                    FileUtil.copy_folder(file, dst)
            # 压缩文件夹
            FileUtil.zip_dir(dir, zipPath)
            # 删除文件夹
            FileUtil.remove_file(dir)
        except Exception as e:
            success = False
            message = str(e)
        finally:
            return {
                "success": success,
                "message": message
            }

    def on_open_terminal_by_dest_path(self, command):
        destPath = command["destPath"]
        success = True
        message = "成功！"
        try:
            # 在zipPath所在目录下，创建临时文件夹
            instance = ProcessInstance()
            instance.setCwd(destPath)
        except Exception as e:
            success = False
            message = str(e)
        finally:
            return {
                "success": success,
                "message": message
            }

    def on_execute_terminal_command(self, command):
        terminalCommand = command["terminalCommand"]
        success = True
        message = "成功！"
        try:
            # 在zipPath所在目录下，创建临时文件夹
            instance = ProcessInstance()
            success, message = instance.run(terminalCommand)
        except Exception as e:
            success = False
            message = str(e)
        finally:
            return {
                "success": success,
                "message": message
            }

    def set_executing_progress_signal(self, signal):
        self.executingProgressSignal = signal

    def resume(self):
        self.isPause = False

    def stop(self):
        self.isPause = False
        self.isStop = True