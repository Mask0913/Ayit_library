# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ai_lib.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_auto_win(object):
    def setupUi(self, auto_win):
        auto_win.setObjectName("auto_win")
        auto_win.resize(756, 557)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        auto_win.setPalette(palette)
        auto_win.setStyleSheet("QLabel{color:#00aaff;}\n"
"QLCDNumber{\n"
"    color:red;    \n"
"}")
        self.centralwidget = QtWidgets.QWidget(auto_win)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet("QLable{color:#00aaff;}")
        self.centralwidget.setObjectName("centralwidget")
        self.layout = QtWidgets.QPushButton(self.centralwidget)
        self.layout.setGeometry(QtCore.QRect(600, 400, 121, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.layout.setFont(font)
        self.layout.setStyleSheet("QPushButton{color:white;\n"
"            border:2px solid black;\n"
"            border-radius:30px;\n"
"            background:#8a9cff;}\n"
"")
        self.layout.setObjectName("layout")
        self.cancle_seat = QtWidgets.QPushButton(self.centralwidget)
        self.cancle_seat.setEnabled(True)
        self.cancle_seat.setGeometry(QtCore.QRect(280, 90, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancle_seat.setFont(font)
        self.cancle_seat.setAcceptDrops(False)
        self.cancle_seat.setAutoFillBackground(False)
        self.cancle_seat.setStyleSheet("QPushButton{color:black;\n"
"                    border:2px solid black;\n"
"                    border-radius:50px;\n"
"                    background:#c6c0ff;}\n"
"")
        self.cancle_seat.setAutoDefault(False)
        self.cancle_seat.setDefault(False)
        self.cancle_seat.setObjectName("cancle_seat")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(560, 240, 20, 281))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(220, 230, 511, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 751, 65))
        self.label.setMouseTracking(True)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{color:black;\n"
"font-size:50px;\n"
"background:#f2f4ff;\n"
"font-family:微软雅黑}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.take_seat = QtWidgets.QPushButton(self.centralwidget)
        self.take_seat.setGeometry(QtCore.QRect(140, 90, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.take_seat.setFont(font)
        self.take_seat.setAutoFillBackground(False)
        self.take_seat.setStyleSheet("QPushButton{color:black;\n"
"            border:2px solid black;\n"
"            border-radius:50px;\n"
"            background:#cafff0;}\n"
"")
        self.take_seat.setObjectName("take_seat")
        self.register_2 = QtWidgets.QPushButton(self.centralwidget)
        self.register_2.setGeometry(QtCore.QRect(600, 250, 121, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.register_2.setFont(font)
        self.register_2.setStyleSheet("QPushButton{color:white;\n"
"            border:2px solid black;\n"
"            border-radius:30px;\n"
"            background:#8a9cff;}\n"
"")
        self.register_2.setObjectName("register_2")
        self.see_seat = QtWidgets.QPushButton(self.centralwidget)
        self.see_seat.setGeometry(QtCore.QRect(420, 90, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.see_seat.setFont(font)
        self.see_seat.setAutoFillBackground(False)
        self.see_seat.setStyleSheet("QPushButton{color:black;\n"
"                    border:2px solid black;\n"
"                    border-radius:50px;\n"
"                    background:#ffddd2;}\n"
"")
        self.see_seat.setObjectName("see_seat")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 240, 551, 291))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.textEdit.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.eidtor_user_data = QtWidgets.QPushButton(self.centralwidget)
        self.eidtor_user_data.setGeometry(QtCore.QRect(10, 90, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.eidtor_user_data.setFont(font)
        self.eidtor_user_data.setAutoFillBackground(False)
        self.eidtor_user_data.setStyleSheet("QPushButton{color:black;\n"
"            border:2px solid black;\n"
"            border-radius:50px;\n"
"            background:#cafff0;}\n"
"")
        self.eidtor_user_data.setObjectName("eidtor_user_data")
        self.magic = QtWidgets.QPushButton(self.centralwidget)
        self.magic.setGeometry(QtCore.QRect(560, 80, 171, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.magic.setFont(font)
        self.magic.setAutoFillBackground(False)
        self.magic.setStyleSheet("QPushButton{color:black;\n"
"                    border:2px solid black;\n"
"                    border-radius:50px;\n"
"                    background:#ffddd2;}\n"
"")
        self.magic.setObjectName("magic")
        auto_win.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(auto_win)
        self.statusbar.setObjectName("statusbar")
        auto_win.setStatusBar(self.statusbar)

        self.retranslateUi(auto_win)
        QtCore.QMetaObject.connectSlotsByName(auto_win)

    def retranslateUi(self, auto_win):
        _translate = QtCore.QCoreApplication.translate
        auto_win.setWindowTitle(_translate("auto_win", "MainWindow"))
        self.layout.setText(_translate("auto_win", "签退"))
        self.cancle_seat.setText(_translate("auto_win", "取消占位"))
        self.label.setText(_translate("auto_win", "图书馆占位系统"))
        self.take_seat.setText(_translate("auto_win", "占位"))
        self.register_2.setText(_translate("auto_win", "签到"))
        self.see_seat.setText(_translate("auto_win", "看位"))
        self.eidtor_user_data.setText(_translate("auto_win", "修改用户"))
        self.magic.setText(_translate("auto_win", "停止占位"))
