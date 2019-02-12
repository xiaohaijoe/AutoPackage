class Constant:
    # class ConstError(PermissionError):pass
    # def __setattr__(self, name, value):
    #     if name in self.__dict__.keys():
    #         raise self.ConstError("Can't rebind const(%s)" % name)
    #     self.__dict__[name]=value
    #
    # def __delattr__(self, name):
    #     if name in self.__dict__:
    #         raise  self.ConstError("Can't unbind const(%s)" % name)
    #     raise  NameError(name)
    COMM_COPY_FILE_TO_DIR                = "copy_file_to_dir"
    COMM_COPY_DIR_TO_DIR                 = "copy_dir_to_dir"
    COMM_REMOVE_FILE                     = "remove_file"
    COMM_RENAME_FILE                     = "rename_file"
    COMM_MERGE_FILES_AND_ZIP_TO_DEST_DIR = "merge_files_and_zip_to_dest_dir"
    COMM_OPEN_TERMINAL_TO_DEST_PATH      = "open_terminal_to_dest_path"
    COMM_EXECUTE_TERMINAL_COMMAND        = "execute_terminal_command"

    COMMAND_LIST = [
      {
        "command": "copy_file_to_dir",
        "name": "复制文件到文件夹"
      },
      {
        "command": "copy_dir_to_dir",
        "name": "复制文件夹下所有文件到指定文件夹下"
      },
      {
        "command": "remove_file",
        "name": "移除文件/文件夹"
      },
      {
        "command": "rename_file",
        "name": "重命名文件/文件夹"
      },
      {
        "command": "merge_files_and_zip_to_dest_dir",
        "name": "合并文件并压缩到指定文件"
      },
      {
        "command": "open_terminal_to_dest_path",
        "name": "在指定目录打开终端"
      },
      {
        "command": "execute_terminal_command",
        "name": "执行终端命令"
      }
    ]

    EXECUTING_STATUS_START = 0
    EXECUTING_STATUS_PROGRESS = 1
    EXECUTING_STATUS_PAUSE = 2
    EXECUTING_STATUS_RESUME = 3
    EXECUTING_STATUS_STOP = 4
    EXECUTING_STATUS_COMPLETE = 5

import sys

sys.modules["__name__"] = Constant()
