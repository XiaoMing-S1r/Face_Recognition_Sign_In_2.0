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

