#coding=utf-8

import sys

from PyQt5.QtWidgets import *
from admin_grasping2 import Ui_admin_grasping
import PyQt5.sip




class admin_grasping(QMainWindow):

    def __init__(self, auto_win):
        QMainWindow.__init__(self)
        self.UI = Ui_admin_grasping()
        self.UI.setupUi(self)
        self.UI.careful.clicked.connect(lambda: self.careful())
        self.UI.save.clicked.connect(lambda: self.save())
        self.f = open('user_data.txt', 'r')
        self.user_data = self.f.read()
        self.f.close()
        self.UI.userdta_edite.setText(self.user_data)
        self.auto_win = auto_win

    def careful(self):
        QMessageBox.information(self, '提示', '注意格式！一楼1A1B1C1D开头5楼05开头 位置和排开头写0几', QMessageBox.Yes)
    def save(self):
        self.data = self.UI.userdta_edite.toPlainText()
        self.f = open('user_data.txt', 'w')
        self.f.write(self.data)
        self.f.close()
        QMessageBox.information(self, '提示', '保存成功', QMessageBox.Yes)
        auto_win_ = self.auto_win()
        auto_win_.show()
        self.close()



