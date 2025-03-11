# 关于ZouB
ZouB是在ZouC（发送端定制版本）的基础上改进的模块化呼叫器应用终端。其具有以下特点：
* PC端呼叫，方便快捷
* 无需定制，设置功能多
* 运行方便，适合老师使用
<mark>注意：初次使用本软件需要进行配置，详情请见《配置文件说明》！</mark>
## 运行设备基本配置需求
### Python源代码
* 搭载Python 3及以上的Windows/Mac/Linux设备。
**推荐：** 搭载Python 3.9及以上的Windows设备。
<mark>注意：Mac/Linux设备需要将主程序中由`os`执行的语句改由`subprocess`执行，并需要将附带应用重新通过`pyinstaller`打包。</mark>
### 可执行应用程序/应用安装程序
* 搭载Windows 10/11的Windows设备。
<mark>注意：Windows 7/8/8.1设备运行主程序会遇到以下报错：</mark>
```
无法启动此程序，因为计算机中丢失 api-ms-win-core-path-l1-1-0.dll。尝试重新安装该程序以解决此问题。
```