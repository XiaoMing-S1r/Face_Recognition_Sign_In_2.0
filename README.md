# 效果展示
整体外貌效果：
![整体外貌效果](https://user-images.githubusercontent.com/57986069/155431634-363e0b90-4a51-4fb3-ae0f-a2adc7ed2e9a.png)

学生信息录入时的用户界面：
![学生信息录入时的用户界面](https://user-images.githubusercontent.com/57986069/155431698-e2c7bd39-6ac8-43b1-a893-5669b70ef2a3.png)

签到时的用户界面：
![签到时的用户界面-1](https://user-images.githubusercontent.com/57986069/155431713-ed44278e-bbda-4ab4-81eb-fbdfe6d9b699.png)
![签到时的用户界面-2](https://user-images.githubusercontent.com/57986069/155431723-0f18307f-9cae-409d-80d8-ebc94bfb1948.png)

签到结束时的用户界面：
![签到结束时的用户界面](https://user-images.githubusercontent.com/57986069/155431735-7376fa15-d155-48d0-bd9f-33e487491933.png)

签到结束后点击“学生签到情况”右侧文本框会显示图中内容（当然，在签到结束后也会自动显示）：
<div style="align: center">
<img src="https://user-images.githubusercontent.com/57986069/155431766-2b185b2d-d8b7-4fa9-b918-4be6e85f70d1.png"/>
</div>

点击“帮助”右侧文本框会显示图中内容：
<div style="align: center">
<img src="https://user-images.githubusercontent.com/57986069/155431800-197a3c7c-3c00-4f50-8c51-56b124775ba8.png"/>
</div>

# 使用说明
1.Face_Recognition_Sign_In.py是该项目的程序入口。
2.该项目文件夹存放的路径中不能有中文，否则会导致打包好的.exe应用程序无法运行。
3.dist文件夹是将.py源代码打包成.exe应用程序时生成的，点击 dist --> Face_Recognition_Sign_In --> Face_Recognition_Sign_In.exe 即可独立打开该项目程序（不需要打开python）。

# 实现方法
1.人脸识别签到的核心代码实现：
- 1.1	采集并录入学生照片：
此步我们将学生照片存放在该程序同一目录下的一个文件夹（Students_Photos）中，为了方便学生人脸与姓名的匹配，我们规定录入时照片的文件名即为该学生的姓名。
- 1.2加载学生照片并对其编码：
这一步是从存储了学生照片的文件夹中，通过Face_Recognition库逐张加载学生照片，并对其进行编码。
- 1.3调用摄像头实时地采集一帧帧的图像，并对采集到的图像中的人脸进行检测：
接下来是通过OpenCV库调用摄像头实时采集每一帧的图像，再通过Face_Recognition库在采集到的图像中把人脸挑出来，并对图像中挑出来的人脸进行编码。
- 1.4将实时采集到的人脸进行编码并与已知人脸库进行匹配：
最后是将摄像头实时采集到的每帧图像中的人脸，与已知学生人脸进行匹配。如果匹配成功，则表明这个学生来签到了。

2.用户界面的制作及各控件功能的实现
- 2.1用户界面整体外观的制作:
在制作用户界面之前，我们先下载Qt designer 和 PyUIC，并把它添加到pycharm的外部工具当中。然后打开Qt designer 后就可以开始用户界面的框架制作了，非常简单，直接拖动各种控件到工作区即可。
制作完成后保存即可，这时我们会发现当前目录下多了一个.ui文件，然后通过外部工具PyUIC，即可自动生成包含有用户界面中的各种类、控件等的.py文件。
- 2.2用户界面中各控件功能的具体实现：
此项内容比较多，但主要就是3类，一是初始化方法，二是控件的回调，三是用户界面中各项功能的具体实现。
（1）初始化方法
这里包括了程序启动时要进行初始化的内容，包括对The_classes_about_UI.py中类的继承，用户界面中控件的回调，初始化一些用于存储学生信息的变量（如存储已经签到的学生的列表，存储学生编码后的照片的列表等等），对用户界面的按键的可按/不可按进行初始化，以及计时器的定义（用于摄像头捕获连续一帧帧图像）。
（2）控件的回调
简单的说，就是当用户点击了某个控件后，程序就要自动地执行那个与此控件关联的方法。比如在用户界面点击了“开始签到”这个按钮，程序就要自动地执行实现“开始签到”这个功能的那个方法。
（3）用户界面中各项功能的具体实现
这一部分包含的方法比较多，每个方法都一一对应一种功能的具体实现。这些方法有“打开摄像头”，“开始人脸识别”，“结束签到”，“学生签到情况”，“学生信息录入”和“帮助”。最核心的“开始人脸识别”在上文（1.人脸识别签到的核心代码实现）中已有介绍，其他方法的实现不难，不在此再进行说明，具体实现请见文末项目源代码。

3.将.py源代码文件打包成.exe文件进行发布
我们将写好的.py源代码文件打包成.exe应用程序，这样程序就可以直接在其他机器（Windows操作系统的机器）上独立的运行了，十分方便。
这里我们用到了pyinstaller来将.py文件打包成.exe文件。首先我们打开命令提示符，进入到该程序所在的目录cd /d D:\Face_Recognition_Sign_In_2.0。然后输入pyinstaller -D -w -i logo.ico Face_Recognition_Sign_In.py，其中-D表示创建一个目录，包含.exe文件和依赖文件；-w表示在运行时不弹出命令提示符窗口；-i表示打包时包括应用程序图标（图标的文件名为logo.ico）；XXX.py表示要打包项目的主程序文件（这里是Face_Recognition_Sign_In.py）。之后，打包将会自动进行。
之后我们打开程序所在的目录，会发现多了2个文件夹，1个是“build”，1个是“dist”。“build”文件夹存放的是打包时用到的一些临时文件，这些文件对我们打包出来的.exe应用程序的运行无关，可以删去，“dist”文件夹中存放着我们打包好的.exe文件。



