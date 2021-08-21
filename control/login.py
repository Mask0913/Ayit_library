#coding=utf-8

import sys
import PyQt5.sip
from PyQt5.QtWidgets import *
from login2 import Ui_login
import win32api
import base64
import os
from ai_lib import auto_win





class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_login()
        self.UI.setupUi(self)
        self.ant = self.getCVolumeSerialNumber()
        self.key = self.get_key(self.ant)
        self.UI.account.setText(self.ant)
        self.UI.login_btn.clicked.connect(lambda :self.login())
        self.UI.register_btn.clicked.connect(lambda :self.register())
        self.UI.findpwd_btn.clicked.connect(lambda :self.findpwd())
        if os.path.exists('key.txt'):
            self.f = open('key.txt', 'r')
            self.yourkey = str(self.f.read())
            self.UI.password.setText(self.yourkey)
    #登录
    def login(self):
        peopleId = self.UI.account.text()
        peoplePassword = self.UI.password.text()
        if len(peopleId) is 0 or len(peoplePassword) is 0:
            QMessageBox.information(self, '提示','账号或密码不能为空！',QMessageBox.Yes)
            return
        elif peoplePassword in self.key and len(peoplePassword) > 8:
            self.f = open('key.txt', 'w')
            self.f.write(str(peoplePassword))
            self.f.close()
            QMessageBox.information(self, '提示', '登录成功', QMessageBox.Yes)
            autowin_ = auto_win()
            autowin_.show()
            self.close()
        else:
            QMessageBox.information(self, '提示','账号或密码错误',QMessageBox.Yes)

    #注册
    def register(self):
        QMessageBox.information(self, '提示', '请联系管理员',QMessageBox.Yes)
    def findpwd(self):
        QMessageBox.information(self, '提示', '请联系管理员',QMessageBox.Yes)

    def getCVolumeSerialNumber(self):
        CVolumeSerialNumber = win32api.GetVolumeInformation("C:\\")[1]
        if CVolumeSerialNumber:
            return str(CVolumeSerialNumber)
        else:
            return 0

    def get_key(self, account):
        account = int(account) * 8 - 15 + 50 * 18 / 30
        account = str(account)
        account = bytes(account, encoding='utf8')
        key = base64.encodestring(account)
        key = str(key, encoding='utf-8')
        return key


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Login()
    mainWindow.show()
    sys.exit(app.exec_())