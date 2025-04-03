from tkinter import*
from tkinter import messagebox,colorchooser
R=0
G=0
B=0
def 修改设置():
    if 密码认证.get()=='PCDC-ZouB':
        with open('设置/IP.ZouSettings', 'w', encoding='utf-8')as IP文件:
            IP文件.write(IP修改框.get())
        with open('设置/接收用户名.ZouSettings', 'w', encoding='utf-8')as 接收用户名文件:
            接收用户名文件.write(接收用户名.get())
        with open('设置/班级显示.ZouSettings', 'w', encoding='utf-8')as 班级显示文件:
            班级显示文件.write(str(
                [
                    班级1选择状态.get(),
                    班级2选择状态.get(),
                    班级3选择状态.get(),
                    班级4选择状态.get(),
                    班级5选择状态.get(),
                    班级6选择状态.get(),
                    班级7选择状态.get(),
                    班级8选择状态.get()
                ]
            ))
        with open('设置/RGB/R.ZouSettings', 'w', encoding='utf-8')as R文件:
            R文件.write(str(R))
        with open('设置/RGB/G.ZouSettings', 'w', encoding='utf-8')as G文件:
            G文件.write(str(G))
        with open('设置/RGB/B.ZouSettings', 'w', encoding='utf-8')as B文件:
            B文件.write(str(B))
        with open('设置/连接ID.ZouSettings', 'w', encoding='utf-8')as 连接ID文件:
            连接ID文件.write(连接ID.get())
        with open('设置/连接密码.ZouSettings', 'w', encoding='utf-8')as 连接密码文件:
            连接密码文件.write(连接密码.get())
        messagebox.showinfo(title='提示',message='设置修改成功，请重新启动主程序')
    else:
        messagebox.showinfo(title='错误',message='密码验证失败')

def 选择颜色():
    global R,G,B
    返回元组,确认选择=colorchooser.askcolor(title='选择颜色')
    if 确认选择:
        返回列表=list(返回元组)
        颜色值文本.config(text=str(返回列表))
        R=返回列表[0]
        G=返回列表[1]
        B=返回列表[2]

root=Tk(className='修改呼叫器设置')
IP提示文本=Label(root,text='服务器IP地址：')
IP提示文本.grid(row=0,column=0)
IP修改框=Entry(root)
IP修改框.grid(row=0,column=1)
连接ID提示文本=Label(root,text='连接ID')
连接ID提示文本.grid(row=0,column=2)
连接ID=Entry(root)
连接ID.grid(row=0,column=3)
连接密码提示文本=Label(root,text='连接密码')
连接密码提示文本.grid(row=0,column=4)
连接密码=Entry(root,show='*')
连接密码.grid(row=0,column=5)
颜色提示文本=Label(root,text='颜色：')
颜色提示文本.grid(row=1,column=0)
颜色修改按钮=Button(root,text='选择',command=选择颜色,width=20)
颜色修改按钮.grid(row=1,column=1)
颜色值文本=Label(root,text='未选择')
颜色值文本.grid(row=1,column=2)
接收用户名提示文本=Label(root,text='接收用户名：')
接收用户名提示文本.grid(row=2,column=0)
接收用户名=Entry(root)
接收用户名.grid(row=2,column=1)
班级1选择状态=IntVar()
班级1=Checkbutton(root,text='1班',variable=班级1选择状态)
班级1.grid(row=3,column=0)
班级2选择状态=IntVar()
班级2=Checkbutton(root,text='2班',variable=班级2选择状态)
班级2.grid(row=3,column=1)
班级3选择状态=IntVar()
班级3=Checkbutton(root,text='3班',variable=班级3选择状态)
班级3.grid(row=3,column=2)
班级4选择状态=IntVar()
班级4=Checkbutton(root,text='4班',variable=班级4选择状态)
班级4.grid(row=3,column=3)
班级5选择状态=IntVar()
班级5=Checkbutton(root,text='5班（测试）',variable=班级5选择状态)
班级5.grid(row=4,column=0)
班级6选择状态=IntVar()
班级6=Checkbutton(root,text='6班',variable=班级6选择状态)
班级6.grid(row=4,column=1)
班级7选择状态=IntVar()
班级7=Checkbutton(root,text='7班',variable=班级7选择状态)
班级7.grid(row=4,column=2)
班级8选择状态=IntVar()
班级8=Checkbutton(root,text='8班',variable=班级8选择状态)
班级8.grid(row=4,column=3)
密码认证=Entry(root,show='*')
密码认证.grid(row=5,column=0)
启动设置=Button(root,text='开始修改设置',width=20,command=修改设置)
启动设置.grid(row=5,column=2)
关于=Label(root,text='V1.1.0.2504\nPowered By PCDC')
关于.grid(row=5,column=1)
root.iconphoto(True, PhotoImage(file='./背景图片/FixLogo.png'))#Logo
root.resizable(False, False)#锁定窗口
root.mainloop()