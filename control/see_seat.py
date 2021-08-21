from PyQt5.QtWidgets import QDialog, QMessageBox,QApplication,QMainWindow
import sys
from see_seat2 import Ui_see_seat
from PyQt5.QtCore import pyqtSignal


class admin_login(QMainWindow):
    _signal = pyqtSignal(str)
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_see_seat()
        self.UI.setupUi(self)
        self.UI.control1.clicked.connect(lambda: self.control1())
        self.UI.control2.clicked.connect(lambda: self.control2())


    def control1(self):
        text = '1'
        self._signal.emit(text)
        self.close()
    def control2(self):
        text = '2'
        self._signal.emit(text)
        self.close()


