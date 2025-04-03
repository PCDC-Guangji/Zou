"""
ZouB项目（呼叫器应用终端模块化版）
版本：Version 3.4.3.2504LTS
状态：LTS
"""

#导入库
import siot,os
from tkinter import messagebox,ttk
from tkinter import*
from datetime import datetime

os.startfile('结束后台进程.bat')

#首次启动操作
with open('./认证.ZouSettings','r+',encoding='utf-8')as 启动验证文件:
    if 启动验证文件.read()=='':
        os.startfile('.\\ZouB3.4.3启动页.ppsx')
        启动验证文件.write('True')
#配置定义区域
#读取配置信息
with open('./设置/连接ID.ZouSettings','r',encoding='utf-8')as 连接ID文件:
    连接ID=连接ID文件.read()

with open('./设置/连接密码.ZouSettings','r',encoding='utf-8')as 连接密码文件:
    连接密码=连接密码文件.read()

with open('./设置/班级/接收端口.ZouSettings','r',encoding='utf-8')as 接收端口文件:
    接收端口=接收端口文件.read()

with open('./设置/接收用户名.ZouSettings','r',encoding='utf-8')as 接收用户名文件:
    接收用户名=接收用户名文件.read()

with open('./设置/班级/班级1.ZouSettings','r',encoding='utf-8')as 一班文件:
    一班文本=一班文件.read()
    一班列表=eval(一班文本)
    一班名称=一班列表[0]
    一班端口=一班列表[1]

with open('./设置/班级/班级2.ZouSettings','r',encoding='utf-8')as 二班文件:
    二班文本=二班文件.read()
    二班列表=eval(二班文本)
    二班名称=二班列表[0]
    二班端口=二班列表[1]

with open('./设置/班级/班级3.ZouSettings','r',encoding='utf-8')as 三班文件:
    三班文本=三班文件.read()
    三班列表=eval(三班文本)
    三班名称=三班列表[0]
    三班端口=三班列表[1]

with open('./设置/班级/班级4.ZouSettings','r',encoding='utf-8')as 四班文件:
    四班文本=四班文件.read()
    四班列表=eval(四班文本)
    四班名称=四班列表[0]
    四班端口=四班列表[1]

with open('./设置/班级/班级5.ZouSettings','r',encoding='utf-8')as 五班文件:
    五班文本=五班文件.read()
    五班列表=eval(五班文本)
    五班名称=五班列表[0]
    五班端口=五班列表[1]

with open('./设置/班级/班级6.ZouSettings','r',encoding='utf-8')as 六班文件:
    六班文本=六班文件.read()
    六班列表=eval(六班文本)
    六班名称=六班列表[0]
    六班端口=六班列表[1]

with open('./设置/班级/班级7.ZouSettings','r',encoding='utf-8')as 七班文件:
    七班文本=七班文件.read()
    七班列表=eval(七班文本)
    七班名称=七班列表[0]
    七班端口=七班列表[1]

with open('./设置/班级/班级8.ZouSettings','r',encoding='utf-8')as 八班文件:
    八班文本=八班文件.read()
    八班列表=eval(八班文本)
    八班名称=八班列表[0]
    八班端口=八班列表[1]

with open('./设置/IP.ZouSettings','r')as 地址文件:
    IP=地址文件.read()

def 设置开机自启():
    os.startfile('开机自启命令.bat')

def 启动后台服务():
    os.startfile('ZouB接收服务V1.0.0.exe')
    os.startfile('终止主进程服务.bat')

def 关于():
    messagebox.showinfo(title='关于',
                        message=f'ZouB项目（呼叫器应用终端模块化版）\n版本：Version 3.4.3.2504LTS\n状态：LTS\n所有教师：{接收用户名}')

def 修改设置():
    os.startfile('.\\附带应用\\设置修改模块.exe')

def 卸载应用():
    os.startfile('卸载应用.bat')

#设定颜色
with open('./设置/RGB/R.ZouSettings','r')as 红色值:
    R=int(红色值.read())
with open('./设置/RGB/G.ZouSettings','r')as 绿色值:
    G=int(绿色值.read())
with open('./设置/RGB/B.ZouSettings','r')as 蓝色值:
    B=int(蓝色值.read())

def 接收消息(client, userdata, msg):
    消息文本=msg.payload.decode()
    消息列表=eval(消息文本)
    if 消息列表[0]==接收用户名:
        with open('历史记录.ZouLog','a+',encoding='gbk')as 历史记录文件:
            时间=str(datetime.now())
            历史记录文件.write('\n'+时间+','+消息列表[1]+','+消息列表[2])
        messagebox.showinfo(title=消息列表[1]+'新消息',message=消息列表[2])

#发送消息函数
def 发送():
    消息=输入框.get()
    #侦测是否为空信息
    if len(消息)!=0:
        #侦测所选班级
        if 一班.get():
            siot.publish_save(topic=一班端口,data=[输入框.get(),R,G,B,接收用户名])
            messagebox.showinfo(title='提示',message=f'{一班名称}消息发送成功！')
        if 二班.get():
            siot.publish_save(topic=二班端口,data=[输入框.get(),R,G,B,接收用户名])
            messagebox.showinfo(title='提示',message=f'{二班名称}消息发送成功！')
        if 三班.get():
            siot.publish_save(topic=三班端口,data=[输入框.get(),R,G,B,接收用户名])
            messagebox.showinfo(title='提示',message=f'{三班名称}消息发送成功！')
        if 四班.get():
            siot.publish_save(topic=四班端口,data=[输入框.get(),R,G,B,接收用户名])
            messagebox.showinfo(title='提示',message=f'{四班名称}消息发送成功！')
        if 五班.get():
            siot.publish_save(topic=五班端口,data=[输入框.get(),R,G,B,接收用户名])
            messagebox.showinfo(title='提示',message=f'{五班名称}消息发送成功！')
        if 六班.get():
            siot.publish_save(topic=六班端口,data=[输入框.get(),R,G,B,接收用户名])
            messagebox.showinfo(title='提示',message=f'{六班名称}消息发送成功！')
        if 七班.get():
            siot.publish_save(topic=七班端口,data=[输入框.get(),R,G,B,接收用户名])
            messagebox.showinfo(title='提示',message=f'{七班名称}消息发送成功！')
        if 八班.get():
            siot.publish_save(topic=八班端口,data=[输入框.get(),R,G,B,接收用户名])
            messagebox.showinfo(title='提示',message=f'{八班名称}消息发送成功！')

#反之做出
    else:
        messagebox.showinfo(title='错误',message='不可发送空消息')

def 消息日志启动():
    os.startfile(r'.\\附带应用\\日志读取器.exe')

#主程序

root=Tk(className = '终端')
root.geometry('432x540')
root.iconphoto(True,PhotoImage(file='./背景图片/logo.png'))#Logo
root.resizable(False, False)#锁定窗口
root.protocol("WM_DELETE_WINDOW",启动后台服务)

底图=PhotoImage(file='./背景图片/UI.gif')
底图标签=Label(root,image=底图)#UI底图
底图标签.place(x=0,y=0,relwidth=1, relheight=1)

空行=Label(root,text='Ms Zou呼叫器应用终端',bg='white',height=2)
空行.pack(fill=X)

输入框=Entry(root)
输入框.pack()
发送按钮=ttk.Button(root, text='发送', command=发送, width=15)
发送按钮.pack()#放置输入区

#复选班级框
一班=IntVar()
一班框=ttk.Checkbutton(root, text=一班名称, variable=一班)

二班=IntVar()
二班框=ttk.Checkbutton(root, text=二班名称, variable=二班)

三班=IntVar()
三班框=ttk.Checkbutton(root, text=三班名称, variable=三班)

四班=IntVar()
四班框=ttk.Checkbutton(root, text=四班名称, variable=四班)

五班=IntVar()
五班框=ttk.Checkbutton(root, text=五班名称, variable=五班)

六班=IntVar()
六班框=ttk.Checkbutton(root, text=六班名称, variable=六班)

七班=IntVar()
七班框=ttk.Checkbutton(root, text=七班名称, variable=七班)

八班=IntVar()
八班框=ttk.Checkbutton(root,text=八班名称,variable=八班)

#顶部菜单
菜单=Menu(root)
菜单.add_command(label='关于',command=关于)
菜单.add_command(label='消息日志',command=消息日志启动)
菜单.add_command(label='修改设置',command=修改设置)
菜单.add_command(label='开机自启',command=设置开机自启)
菜单.add_command(label='卸载应用',command=卸载应用)
root.config(menu=菜单)

siot.init(client_id="",server=IP,port=1883,user=连接ID,password=连接密码)
siot.connect()
siot.loop()
siot.set_callback(接收消息)

siot.getsubscribe(topic=接收端口)

#根据配置文件决定订阅与显示
with open('./设置/班级显示.ZouSettings','r') as 配置文件:
    文本配置=配置文件.read()
    配置列表=eval(文本配置)
if 配置列表[0]:
    一班框.pack()
if 配置列表[1]:
    二班框.pack()
if 配置列表[2]:
    三班框.pack()
if 配置列表[3]:
    四班框.pack()
if 配置列表[4]:
    五班框.pack()
if 配置列表[5]:
    六班框.pack()
if 配置列表[6]:
    七班框.pack()
if 配置列表[7]:
    八班框.pack()

root.mainloop()
