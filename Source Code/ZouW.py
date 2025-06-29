"""
····························
■■■■■■··■■■■··■····■·■·····■
····■··■■■■■■·■····■·■·····■
···■···■■··■■·■····■·■··■··■
··■····■■··■■·■····■·■··■··■
·■·····■■■■■■·■■··■■·■··■··■
■■■■■■··■■■■··■·■■·■·■■■·■■■
····························
Ms Zou呼叫器系列项目-ZouW
主程序
Powered By PCDC
Version1.0.0.2506B2
状态：公测Beta2

Bug Fix:
WB250611-01
"""

from tkinter import *
from tkinter import ttk,messagebox
from datetime import datetime
import pyttsx3
import siot,os

#文件读取
with open('Settings/Version/ZouW版本信息.ZouVersion', 'r', encoding='utf-8') as 版本信息文件:
    版本信息字符串 = 版本信息文件.read()
    版本信息列表 = eval(版本信息字符串)
    版本号 = 版本信息列表[0]
    状态 = 版本信息列表[1]
with open('Settings/Connect/IP.ZouSettings', 'r',encoding='utf-8')as IP文件:
    IP=IP文件.read()
with open('./Settings/Connect/ID.ZouSettings','r',encoding='utf-8')as ID文件:
    ID=ID文件.read()
with open('./Settings/Connect/Key.ZouSettings','r',encoding='utf-8')as 连接密码文件:
    连接密码=连接密码文件.read()
with open('./Settings/Topics/发送端口.ZouSettings','r',encoding='utf-8')as 发送文件:
    发送端口=发送文件.read()
with open('./Settings/Topics/接收端口.ZouSettings','r',encoding='utf-8')as 接收文件:
    接收端口=接收文件.read()
with open('./Settings/ClassName.ZouSettings','r',encoding='utf-8')as 班级名称文件:
    班级名称=班级名称文件.read()

#定义函数

#语音合成函数
def 语音合成(文本):
    合成对象=pyttsx3.init()
    合成对象.say(文本)
    合成对象.runAndWait()

def 反关闭():
    #此处防止学生乱动设备，专设反关闭函数
    pass

def 关于():
    #读取版本参数，获取版本信息并通过对话框形式出现
    messagebox.showinfo(
        title='关于ZouW',
        message=f'Ms Zou呼叫器Windows版\n版本号：{版本号}\n状态：{状态}'
    )

def 接收消息(client,userdata,msg):
    消息字串=msg.payload.decode()
    消息列表=eval(消息字串)
    消息窗口.deiconify()
    消息标签.config(state='normal')
    消息标签.delete(1.0,"end")
    颜色列表=[消息列表[1],消息列表[2],消息列表[3]]
    消息标签.tag_config('消息标签',foreground='#'+bytes(颜色列表).hex())
    消息标签.insert('insert',消息列表[0],'消息标签')
    消息标签.config(state='disabled')
    with open('历史记录.ZouLog','a',encoding='gbk')as 历史记录:
        历史记录.write(f'\n{datetime.now()},{消息列表[0]},{消息列表[1]},{消息列表[2]},{消息列表[3]}')
    for i in range(10):
        语音合成(消息列表[0])

def CNU():
    os.startfile('CNU.exe')

def 发送消息():
    #[教师,发送班级,消息]
    发送文本列表=[教师姓氏输入框.get(),班级名称,消息输入框.get()]
    siot.publish_save(topic=发送端口,data=发送文本列表)
    messagebox.showinfo(title='提示',message='消息发送完成')

def 修改设置():
    os.startfile('设置修改程序.exe')

def 查阅日志():
    os.startfile('LogReader.exe')

def 关闭消息窗口():
    消息窗口.withdraw()

def 检查更新():
    os.startfile('UpdateCheck.exe')

#主窗口
root=Tk()
root.title('Ms Zou呼叫器接收端')
#root.geometry('480x600')
root.iconphoto(True,PhotoImage(file='./Images/Logo.png'))#Logo
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW",反关闭)
root.attributes('-topmost', 1)#置顶

菜单=Menu(root)
工具菜单=Menu(菜单,tearoff=0)
工具菜单.add_command(label='设置',accelerator='Alt+S',command=修改设置)
工具菜单.add_command(label='查阅日志',accelerator='Alt+L',command=查阅日志)
工具菜单.add_command(label='检查更新',accelerator='Alt+U',command=检查更新)
工具菜单.add_command(label='CNU Tools',accelerator='Alt+N',command=CNU)
菜单.add_cascade(label='工具',menu=工具菜单)
菜单.add_command(label='关于',accelerator='Alt+A',command=关于)
root.bind('<Alt-Key-a>',lambda e:关于())
root.bind('<Alt-Key-n>',lambda e:CNU())
root.bind('<Alt-Key-s>',lambda e:修改设置())
root.bind('<Alt-Key-l>',lambda e:查阅日志())
root.bind('<Alt-Key-u>',lambda e:检查更新())
root.config(menu=菜单)

#组件布局区域
消息输入框=ttk.Entry(root)
消息输入框.insert(0,'请输入需要发送的消息')
消息输入框.grid(row=0,column=0)

教师姓氏输入框=ttk.Entry(root)
教师姓氏输入框.insert(0,'教师姓氏')
教师姓氏输入框.grid(row=0,column=1)

发送按钮=ttk.Button(root,text='发送',command=发送消息)
发送按钮.grid(row=0,column=2)

消息窗口=Toplevel()
消息窗口.title('新消息')
消息窗口.withdraw()
消息窗口.resizable(False, False)
消息窗口.attributes('-topmost', 1)
消息窗口.protocol("WM_DELETE_WINDOW",反关闭)
消息标签=Text(消息窗口)
消息标签.insert('end','暂无消息')
消息标签.config(state='disabled')
消息标签.pack()
消息关闭按钮=ttk.Button(消息窗口,text='关闭窗口',command=关闭消息窗口)
消息关闭按钮.pack()

'''
连接部分
说明：连接服务器，正常情况启动应用，连接失败自动启动设置服务
'''

siot.init('',IP,1883,ID,连接密码)
try:
    siot.connect()
    siot.loop()
    siot.set_callback(接收消息)
    siot.getsubscribe(接收端口)
except Exception as 错误:
    messagebox.showerror(title='连接错误',message=f'连接参数错误，将自动启动设置工具，请尝试修改设置！\n详细报错：\n{错误}')
    os.startfile('设置修改程序.exe')
else:
    #连接正常，开启MainLoop
    root.mainloop()
    消息窗口.mainloop()