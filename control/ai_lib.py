#coding=utf-8
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
import _thread
from PyQt5.QtCore import *
import json
import time
import socket
import PyQt5.sip


class Thread(QThread):
    _signal = pyqtSignal(str)
    def __init__(self,userid, seatid,username):
        super(Thread, self).__init__()
        self.userid = userid
        self.seatid = seatid
        self.username = username
    def run(self):
        #今天的坑
        x = str(datetime.datetime.now())
        start_time = x[0:10] + '%20' + x[11:16]
        end_time = x[0:10] + '%2022:30'
        #明天的坑
        # tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        # start_time = tomorrow + '%2007:00'
        # end_time = tomorrow + '%2022:30'
        url = 'https://www.360banke.com/xiaotu/Seatresv/seatorder.asp?number=0.5260297873297035&userid={}&seatid={}' \
              '&validtime={}&invalidtime={}'.format(self.userid, self.seatid, start_time, end_time)
        headers = {'Host': 'www.360banke.com', 'Connection': 'keep-alive',
                   'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                   'sec-ch-ua-mobile': '?0', 'User-Agent': 'LogStatistic', 'Accept': '*/*',
                   'Origin': 'http://211.84.229.61', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-Mode': 'cors',
                   'Sec-Fetch-Dest': 'empty', 'Referer': 'http://211.84.229.61/',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {}
        data = {}
        try:
            html = requests.get(url, headers=headers, verify=False, cookies=cookies)
        except Exception as e:
            pass
        result = str(html.text)
        print(self.username + str(result) + str(datetime.datetime.now()))
        self._signal.emit(result)

class Thread2(QThread):
    _signal = pyqtSignal(str)
    def __init__(self, userid):
        super(Thread2, self).__init__()
        self.userid = userid
    def run(self):
        self.seatid = self.get_random_seatid()
        if self.seatid == False:
            self.sleep(6)
            self._signal.emit('一个坑都没有了，真的没办法了')
        else:
            #今天的坑
            x = str(datetime.datetime.now())
            start_time = x[0:10] + '%20' + x[11:16]
            end_time = x[0:10] + '%2022:30'

            # 明天的坑
            # tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            # start_time = tomorrow + '%2007:00'
            # end_time = tomorrow + '%2022:30'
            url = 'https://www.360banke.com/xiaotu/Seatresv/seatorder.asp?number=0.5260297873297035&userid={}&seatid={}' \
                  '&validtime={}&invalidtime={}'.format(self.userid, self.seatid, start_time, end_time)
            headers = {'Host': 'www.360banke.com', 'Connection': 'keep-alive',
                       'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                       'sec-ch-ua-mobile': '?0', 'User-Agent': 'LogStatistic', 'Accept': '*/*',
                       'Origin': 'http://211.84.229.61', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-Mode': 'cors',
                       'Sec-Fetch-Dest': 'empty', 'Referer': 'http://211.84.229.61/',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'zh-CN,zh;q=0.9'}
            cookies = {}
            data = {}
            html = requests.get(url, headers=headers, verify=False, cookies=cookies)
            result = str(html.text)
            self.sleep(6)
            self._signal.emit(result)

    def get_random_seatid(self):
        self._signal.emit('没有你想要的坑，下面为你随机一个坑')
        tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        start_time = tomorrow + '%2007:00'
        end_time = tomorrow + '%2022:30'
        url = 'https://www.360banke.com/xiaotu/Seatresv/RandomSeat.asp?libid=ayit&mapid=830&userid=12345&number=0.6922689160823745&starttime={}&endtime={}'.format(start_time,end_time)
        headers = {'Host': 'www.360banke.com', 'Connection': 'keep-alive',
                   'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                   'sec-ch-ua-mobile': '?0', 'User-Agent': 'LogStatistic', 'Accept': '*/*',
                   'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty',
                   'Referer': 'https://www.360banke.com/xiaotu/index.html?libid=ayit',
                   'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {'ASPSESSIONIDQURRRDAS': 'AHBMNKODIBJKFLPOJMIOKKNK'}
        data = {}

        html = requests.get(url, headers=headers, verify=False, cookies=cookies)
        print(html.text)
        x = json.loads(html.text)
        if x['msg'] == "":
            print(x['seatid'])
            print(x['areatag'])
            print(x['seatnum'])
            return x['seatid']
        else:
            return False




class auto_win(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_auto_win()
        self.UI.setupUi(self)
        self.console = self.UI.textEdit
        self.UI.eidtor_user_data.clicked.connect(lambda: self.eidtor_user_data())
        self.UI.take_seat.clicked.connect(lambda: self.take_seat())
        self.UI.register_2.clicked.connect(lambda: self.register())
        self.UI.cancle_seat.clicked.connect(lambda: self.cancle())
        self.UI.see_seat.clicked.connect(lambda: self.see_seat())
        self.UI.magic.clicked.connect(lambda: self.magic1())
        self.UI.layout.clicked.connect(lambda: self.lay())
        self.thread = None  # 初始化线程
        self.n = 0
        self.thread2 = []
        self.thread_pool = []
        self.get_user_data()

    def eidtor_user_data(self):
        edite_user_ = admin_grasping(auto_win)
        edite_user_.show()
        self.close()

    def sent_txt(self, strs):
        str1 = self.console.toPlainText()
        str1 +=str(datetime.datetime.now())[0:-7] + ':  ' + strs + '\n'
        self.console.setText(str1)
        self.console.moveCursor(QTextCursor.End)

    def take_seat(self):
        x = str(datetime.datetime.now())[11:18]
        if x > '19:55':
            self.sent_txt('19:55在来，现在急个啥')
        else:
            while True:
                if x < '19:59':
                    self.sent_txt('现在开始占坑')
                    n = 0
                    while n < 10:
                        for i in self.user_list:
                            self.x = Thread(i[0], i[4], i[2])
                            self.x._signal.connect(self.call_backlog)
                            self.thread_pool.append(self.x)
                            self.thread_pool[n].start()
                            n += 1
                    break
                else:
                    self.sent_txt('等19:59')
                    self.sleep(1)

        # self.thread = users(self.user_list, 1)
        # self.thread._signal.connect(self.call_backlog)  # 进程连接回传到GUI的事件
        # self.thread.start()

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
        if msg == '19:55在来，现在急个啥':
            QMessageBox.information(self, '提示', '19:55在来，现在急个啥', QMessageBox.Yes)
        if '已被他人预约' in msg and self.n == 0:
            for i in self.user_list:
                self.y = Thread2(i[0])
                self.y._signal.connect(self.call_backlog)
                self.thread2.append(self.y)
                self.thread2[self.n].start()
                self.n += 1



    def see_seat(self):
        self.see = admin_login()
        self.see._signal.connect(self.call_back_see)
        self.see.show()

    def magic1(self):
        self.mg = magic()
        self.mg._signal.connect(self.call_back_mgc)
        self.mg.show()

    def call_back_mgc(self, msg):
        self.sent_txt(msg)
        now = str(datetime.datetime.now())
        filename = now[0:10] + '.txt'
        if not os.path.exists(filename):
            self.sent_txt('找不到当天的座位信息文件')
            self.sent_txt('开始下载')
            self.download()
        self.magic2(msg)

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
            except:
                self.sent_txt(seats[user_list[i][1]] + '不存在')
                QMessageBox.information(self, '提示', '账号输入有误，请检查user_data.txt文件', QMessageBox.Yes)
                exit()
        self.user_list = user_list
        self.sent_txt(str(self.user_list))
        self.sent_txt('初始化成功')

    def get_id(self, account, password):
        url = 'https://www.360banke.com/xiaotu/interface/ayit/user_login.asp?libid=ayit&username=' + account + '&password=' + password
        headers = {'Host': 'www.360banke.com',
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
        html = requests.get(url, headers=headers, verify=False, cookies=cookies)
        print(html.text)
        if (len(html.text) < 40):
            QMessageBox.information(self, '提示', '需要占位置的数据有误，请检查user_data.txt文件', QMessageBox.Yes)
            exit()
        x = json.loads(html.text)
        userid = x['userid']
        user_name = x['nickname']
        return userid, user_name

    def download(self):
        client = socket.socket()
        client.connect(("1.116.4.250", 1234))
        now = str(datetime.datetime.now())
        now = now[0:10] + '.txt'
        while True:
            cmd = 'get ' + now
            if len(cmd) == 0: continue
            if cmd.startswith("get"):
                client.send(cmd.encode())  # 发送请求
                server_response = client.recv(1024)
                if server_response.decode().startswith("not"):
                    print("请输入有效文件名")
                    continue
                client.send(b"ready to recv file")  # 发送确认
                file_size = int(server_response.decode())  # 获取文件大小
                rece_size = 0
                filename = cmd.split()[1]
                f = open(filename, "wb")
                while rece_size < file_size:
                    if file_size - rece_size > 1024:  # 要收不止一次
                        size = 1024
                    else:  # 最后一次了，剩多少收多少,防止之后发送数据粘包
                        size = file_size - rece_size
                    recv_data = client.recv(size)
                    rece_size += len(recv_data)  # 累加接受数据大小
                    f.write(recv_data)  # 写入文件,即下载
                else:
                    self.sent_txt("文件下载完成")
                    f.close()
                    time.sleep(1)
                    client.close()
                    break

    def magic2(self, seat):
        now = str(datetime.datetime.now())
        filename = now[0:10] + '.txt'
        f = open(filename, 'r')
        temp = f.read()
        seats = eval(temp)
        f.close()
        f = open('seat.txt','r')
        dic = f.read()
        dic = eval(dic)
        f.close()
        try:
            seatid = dic[seat][0]
            userid = seats[seat]
            self.get_away(userid, seatid)
            self.to_cancle(userid, self.get_cancle_id(userid))
            self.sent_txt('你可真是个好人\n')
        except:
            self.sent_txt('找不到此人')

    def magic3(self, seat1, seat2):
        now = str(datetime.datetime.now())
        filename = now[0:10] + '.txt'
        f = open(filename, 'r')
        temp = f.read()
        seats = eval(temp)
        f.close()
        f = open('seat.txt','r')
        dic = f.read()
        dic = eval(dic)
        f.close()
        try:
            seatid1 = dic[seat1][0]
            seatid2 = dic[seat2][0]
            userid1 = seats[seat1]
            userid2 = seats[seat2]
            self.get_away(userid1, seatid1)
            self.get_away(userid2, seatid2)
            self.to_cancle(userid1, self.get_cancle_id(userid1))
            self.to_cancle(userid2, self.get_cancle_id(userid2))
            self.sent_txt('你可真是个好人\n')
        except:
            self.sent_txt('找不到此人')

    def get_away(self, userid, seatid):
        url = 'https://www.360banke.com/xiaotu/Seatresv/CheckOut.asp?libid=ayit&seatid={}&userid={}&number=0.03153986302655798'.format(
            seatid, userid)
        headers = {'Host': 'www.360banke.com', 'Connection': 'keep-alive', 'Origin': 'http://www.360banke.com',
                   'User-Agent': 'Mozilla/5.0 (Linux; Android 10; 16th Plus Build/QKQ1.191222.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2797 MMWEBSDK/20210302 Mobile Safari/537.36 MMWEBID/1946 MicroMessenger/8.0.3.1880(0x28000339) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
                   'Accept': '*/*', 'X-Requested-With': 'com.tencent.mm', 'Sec-Fetch-Site': 'cross-site',
                   'Sec-Fetch-Mode': 'cors',
                   'Referer': 'http://www.360banke.com/xiaotu/index.html?seatid=A9097E62-5E85-4E71-9C24-C8EC3C281806&seatresv=1&libid=ayit&result=1&username=18031110137&openid=oMWEVxCCJqyGcEgUMPipHy5oMD-0',
                   'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}
        cookies = {}
        data = {}

        html = requests.get(url, headers=headers, verify=False, cookies=cookies)
        self.sent_txt(str(html.text))

    def to_cancle(self, userid, cancle_id):
        url = 'https://www.360banke.com/xiaotu/Seatresv/CancelOrder.asp?libid=ayit&seatorderid={}&userid={}&number=0.20709293419268082'.format(
            cancle_id, userid)
        headers = {'Host': 'www.360banke.com', 'Connection': 'keep-alive',
                   'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                   'sec-ch-ua-mobile': '?0', 'User-Agent': 'LogStatistic', 'Accept': '*/*',
                   'Origin': 'http://www.360banke.com', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-Mode': 'cors',
                   'Sec-Fetch-Dest': 'empty', 'Referer': 'http://www.360banke.com/',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {}
        data = {}
        html = requests.get(url, headers=headers, verify=False, cookies=cookies)
        self.sent_txt(str(html.text))

    def get_cancle_id(self, userid):
        url = 'https://www.360banke.com/xiaotu/Seatresv/GetMyOrder.asp?userid={}&number=0.7515593691892066'.format(
            userid)
        headers = {'Host': 'www.360banke.com', 'Connection': 'keep-alive',
                   'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
                   'sec-ch-ua-mobile': '?0', 'User-Agent': 'LogStatistic', 'Accept': '*/*',
                   'Origin': 'http://www.360banke.com', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-Mode': 'cors',
                   'Sec-Fetch-Dest': 'empty', 'Referer': 'http://www.360banke.com/',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {}
        data = {}

        html = requests.get(url, headers=headers, verify=False, cookies=cookies)
        x = json.loads(html.text)
        id = x['seatorder'][0]['seatorderid']
        return id

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = auto_win()
    mainWindow.show()
    sys.exit(app.exec_())
