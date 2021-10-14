# coding=utf-8
import os
import sys
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog
from ai_lib2 import Ui_auto_win
from edite_user import admin_grasping
from see_seat import admin_login
from magic import magic
import datetime
from tools import users
import requests
import threading
from PyQt5.QtCore import *
import json
import time
import socket
import PyQt5.sip


class Mythread(QThread):
    _signal = pyqtSignal(str)
    def __init__(self, userid, seatid, seatPlace):
        super().__init__()
        self.userid = userid
        self.seatid = seatid
        self.status = 3
        self.seatPlace = seatPlace

    def run(self):
        tomorrow = (
            datetime.date.today() +
            datetime.timedelta(
                days=1)).strftime("%Y-%m-%d")
        starttime = tomorrow + ' 07:00'
        endtime = tomorrow + ' 22:30'
        now = str(datetime.datetime.now())
        now = now[:-7]
        url = "libid=ayit&seatid={}&userid={}&validtime={}&invalidtime={}&number=0.6986631503360254&time={}".format(
            self.seatid, self.userid, starttime, endtime, now)
        url = self.crypto(str(url))
        url = "https://www.360banke.com/xiaotu/Seatresv/SeatOrder.asp?" + url
        headers = {
            'Host': 'www.360banke.com',
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'LogStatistic',
            'sec-ch-ua-platform': '"Windows"',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.360banke.com/xiaotu/index.html?seatid=7C746671-984D-4596-9D10-E83C64922F9D&seatresv=1&libid=ayit',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {'ASPSESSIONIDCUATSCTA': 'KFBPHGJDPINKMEJMDHNNIHHM'}
        data = {}
        s = requests.session()
        s.keep_alive = False  # 关闭多余连接
        try:
            html = requests.get(
                url,
                headers=headers,
                verify=False,
                cookies=cookies)
            result = str(html.text)
            print(result)
            if '同时' in result:
                self.status = 1
                print(
                    "Don't do anything for more than two times!   位置：{}".format(
                        self.seatPlace))
            elif "已被" in result:
                self.status = 2
                print(
                    '          垃圾小霸王服务器，占不到坑   位置：{}   '.format(
                        self.seatPlace))
            elif '成功' in result:
                self.status = 1
                print(result)
                print(
                    '        s  注意我的解题手法     位置：{}   '.format(
                        self.seatPlace))
            elif '失败' in result:
                self.status = 0
                print('还没到点，急个啥？   位置：{}   '.format(self.seatPlace))
            else:
                self.status = 0
                #self._signal.emit('Http1.2 精妙无比   位置：{}   '.format(self.seatPlace))
        except Exception as e:
            self.status = 0
            print(e)
            print('啥几把玩意服务器代码报错   位置：{}   '.format(self.seatPlace))

    def crypto(self, url):
        n = 0
        e = ["", "g", "h", "i"]
        i = "wx3cba883abac619bb"
        a = ''
        for s in url:
            r = ord(s) + 2
            if n >= len(i):
                n = 0
            r += ord(i[n])
            o = str(hex(r))
            o = o[2:]
            if len(o) < 4:
                h = ''
                h = e[4 - len(o)]
                o = h + o
            a += o
            n += 1
        return a


class Mythread2(QThread):
    def __init__(self, userid, number):
        super().__init__()
        self.userid = userid
        self.oldseat = number
        self.seat = 'None'
        self.seatid = 'None'
        self.flag = 0

    def run(self):
        url = 'https://www.360banke.com/xiaotu/seatresv/RandomSeatQuick/RandomSeatorder/?userid={}&libid=ayit&code=0&state=1&result=1&username=18031110221&openid=0'.format(
            self.userid)
        headers = {
            'Host': 'www.360banke.com',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'LogStatistic',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.360banke.com/xiaotu/index.html?libid=ayit',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {'ASPSESSIONIDQURRRDAS': 'AHBMNKODIBJKFLPOJMIOKKNK'}
        data = {}
        try:
            html = requests.get(
                url,
                headers=headers,
                verify=False,
                cookies=cookies)
            result = str(html.text)
            print(result)
            if '成功' in result:
                self.seat = 'OK'
            else:
                self.run()
        except BaseException:
            time.sleep(1)
            self.run()


class Mythread3(QThread):
    _signal = pyqtSignal(str)

    def __init__(self, userlist, call_backlog):
        super().__init__()
        self.user_list = userlist
        self.call_backlog = call_backlog
        self.stop_flag = 0

    def run(self):
        n = 0
        thread_pool = []
        not_get = []
        for i in self.user_list:
            try:
                thread_pool.append(Mythread(i[0], i[4], i[1]))
                thread_pool[n]._signal.connect(self.call_backlog)
                thread_pool[n].start()
            except Exception as e:
                print(e)
            n += 1
            time.sleep(0.2)
        thread_pool = []
        n = 0
        for i in self.user_list:
            try:
                thread_pool.append(Mythread(i[0], i[4], i[1]))
                thread_pool[n].start()
            except Exception as e:
                print(e)
            n += 1
            time.sleep(0.2)
        self._signal.emit('启动监控线程，出现预约失败的包，重新预约')
        not_get_thread_pool = []
        while True:
            for i in range(0, len(thread_pool)):
                if thread_pool[i].status == 0:
                    self._signal.emit(
                        '{}预约失败,重新预约(未到8:00时间或服务器繁忙)'.format(
                            thread_pool[i].seatPlace))
                    try:
                        m = Mythread(
                            thread_pool[i].userid,
                            thread_pool[i].seatid,
                            thread_pool[i].seatPlace)
                        m.start()
                        thread_pool[i] = m
                    except BaseException:
                        pass
                elif thread_pool[i].status == 2:
                    if thread_pool[i].seatPlace not in not_get:
                        self._signal.emit(
                            '{}位置没抢到，随机抢一个'.format(
                                thread_pool[i].seatPlace))
                        not_get.append(thread_pool[i].seatPlace)
                        m = Mythread2(
                            thread_pool[i].userid,
                            thread_pool[i].seatPlace)
                        m.start()
                        not_get_thread_pool.append(m)
                elif thread_pool[i].status == 1:
                    self._signal.emit(
                        '{}位置已经抢到'.format(
                            thread_pool[i].seatPlace))
                time.sleep(0.2)
            if self.stop_flag == 1:
                break


class auto_win(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_auto_win()
        self.UI.setupUi(self)
        self.console = self.UI.textEdit
        self.UI.eidtor_user_data.clicked.connect(
            lambda: self.eidtor_user_data())
        self.UI.take_seat.clicked.connect(lambda: self.take_seat())
        self.UI.register_2.clicked.connect(lambda: self.register())
        self.UI.cancle_seat.clicked.connect(lambda: self.cancle())
        self.UI.see_seat.clicked.connect(lambda: self.see_seat())
        self.UI.magic.clicked.connect(lambda: self.stop_takeseat())
        self.UI.layout.clicked.connect(lambda: self.lay())
        self.thread = None  # 初始化线程
        self.n = 0
        self.thread2 = []
        self.thread_pool = []
        self.get_user_data()
        self.take_seat_thread = None

    def eidtor_user_data(self):
        edite_user_ = admin_grasping(auto_win)
        edite_user_.show()
        self.close()

    def sent_txt(self, strs):
        str1 = self.console.toPlainText()
        str1 += str(datetime.datetime.now())[0:-7] + ':  ' + strs + '\n'
        self.console.setText(str1)
        self.console.moveCursor(QTextCursor.End)

    def take_seat(self):
        self.take_seat_thread = Mythread3(self.user_list, self.call_backlog)
        self.take_seat_thread._signal.connect(self.call_backlog)
        self.take_seat_thread.start()
        time.sleep(1)

    def stop_takeseat(self):
        try:
            self.take_seat_thread.stop_flag = 1
        except BaseException:
            QMessageBox.information(self, '提示', '还没开始停个啥？', QMessageBox.Yes)
        self.sent_txt('停止占位置')

    def cancle(self):
        self.thread = users(self.user_list, 2)
        self.thread._signal.connect(self.call_backlog)  # 进程连接回传到GUI的事件
        self.thread.start()

    def register(self):
        self.thread = users(self.user_list, 5)
        self.thread._signal.connect(self.call_backlog)  # 进程连接回传到GUI的事件
        self.thread.start()

    def lay(self):
        self.thread = users(self.user_list, 6)
        self.thread._signal.connect(self.call_backlog)  # 进程连接回传到GUI的事件
        self.thread.start()

    def call_backlog(self, msg):
        self.sent_txt(msg)  # 将线程的参数传入进度条

    def see_seat(self):
        self.see = admin_login()
        self.see._signal.connect(self.call_back_see)
        self.see.show()

    def magic1(self):
        self.mg = magic()
        self.mg._signal.connect(self.call_back_mgc)
        self.mg.show()

    def call_back_see(self, msg):
        if msg == '1':
            self.thread = users(self.user_list, 3.1)
            self.thread._signal.connect(self.call_backlog)  # 进程连接回传到GUI的事件
            self.thread.start()
        elif msg == '2':
            self.thread = users(self.user_list, 3.2)
            self.thread._signal.connect(self.call_backlog)  # 进程连接回传到GUI的事件
            self.thread.start()

    def get_user_data(self):
        f = open('user_data.txt', 'r')
        c = f.read()
        user_data = eval(c)
        f.close()
        f = open('seat.txt', 'r')
        temp = f.read()
        seats = eval(temp)
        f.close()
        user_list = []
        for i in user_data:
            userid, user_name = self.get_id(i[0], i[1])
            user_list.append([userid, i[2], i[0], user_name])
        for i in range(len(user_list)):
            try:
                user_list[i].append(seats[user_list[i][1]][0])
            except BaseException:
                self.sent_txt(seats[user_list[i][1]] + '不存在')
                QMessageBox.information(
                    self, '提示', '账号或密码输入有误，请检查user_data.txt文件', QMessageBox.Yes)
        self.user_list = user_list
        self.sent_txt(str(self.user_list))
        self.sent_txt('初始化成功')

    def get_id(self, account, password):
        url = 'https://www.360banke.com/xiaotu/interface/ayit/user_login.asp?libid=ayit&username=' + \
            account + '&password=' + password
        headers = {
            'Host': 'www.360banke.com',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'LogStatistic',
            'Accept': '*/*',
            'Origin': 'http://211.84.229.61',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.360banke.com/xiaotu/index.html?libid=ayit',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {}
        data = {}
        html = requests.get(
            url,
            headers=headers,
            verify=False,
            cookies=cookies)
        print(html.text)
        if (len(html.text) < 40):
            QMessageBox.information(
                self,
                '提示',
                '需要占位置的数据有误，请检查user_data.txt文件',
                QMessageBox.Yes)
            exit()
        x = json.loads(html.text)
        userid = x['userid']
        user_name = x['nickname']
        return userid, user_name

    def get_away(self, userid, seatid):
        url = 'https://www.360banke.com/xiaotu/Seatresv/CheckOut.asp?libid=ayit&seatid={}&userid={}&number=0.03153986302655798'.format(
            seatid, userid)
        headers = {
            'Host': 'www.360banke.com',
            'Connection': 'keep-alive',
            'Origin': 'http://www.360banke.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; 16th Plus Build/QKQ1.191222.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2797 MMWEBSDK/20210302 Mobile Safari/537.36 MMWEBID/1946 MicroMessenger/8.0.3.1880(0x28000339) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
            'Accept': '*/*',
            'X-Requested-With': 'com.tencent.mm',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Referer': 'http://www.360banke.com/xiaotu/index.html?seatid=A9097E62-5E85-4E71-9C24-C8EC3C281806&seatresv=1&libid=ayit&result=1&username=18031110137&openid=oMWEVxCCJqyGcEgUMPipHy5oMD-0',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}
        cookies = {}
        data = {}

        html = requests.get(
            url,
            headers=headers,
            verify=False,
            cookies=cookies)
        self.sent_txt(str(html.text))

    def to_cancle(self, userid, cancle_id):
        url = 'https://www.360banke.com/xiaotu/Seatresv/CancelOrder.asp?libid=ayit&seatorderid={}&userid={}&number=0.20709293419268082'.format(
            cancle_id, userid)
        headers = {
            'Host': 'www.360banke.com',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'LogStatistic',
            'Accept': '*/*',
            'Origin': 'http://www.360banke.com',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'http://www.360banke.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {}
        data = {}
        html = requests.get(
            url,
            headers=headers,
            verify=False,
            cookies=cookies)
        self.sent_txt(str(html.text))

    def get_cancle_id(self, userid):
        url = 'https://www.360banke.com/xiaotu/Seatresv/GetMyOrder.asp?userid={}&number=0.7515593691892066'.format(
            userid)
        headers = {
            'Host': 'www.360banke.com',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'LogStatistic',
            'Accept': '*/*',
            'Origin': 'http://www.360banke.com',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'http://www.360banke.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {}
        data = {}

        html = requests.get(
            url,
            headers=headers,
            verify=False,
            cookies=cookies)
        x = json.loads(html.text)
        id = x['seatorder'][0]['seatorderid']
        return id


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = auto_win()
    mainWindow.show()
    sys.exit(app.exec_())
