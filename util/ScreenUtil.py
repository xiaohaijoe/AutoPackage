
from PyQt5.QtWidgets import QApplication

class ScreenUtil:

    @staticmethod
    def get_screen_size():
        desktop = QApplication.desktop()

        # 获取显示器分辨率大小
        screenRect = desktop.screenGeometry()
        height = screenRect.height()
        width = screenRect.width()

        return width, height