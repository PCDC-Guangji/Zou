'''
ZouB接受服务V1.0.0.2503LTS
状态：LTS
'''
import siot,time
from win10toast import ToastNotifier
from tkinter import messagebox
from datetime import datetime
with open('./设置/连接ID.ZouSettings','r',encoding='utf-8')as 连接ID文件:
    连接ID=连接ID文件.read()

with open('./设置/连接密码.ZouSettings','r',encoding='utf-8')as 连接密码文件:
    连接密码=连接密码文件.read()

with open('./设置/班级/接收端口.ZouSettings','r',encoding='utf-8')as 接收端口文件:
    接收端口=接收端口文件.read()

with open('./设置/接收用户名.ZouSettings','r',encoding='utf-8')as 接收用户名文件:
    接收用户名=接收用户名文件.read()

with open('./设置/IP.ZouSettings','r')as 地址文件:
    IP=地址文件.read()

def 接收消息(client, userdata, msg):
    消息文本=msg.payload.decode()
    消息列表=eval(消息文本)
    if 消息列表[0]==接收用户名:
        with open('历史记录.ZouLog','a+',encoding='gbk')as 历史记录文件:
            时间=str(datetime.now())
            历史记录文件.write('\n'+时间+','+消息列表[1]+','+消息列表[2])
        messagebox.showinfo(title=消息列表[1]+'新消息',message=消息列表[2])

siot.init(client_id="",server=IP,port=1883,user=连接ID,password=连接密码)
siot.connect()
siot.loop()
siot.set_callback(接收消息)
siot.getsubscribe(topic=接收端口)
提示气泡=ToastNotifier()
提示气泡.show_toast('提示','ZouB接收模块正在后台运行','./背景图片/logo.ico',20,True)
while 提示气泡.notification_active():
    time.sleep(0.1)