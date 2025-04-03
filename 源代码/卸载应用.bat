@echo off
taskkill /F /IM ZouB3.4.3.exe
taskkill /F /IM ZouB接收服务V1.0.0.exe
taskkill /F /IM 日志读取器.exe
taskkill /F /IM 设置修改模块.exe
echo 已成功结束所有应用进程，可以开始卸载
pause
start unins000.exe