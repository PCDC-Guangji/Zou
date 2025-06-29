from tkinter import *
from tkinter import messagebox,ttk
import hashlib,time

#创建主窗口，完成初始设置
root=Tk()
root.title('ZouW设置修改工具')
root.iconphoto(True,PhotoImage(file='./Images/ZouWSLogo.png'))

def 开始设置():
    root.title('ZouW设置修改工具(正在修改配置文件)')
    time.sleep(1)
    #对设置项进行写入处理
    if hashlib.md5(设置密码输入框.get().encode('utf-8')).hexdigest()=='1c1f0afc0e4b99b0246f511253e3ec2f':
        try:
            with open('./Settings/Connect/IP.ZouSettings','w',encoding='utf-8')as IP修改文件:
                IP修改文件.write(ID输入框.get())
            with open('./Settings/Connect/ID.ZouSettings','w',encoding='utf-8')as ID修改文件:
                ID修改文件.write(IP输入框.get())
            with open('./Settings/Connect/Key.ZouSettings','w',encoding='utf-8')as 密码修改文件:
                密码修改文件.write(密码输入框.get())
            with open('./Settings/Topics/发送端口.ZouSettings','w',encoding='utf-8')as 发送修改文件:
                发送修改文件.write(发送输入框.get())
            with open('./Settings/Topics/接收端口.ZouSettings','w',encoding='utf-8')as 接收修改文件:
                接收修改文件.write(接收输入框.get())
            with open('./Settings/ClassName.ZouSettings','w',encoding='utf-8')as 班级名称修改文件:
                班级名称修改文件.write(班级名称输入框.get())
        except Exception as 错误:
            root.title('ZouW设置修改工具(设置错误)')
            messagebox.showerror(title='错误',message=错误+'\n请检查设置项是否有误！')
        else:
            root.title('ZouW设置修改工具(设置成功)')
            messagebox.showinfo(title='提示',message='设置成功！')
        finally:
            time.sleep(1)
            root.title('ZouW设置修改工具')
    else:
        messagebox.showerror(title='错误',message='设置密码错误，请检查设置密码！')

'''
文本读取区域
此区域用于读取原有设置项，从而实现文本框自动填充，全部使用'r'读取方法！
'''
with open('./Settings/Connect/IP.ZouSettings','r',encoding='utf-8')as IP文件:
    原IP=IP文件.read()
with open('./Settings/Connect/ID.ZouSettings','r',encoding='utf-8')as ID文件:
    原ID=ID文件.read()
with open('./Settings/Topics/发送端口.ZouSettings','r',encoding='utf-8')as 发送文件:
    原发送=发送文件.read()
with open('./Settings/Topics/接收端口.ZouSettings','r',encoding='utf-8')as 接收文件:
    原接收=接收文件.read()
with open('./Settings/ClassName.ZouSettings','r',encoding='utf-8')as 班级名称文件:
    原班级名称=班级名称文件.read()

'''
组件声明部分
此部分用于显示图形化页面
'''
IP提示文本=Label(root,text='服务器IP地址：')
IP提示文本.grid(row=0,column=0)
IP输入框=ttk.Entry(root)
IP输入框.insert(0,原IP)
IP输入框.grid(row=0,column=1)
ID提示文本=Label(root,text='连接ID：')
ID提示文本.grid(row=0,column=2)
ID输入框=ttk.Entry(root)
ID输入框.insert(0,原ID)
ID输入框.grid(row=0,column=3)
密码提示文本=Label(root,text='连接密码：')
密码提示文本.grid(row=0,column=4)
密码输入框=ttk.Entry(root,show='*')
密码输入框.grid(row=0,column=5)
发送提示文本=Label(root,text='发送端口：')
发送提示文本.grid(row=1,column=0)
发送输入框=ttk.Entry(root)
发送输入框.insert(0,原发送)
发送输入框.grid(row=1,column=1)
接收提示文本=Label(root,text='接收端口：')
接收提示文本.grid(row=1,column=2)
接收输入框=ttk.Entry(root)
接收输入框.insert(0,原接收)
接收输入框.grid(row=1,column=3)
设置密码提示文本=Label(root,text='设置密码：')
设置密码提示文本.grid(row=1,column=4)
设置密码输入框=ttk.Entry(root,show='*')
设置密码输入框.grid(row=1,column=5)
班级名称提示文本=Label(root,text='班级名称：')
班级名称提示文本.grid(row=2,column=0)
班级名称输入框=ttk.Entry(root)
班级名称输入框.insert(0,原班级名称)
班级名称输入框.grid(row=2,column=1)
设置图标=PhotoImage(file='./Images/Set.png')
开始设置按钮=ttk.Button(root,image=设置图标,command=开始设置)
开始设置按钮.grid(row=2,column=2)
警告信息=Label(root,text='警告：\n请在官方指导下使用设置程序，\n以免遇到ZouW无法使用的问题！',width=40,fg='#ff0000')
警告信息.grid(row=2,column=3)
关于=Label(root,text='Powered By PCDC',fg='#33cc99')
关于.grid(row=2,column=5)

root.mainloop()