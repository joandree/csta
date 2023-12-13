import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from tela import Ui_MainWindow

class mianWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__(self)
        self.ui = Ui_MainWindow( )
        self.ui.setupUi(self)
        self.show()
    pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mianWindow()
    sys.exit(app.exec_())