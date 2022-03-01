# -*- coding: UTF-8 -*-
import requests
import json
import datetime
import re
import warnings
import time
import _thread
from PyQt5.QtCore import QThread, pyqtSignal
warnings.filterwarnings(action='ignore')


class Thread(QThread):
    def __init__(self, userid, seatid, signal):
        super(Thread, self).__init__()
        self.userid = userid
        self.seatid = seatid
        self._signal = signal

    def run(self):
        tomorrow = (
            datetime.date.today() +
            datetime.timedelta(
                days=1)).strftime("%Y-%m-%d")
        start_time = tomorrow + '%2007:00'
        end_time = tomorrow + '%2022:30'
        url = 'https://zwyy.ayit.edu.cn/Seatresv/seatorder.asp?number=0.5260297873297035&userid={}&seatid={}' \
              '&validtime={}&invalidtime={}'.format(self.userid, self.seatid, start_time, end_time)
        headers = {
            'Host': 'zwyy.ayit.edu.cn',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'LogStatistic',
            'sec-ch-ua-platform': '"Windows"',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://zwyy.ayit.edu.cn/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {'ASPSESSIONIDQCAQDQAD': 'MGKFIPOCACEHLPPLKGCJLLIM'}
        data = {}
        try:
            html = requests.get(
                url,
                headers=headers,
                verify=False,
                cookies=cookies)
        except Exception as e:
            pass
        result = str(html.text)
        print(result)
        self._signal.emit(result)


class users(QThread):
    _signal = pyqtSignal(str)

    def __init__(self, user_list, flag):
        super(users, self).__init__()
        self.flag = flag
        self.user_list = user_list
        self.thread = []
        self.cookie = ''
        with open('cookie.txt', 'r') as f:
            self.cookie = f.read()

    def __del__(self):
        self.wait()

    def run(self):
        if self.flag == 1:
            self.take_seat()
        elif self.flag == 2:
            self.cancle()
        elif self.flag == 3.1:
            self.get_table_status(1)
        elif self.flag == 3.2:
            self.get_table_status(2)
        elif self.flag == 5:
            self.register()
        elif self.flag == 6:
            self.away()

    def get_seat(self, userid, seatid):
        tomorrow = (
            datetime.date.today() +
            datetime.timedelta(
                days=1)).strftime("%Y-%m-%d")
        start_time = tomorrow + '%2007:00'
        end_time = tomorrow + '%2022:30'
        url = 'https://zwyy.ayit.edu.cn/Seatresv/seatorder.asp?number=0.5260297873297035&userid={}&seatid={}' \
              '&validtime={}&invalidtime={}'.format(userid, seatid, start_time, end_time)
        headers = {
            'Host': 'zwyy.ayit.edu.cn',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'LogStatistic',
            'sec-ch-ua-platform': '"Windows"',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://zwyy.ayit.edu.cn/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {'ASPSESSIONIDQCAQDQAD': 'MGKFIPOCACEHLPPLKGCJLLIM'}
        data = {}
        html = requests.get(
            url,
            headers=headers,
            verify=False,
            cookies=cookies)
        result = str(html.text)
        print(result)
        return result

    def take_seat(self):
        x = str(datetime.datetime.now())[11:18]
        if x < '19:55':
            self._signal.emit('19:55在来，现在急个啥')
        else:
            while True:
                if x > '19:59':
                    self._signal.emit('现在开始占坑')
                    n = 0
                    while n < 180:
                        for i in self.user_list:
                            x = Thread(i[0], i[4], self._signal)
                            self.thread.append(x)
                            self.thread[n].start()
                            n += 1
                            self.sleep(1)
                        self.sleep(1)
                    return 1
                else:
                    self._signal.emit('等19:59')
                    self.sleep(1)

    def register(self):
        for i in self.user_list:
            self.register_in_lib(i[0], i[4], i[2])

    def register_in_lib(self, userid, seatid, username):
        self.afterregister(username, seatid)
        url = 'https://zwyy.ayit.edu.cn/Seatresv/CheckIn.asp?libid=ayit&seatid={}&userid={}&lat=36.068855&lng=114.35006&number=0.12086418536726717'.format(
            seatid, userid)
        headers = {
            'Host': 'zwyy.ayit.edu.cn',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'LogStatistic',
            'sec-ch-ua-platform': '"Windows"',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://zwyy.ayit.edu.cn/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {'ASPSESSIONIDQCAQDQAD': 'MGKFIPOCACEHLPPLKGCJLLIM'}
        data = {}

        html = requests.get(
            url,
            headers=headers,
            verify=False,
            cookies=cookies)
        print(html.text)
        self._signal.emit(username + str(html.text))
        time.sleep(1)

    def afterregister(self, username, seatid):
        url = 'https://zwyy.ayit.edu.cn/php/getSignPackage.php?url=http%3A%2F%2Fwww.360banke.com%2Fxiaotu%2Findex.html%3Fsea' \
              'tid%{}%26seatresv%3D1%26libid%3Dayit%26result%3D1%26username%{}%26openid%3DoMWEVxCCJqyGcEgUMPipHy5oMD-0'.format(
                  seatid, username)
        headers = {
            'Host': 'zwyy.ayit.edu.cn',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'LogStatistic',
            'sec-ch-ua-platform': '"Windows"',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://zwyy.ayit.edu.cn/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {'ASPSESSIONIDQCAQDQAD': 'MGKFIPOCACEHLPPLKGCJLLIM'}
        data = {}

        html = requests.get(
            url,
            headers=headers,
            verify=False,
            cookies=cookies)
        print(html.text)
    def away(self):
        for i in self.user_list:
            self.get_away(i[0], i[4])

    def get_away(self, userid, seatid):
        url = 'https://zwyy.ayit.edu.cn/Seatresv/CheckOut.asp?libid=ayit&seatid={}&userid={}&number=0.03153986302655798'.format(
            seatid, userid)
        headers = {
            'Host': 'zwyy.ayit.edu.cn',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'LogStatistic',
            'sec-ch-ua-platform': '"Windows"',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://zwyy.ayit.edu.cn/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {'ASPSESSIONIDQCAQDQAD': 'MGKFIPOCACEHLPPLKGCJLLIM'}
        data = {}
        html = requests.get(
            url,
            headers=headers,
            verify=False,
            cookies=cookies)
        self._signal.emit(str(html.text))

    def get_table_status(self, flag):
        self._signal.emit('看坑比较慢，请多等一会')
        x = str(datetime.datetime.now())
        if flag == 1:
            starttime = x[0:10] + '%20' + x[11:16]
            endtime = x[0:10] + '%2022:30'
        elif flag == 2:
            tomorrow = (
                datetime.date.today() +
                datetime.timedelta(
                    days=1)).strftime("%Y-%m-%d")
            starttime = tomorrow + '%2007:00'
            endtime = tomorrow + '%2022:30'
        url = 'https://zwyy.ayit.edu.cn/Seatresv/GetTableList.asp?number=0.13820980593382015&mapid=834&starttime=2021-05-13%2022:05&endtime=2021-05-13%2022:30'
        headers = {
            'Host': 'zwyy.ayit.edu.cn',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'LogStatistic',
            'sec-ch-ua-platform': '"Windows"',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://zwyy.ayit.edu.cn/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {'ASPSESSIONIDQCAQDQAD': 'MGKFIPOCACEHLPPLKGCJLLIM'}
        data = {}

        html = requests.get(
            url,
            headers=headers,
            verify=False,
            cookies=cookies)
        x = json.loads(html.text)
        y = x['seattables']
        seats = {}

        for i in y:
            seattableid = i['seattableid']
            url = 'https://zwyy.ayit.edu.cn/Seatresv/GetTableInfo.asp?tableid={}&' \
                  'number=0.8444846184256927&starttime={}&endtime={}'.format(seattableid, starttime, endtime)
            headers = {
                'Host': 'zwyy.ayit.edu.cn',
                'Connection': 'keep-alive',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                'sec-ch-ua-mobile': '?0',
                'User-Agent': 'LogStatistic',
                'sec-ch-ua-platform': '"Windows"',
                'Accept': '*/*',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://zwyy.ayit.edu.cn/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9'}
            cookies = {'ASPSESSIONIDQCAQDQAD': 'MGKFIPOCACEHLPPLKGCJLLIM'}
            cookies = {}
            data = {}
            html = requests.get(
                url,
                headers=headers,
                verify=False,
                cookies=cookies)
            all_seat_status = json.loads(html.text)
            all_seat_status = all_seat_status['seats']
            for seat_status in all_seat_status:
                seat_row = re.findall("第(.*?)排", seat_status['seatnum'])[0]
                if int(seat_row) < 10:
                    seat_row = '0' + seat_row
                seat_number = re.findall("\n(.*?)号", seat_status['seatnum'])[0]
                seat = seat_row + seat_number
                seatid = seat_status['seatid']
                if seat_status['state'] == '空闲':
                    seats[seat] = [seatid, '可以搞']
                    print(seat)
                else:
                    seats[seat] = [seatid, '不太行']
                    print(seat)
        x = sorted(seats)
        temp = {}
        for i in x:
            temp[i] = seats[i]
        for key in temp.keys():
            self._signal.emit(key + ':  ' + temp[key][1])

    def cancle(self):
        for i in self.user_list:
            self.to_cancle(i[0], self.get_cancle_id(i[0]))

    def to_cancle(self, userid, cancle_id):

        url = 'https://zwqd.ayit.edu.cn/Seatresv/CancelOrder.asp?libid=ayit&seatorderid={}&userid={}&number=0.20709293419268082'.format(
            cancle_id, userid)
        headers = {
            'Host': 'zwqd.ayit.edu.cn',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'LogStatistic',
            'sec-ch-ua-platform': '"Windows"',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://zwqd.ayit.edu.cn/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {'ASPSESSIONIDQCAQDQAD': 'MGKFIPOCACEHLPPLKGCJLLIM',
                   'client_vpn_ticket': self.cookie}
        data = {}

        html = requests.get(
            url,
            headers=headers,
            verify=False,
            cookies=cookies)
        self._signal.emit(str(html.text))

    def get_cancle_id(self, userid):
        url = 'https://zwqd.ayit.edu.cn/Seatresv/GetMyOrder.asp?userid={}&number=0.7515593691892066'.format(
            userid)
        headers = {
            'Host': 'zwqd.ayit.edu.cn',
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'LogStatistic',
            'sec-ch-ua-platform': '"Windows"',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://zwqd.ayit.edu.cn/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'}
        cookies = {'ASPSESSIONIDQCAQDQAD': 'MGKFIPOCACEHLPPLKGCJLLIM',
                   'client_vpn_ticket': self.cookie}
        data = {}

        html = requests.get(
            url,
            headers=headers,
            verify=False,
            cookies=cookies)
        x = json.loads(html.text)
        id = x['seatorder'][0]['seatorderid']
        return id
