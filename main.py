
from PyQt5 import QtWidgets
from controller.IndexController import IndexController

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = IndexController()
    window.show()
    sys.exit(app.exec_())

