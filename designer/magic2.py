# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'magic.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_magic(object):
    def setupUi(self, magic):
        magic.setObjectName("magic")
        magic.resize(402, 161)
        magic.setStyleSheet("*{    \n"
"    font-family:微软雅黑;\n"
"    font-size:15px;\n"
"    color: #1d649c;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(magic)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 5, 5, 5)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.seat_number = QtWidgets.QLineEdit(self.centralwidget)
        self.seat_number.setObjectName("seat_number")
        self.horizontalLayout.addWidget(self.seat_number)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.gun = QtWidgets.QPushButton(self.centralwidget)
        self.gun.setObjectName("gun")
        self.horizontalLayout_3.addWidget(self.gun)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        magic.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(magic)
        self.statusbar.setObjectName("statusbar")
        magic.setStatusBar(self.statusbar)
        self.label.setBuddy(self.seat_number)

        self.retranslateUi(magic)
        QtCore.QMetaObject.connectSlotsByName(magic)
        magic.setTabOrder(self.seat_number, self.gun)

    def retranslateUi(self, magic):
        _translate = QtCore.QCoreApplication.translate
        magic.setWindowTitle(_translate("magic", "MainWindow"))
        self.label_3.setText(_translate("magic", "Have you ever head magic"))
        self.label.setText(_translate("magic", "座位号"))
        self.gun.setText(_translate("magic", "滚"))
