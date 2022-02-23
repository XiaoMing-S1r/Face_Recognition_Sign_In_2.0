"""
文件名：Face_Recognition_Sign_In.py

该文件是“刷脸签到”系统的主文件，运行此.py文件即可运行该“刷脸签到”系统。

作者：徐宇明
学号：2018047087
邮箱：william87668@outlook.com
"""
from The_classes_about_UI import Ui_CamShow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QIcon
from numpy import argmin
from sys import argv, exit
from qimage2ndarray import array2qimage
from os import listdir, system
from time import time, strftime, localtime
import cv2
import face_recognition


class CamShow(QMainWindow, Ui_CamShow):
    def __del__(self):
        try:
            self.video_capture.release()  # 释放资源
        except:
            return

    def __init__(self, parent=None):
        """初始化方法"""
        super(CamShow, self).__init__(parent)  # 将QMainWindow,Ui_CamShow的各种属性继承给CamShow类。
        self.setupUi(self)  # 用从Ui_CamShow中继承过来的setupUi函数来实现程序界面的创建和属性设置。
        self.CallBackFunctions()  # 控件回调函数。它定义了每一个功能控件的触发条件和相应的回调函数。
        self.students_photos_list = []  # 用于存储已经录入了系统的学生的照片。
        self.students_photos_encoding = []  # 用于存储已经录入了系统的学生的编码后的照片。
        self.known_face_names = []  # 用于存储已知学生面部的姓名的列表。
        self.attend_students_list = []  # 用于存储已经签到学生的姓名的列表（其元素为string类型）。
        self.Prepare()  # 初始化其他内容（包括对用户界面按键可按/不可按的初始化，学生照片的加载等）。
        self.attend_times_list = []  # 用于存储已经签到学生的到达时间。
        self.Timer = QTimer()  # 定义定时器。
        self.Timer.timeout.connect(self.Face_Recognition_Begin)  # 回调。

    def Prepare(self):
        """初始化各项内容"""
        # 对用户界面的各个按键初始化（可按/不可按）
        # self.pushButton_1     用户界面上方的“开始签到”按键
        # self.pushButton_2     用户界面上方的“结束签到”按键
        # self.pushButton_3     用户界面上方的“学生签到情况”按键
        # self.pushButton_4     用户界面上方的“学生信息录入”按键
        # self.pushButton_5     用户界面上方的“帮助”按键
        # self.tips_browser     用户界面最下方的用于显示提示信息的文本框
        # self.textBrowser      用户界面右边的用于信息输出的文本框
        # self.video_show_label 用户界面左边的用于显示视频的方框
        self.pushButton_1.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        # 加载所有学生的照片（照片存放在当前目录下的"Students_Photos"文件夹中）并进行编码
        self.Load_Students_Photos("Students_Photos")
        # 在用户界面上输出欢迎信息
        self.tips_browser.clear()
        self.tips_browser.append(" 欢迎使用刷脸签到人脸识别签到系统！")
        # 在右边的信息输出文本框（self.textBrowser）显示帮助信息
        self.Help()
        # 在左边的显示视频的方框（self.video_show_label）显示背景图片
        bgp = QPixmap('background.jpg')
        self.video_show_label.setPixmap(bgp)
        # 设置窗口左上角的图标
        self.setWindowIcon(QIcon("logo.ico"))

    def Load_Students_Photos(self, directory_name):
        """加载所有学生的照片并进行编码"""
        for file_name in listdir(r"./" + directory_name):
            # 对文件夹“directory_name（字符串类型）”中的图片逐个进行加载，并将色彩转换为'RGB'格式
            img = face_recognition.load_image_file(directory_name + "/" + file_name, mode='RGB')
            # 读取文件夹下所有图片,并将其存放在列表students_photos_list中
            self.students_photos_list.append(img)
            # 对读取到的图片进行编码，并存放中列表students_photos_encoding中
            self.students_photos_encoding.append(face_recognition.face_encodings(img)[0])
            # 将读取到的照片的学生姓名存放在列表known_face_names中
            # 其中照片的文件名就是学生姓名，[:-4]是把后缀名去掉
            self.known_face_names.append(file_name[:-4])

    def CallBackFunctions(self):
        """控件回调函数"""
        self.pushButton_1.clicked.connect(self.Start_Sign_In)
        self.pushButton_2.clicked.connect(self.End_Sign_In)
        self.pushButton_3.clicked.connect(self.Current_Student_Attendance)
        self.pushButton_4.clicked.connect(self.Student_Information_Entry)
        self.pushButton_5.clicked.connect(self.Help)

        # 下面是用户界面中每一个按键的功能的具体实现：

    def Start_Sign_In(self):
        """开始签到"""
        # 打开摄像头
        self.video_capture = cv2.VideoCapture(0)
        if self.video_capture:
            # 如果启动正常，对用户界面中各个按键的可按/不可按进行修改
            self.pushButton_1.setEnabled(False)
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setEnabled(False)
            self.pushButton_5.setEnabled(False)
            # 设置视频窗口大小
            self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640 * 1.5)
            self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480 * 1.5)
            # 输出提示信息
            self.tips_browser.clear()
            self.tips_browser.append(" 正在打开您的摄像头......")
        else:
            # 输出提示信息
            self.tips_browser.clear()
            self.tips_browser.append(" ERROR! 您的摄像头无法打开！")
            return

        # 清空用于存储已经签到学生的姓名的列表
        self.attend_students_list = []
        # 清空用于存储已经签到学生的到达时间的列表
        self.attend_times_list = []
        # 输出提示信息
        self.tips_browser.clear()
        self.tips_browser.append(" 签到开始！")

        # 每隔1ms就调用一次self.Face_Recognition_Begin()方法
        self.Timer.start(1)

    def Face_Recognition_Begin(self):
        """开始人脸识别"""
        # 显示学生签到情况
        self.Current_Student_Attendance()

        # 抓取一帧视频
        ret, frame = self.video_capture.read()
        # 获取当前的时间
        now = int(round(time() * 1000))
        now2 = strftime('%Y-%m-%d  %a  %H:%M:%S', localtime(now / 1000))
        cv2.putText(frame, now2, (5, 25), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)
        # 将视频帧调整为1/2尺寸以加快人脸识别处理
        small_frame = cv2.resize(frame, (0, 0), fx=1 / 2, fy=1 / 2)

        # 查找当前视频帧中的所有面部和面部编码
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)
        # # face_recognition.face_locations()
        # # 其返回的是一个元组列表数据类型，即列表的每个元素（有多少个脸就有多少个）是一个元组，里面有4个元素
        # # 列表里每个元组的4个元素为人脸的四边位置(top, right, bottom, left)

        face_names = []
        for face_encoding in face_encodings:
            # 查看人脸是否与已知人脸匹配。返回值为True或False
            matches = face_recognition.compare_faces(self.students_photos_encoding, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(self.students_photos_encoding, face_encoding)
            # # compare_faces函数检测两张人脸是否能匹配，最后返回值只有True或False。
            # # 而如果想知道检测的两张人脸之间的相似度有多高，则可以使用使用face_distance函数，
            # # 该函数返回的是两个人脸特征向量间的欧氏距离，距离越小就说明两者越相似。
            # # 默认这个阈值为0.6，表示两张脸之间的距离在0.6以下才算匹配上，所以阈值设置得越小，那么对人脸检测的要求就越高。
            best_match_index = argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
                # 如果检测到一个学生来了，但是已签到学生列表(attend_students_list)里面还没有他的名字，则在已签到列表里面追加他的名字。
                # 并实时地在用户界面下方打印出刚刚签到的那位学生的到达时间（now2)和姓名(name)
                if name not in self.attend_students_list:
                    self.attend_students_list.append(name)
                    self.attend_times_list.append(now2)
                    self.tips_browser.clear()
                    self.tips_browser.append(" " + now2 + "\t" + name + "  签到成功！")

            face_names.append(name)

        # 把视频中的人脸用一个矩形框起来
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # 缩放用于框住人脸的矩形的位置。因为我们前面把视频帧缩为了1/2尺寸，在这里要把它还原回来。
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2
            # 在人脸上画一个空心矩形
            cv2.rectangle(frame, (left, top), (right, bottom), (250, 150, 0), 2)
            # 在人脸下方画一个实心矩形(为了好看一点)
            cv2.rectangle(frame, (left, bottom - 30), (right, bottom), (250, 150, 0), -1)

        # 将实时视频图像显示在用户界面上
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        q_img = array2qimage(img)  # 调用array2qimage函数将其转为QImage格式
        self.video_show_label.setPixmap(QPixmap(q_img))  # 再通过QPixmap函数转为QPixmap格式进行显示。
        self.video_show_label.show()  # 图像显示

    def End_Sign_In(self):
        """结束签到"""
        # 初始化用户界面的各个按键
        self.pushButton_1.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        # 清空视频窗口
        self.video_show_label.clear()
        # 在左边的显示视频的方框（self.video_show_label）显示背景图片
        bgp = QPixmap('background.jpg')
        self.video_show_label.setPixmap(bgp)
        # 输出提示信息
        self.tips_browser.clear()
        self.tips_browser.append(" 签到已结束！")
        # 释放摄像头
        self.video_capture.release()
        # 停止计时器
        self.Timer.stop()

    def Current_Student_Attendance(self):
        """学生签到情况"""
        # 清空右边的信息栏，并输出信息
        self.textBrowser.clear()
        self.textBrowser.append("[已签到学生名单]：")

        # 定义用于存储要显示的信息的列表
        sign_in_information_string = []

        # 下面的两个for in 循环是将学生姓名与签到时间两个字符串连接成一个字符串
        for attend_time in self.attend_times_list:
            sign_in_information_string.append(attend_time)

        i = 0
        for attend_name in self.attend_students_list:
            sign_in_information_string[i] = sign_in_information_string[i] + '\t' + attend_name
            i = i + 1

        # 将已签到学生姓名与签到时间两个信息一并输出
        for information_to_show in sign_in_information_string:
            self.textBrowser.append(information_to_show)

        self.textBrowser.append("\n[未签到学生名单]：")

        for name in self.known_face_names:
            if name not in self.attend_students_list:
                self.textBrowser.append(name)

    def Student_Information_Entry(self):
        """学生信息录入"""
        # 打开当前目录下的存放学生照片的“Students_Photos”文件夹
        system('explorer.exe /n, .\Students_Photos')

    def Help(self):
        """帮助"""
        # 清空右边的信息栏
        self.textBrowser.clear()
        # 定义要含有帮助信息的字符串
        text_of_help1 = "软件版本：\n刷脸签到2.0\n"
        text_of_help2 = "使用说明：\n该系统是基于实时人脸识别的一款签到系统。"
        text_of_help3 = "1、在使用前若没有录入过学生信息，应当先录入学生信息。具体操作如下：①点击“学生信息录入”，点击后会自动打开一个名为“Student_Photos”的文件夹；②将学生的照片都放置在该文件夹中，且照片的文件名为学生本人姓名；③录入完毕后重新启动该程序（只有重新启动后才会生效！）。"
        text_of_help4 = "2、录入学生信息后点击“开始签到”，即可开始刷脸签到。"
        text_of_help5 = "3、要结束签到，点击“结束签到”即可。\n"
        text_of_help6 = "最近更新：\n2019/12/6\n"
        text_of_help7 = "开发者：\n深圳大学 徐宇明\nwilliam87668@outlook.com"
        # 显示写有帮助信息的字符串
        self.textBrowser.append(text_of_help1)
        self.textBrowser.append(text_of_help2)
        self.textBrowser.append(text_of_help3)
        self.textBrowser.append(text_of_help4)
        self.textBrowser.append(text_of_help5)
        self.textBrowser.append(text_of_help6)
        self.textBrowser.append(text_of_help7)


# 运行程序
app = QApplication(argv)
ui = CamShow()
ui.show()
exit(app.exec_())
