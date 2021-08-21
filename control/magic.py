from PyQt5.QtWidgets import QDialog, QMessageBox,QApplication,QMainWindow
import sys
from magic2 import Ui_magic
from PyQt5.QtCore import pyqtSignal


class magic(QMainWindow):
    _signal = pyqtSignal(str)
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_magic()
        self.UI.setupUi(self)
        self.UI.gun.clicked.connect(lambda: self.gun())

    def gun(self):
        text = self.UI.seat_number.text()
        self._signal.emit(text)
        self.close()



