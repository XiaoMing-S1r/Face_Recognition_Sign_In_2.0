"""
文件名：The_classes_about_UI.py

该文件存放的是“刷脸签到”系统中用户界面的各种类、控件等。
此文件是由"The_classes_about_UI.ui"通过外部工具PyUIC自动生成的，
而"The_classes_about_UI.ui"又是通过QT designer制作的。

作者：徐宇明
学号：2018047087
邮箱：william87668@outlook.com
"""
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'The_classes_about_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CamShow(object):
    def setupUi(self, CamShow):
        CamShow.setObjectName("CamShow")
        CamShow.resize(1600, 900)
        CamShow.setMinimumSize(QtCore.QSize(1600, 900))
        CamShow.setMaximumSize(QtCore.QSize(1600, 900))
        CamShow.setAutoFillBackground(False)
        CamShow.setStyleSheet("")
        CamShow.setIconSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(CamShow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 4, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 51, 511, 20))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.tips_browser = QtWidgets.QTextBrowser(self.frame_2)
        self.tips_browser.setGeometry(QtCore.QRect(-20, 0, 1611, 48))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tips_browser.setFont(font)
        self.tips_browser.setObjectName("tips_browser")
        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 5)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.video_show_label = QtWidgets.QLabel(self.frame_1)
        self.video_show_label.setGeometry(QtCore.QRect(20, 10, 960, 720))
        self.video_show_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.video_show_label.setText("")
        self.video_show_label.setObjectName("video_show_label")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_1)
        self.textBrowser.setGeometry(QtCore.QRect(1040, 10, 511, 721))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.frame_1, 1, 0, 1, 5)
        CamShow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CamShow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 18))
        self.menubar.setObjectName("menubar")
        CamShow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CamShow)
        self.statusbar.setObjectName("statusbar")
        CamShow.setStatusBar(self.statusbar)

        self.retranslateUi(CamShow)
        QtCore.QMetaObject.connectSlotsByName(CamShow)
        CamShow.setTabOrder(self.pushButton_1, self.pushButton_2)
        CamShow.setTabOrder(self.pushButton_2, self.pushButton_3)
        CamShow.setTabOrder(self.pushButton_3, self.pushButton_4)
        CamShow.setTabOrder(self.pushButton_4, self.pushButton_5)

    def retranslateUi(self, CamShow):
        _translate = QtCore.QCoreApplication.translate
        CamShow.setWindowTitle(_translate("CamShow", "刷脸签到"))
        self.pushButton_3.setText(_translate("CamShow", "学生签到情况"))
        self.pushButton_1.setText(_translate("CamShow", "开始签到"))
        self.pushButton_5.setText(_translate("CamShow", "帮助"))
        self.pushButton_4.setText(_translate("CamShow", "学生信息录入"))
        self.label.setText(_translate("CamShow", " 刷脸签到2.0     by.深圳大学 徐宇明"))
        self.pushButton_2.setText(_translate("CamShow", "结束签到"))
