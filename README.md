# 关于Ms Zou呼叫器系列项目
## 项目概述
本项目基于QOS=1的MQTT协议运行，旨在方便老师们对学生进行远程呼叫。本项目在宁波广济中心小学世纪苑校区的许多班级中投入使用，方便了老师们和学生们的远程沟通。
## 项目搭建配置
* 基于ESP32的主控板（用于接收端，例如盛思生产的掌控板）
* MQTT物联网服务器（基于QOS=1的协议，推荐使用DFRobot生产的UNIHIKER行空板，或在Windows上搭建服务器）
* 一台或多台搭载Windows10+系统的PC（发送端，老师们日常使用的设备，同样可以使用Mac或Linux系统，但要确保使用的系统可以运行由Python3.13和Pyinstaller 6.12.0打包的可执行文件，并且需要在.py源文件中修改部分涉及os库的代码改用subprocess执行并在Mac设备上重新使用Pyinstaller打包，Linux系统可直接运行Python源文件，同样需要进行一些修改）
* 一台或多台搭载Android 5+的设备（不支持iOS系统，同样作为接收端使用）
## 项目文件开源说明
本项目由多个部分构成，其程序提供方式说明如下：
### ZouE（ESP32接收端）
说明：接收端主要版本，分多个班级，主要提供测试端口版本以供示例。
* [x] 已在基于ESP32的掌控板上测试成功
#### 提供内容
* 基于MicroPython 2.3.1运行的.py源代码（请根据实际服务器IP以及班级端口对源代码进行修改）
* 使用Mind+编写的图形化源码（请前往[Mind+官网](https://mindplus.cc/)下载Mind+1.7.3及以上版本后对源码进行修改后烧录运行）
### ZouB（Ms Zou呼叫器应用终端模块化版）
说明：发送端模块化版本，使用Python3.13编写源代码，Pyinstaller6.12.0打包.exe可执行文件，InnoSetup6.3.3打包.exe可执行安装包文件。安装后，请打开根目录/设置文件夹，根据说明对.ZouSettings（纯文本文件）的初始设置进行修改。
* [x] 使用安装程序打包的完整应用已在未安装任何Python解释器的Windows10/11系统测试通过。
#### 提供内容
* 基于Python3.13.0编写的.py源代码
<mark>注意：</mark>源代码基于Windows编写，存在部分涉及os库的代码，若在Mac/Linux系统下运行本程序，请事先修改好源代码，将涉及os库的指令转由subprocess执行！
<mark>注意：</mark>源代码需要依赖第三方库运行，请在运行源代码前通过以下命令安装必要的依赖：
```
pip install -U siot
pip install -U pyinstaller
```
其中，Pyinstaller库将用于将源码打包为可执行文件，可以不安装。
* 使用Pyinstaller 6.2.0打包的Windows应用（提供.zip压缩文件）
您可将此文件解压到任意目录下，需要在运行前修改设置文件夹里的配置文件。
<mark>注意：</mark>本程序不支持在Windows 8.1/8/7/XP及更早期系统运行，若在低于Windows10以下的系统中运行，会遇到如下错误：
```
无法启动此程序,因为计算机中丢失 api-ms-win-core-path-l1-1-0.dll。尝试重新安装该程序以解决此问题。
```
* 基于InnoSetup 6.3.3打包的安装程序
和.zip压缩文件类似，根据提示操作，在设置文件夹中修改相关设置即可。
#### ZouM（Android发送端）
应用已在Android8/10/13系统下测试通过。
提供内容：
* .apk安装包文件
说明：请通过ADB等方式安装此应用。
<mark>注意：</mark>推荐有能力者使用ADB安装，部分厂商的Android设备可能会对直接侧载安装.apk文件进行限制，请支持我们。
ADB方式：
1. 前往[谷歌开发者平台](https://developer.android.google.cn/tools/releases/platform-tools)下载platform-tools
2. 为platform-tools配置环境变量。
3. 打开Android设备的开发者选项，打开”ADB调试“功能。
4. 通过数据线连接PC和Android设备，在Android设备的`USB连接方式`菜单中选择“传输文件”
5. PC端打开命令行，导航至应用所在的文件夹，如：`cd 'path/to/your/file'`
6. 输入命令`adb devices`，Android设备会出现提示，选择“确认”，再次输入`adb devices`
此时，应当出现以下提示：
```
List of devices attached
(设备名称)        device
```
输入以下命令：
```
adb install -r -d (文件名称).apk
```
命令行将会出现以下提示：
```
Performing Streamed Install
完成
```
7. 应用安装完成，可以运行应用。
<mark>注意：</mark>启动应用后，请完成基本设置。设置时需要填写服务器IP和验证密码。本应用所有确认密码均为：
<mark>PCDC-ZouA1</mark>
此密码用于防止意外修改设置项导致应用无法正常启动，请不要随意修改设置。
* 基于MIT App Inventor编写的.aia图形化源码
## MQTT搭建说明
本应用可以在基于QOS1的MQTT平台上运行。推荐使用DFRobot制作的SIot。请前往[DFRobot](https://mindplus.dfrobot.com.cn/dashboard)下载SIot。
## ZouB与ZouM的区别
|                  | ZouM | ZouB |
| ---------------- | ---- | ---- |
| 基本呼叫/接收功能 | √    | √    |
| 应用快速设置      | √    | √    |
| 模块化应用        | ×    | √    |

---
__Powered By PCDC__

![Uploading Logo.jpg…](ZouLogo)
