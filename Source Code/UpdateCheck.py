"""
····························
■■■■■■··■■■■··■····■·■·····■
····■··■■■■■■·■····■·■·····■
···■···■■··■■·■····■·■··■··■
··■····■■··■■·■····■·■··■··■
·■·····■■■■■■·■■··■■·■··■··■
■■■■■■··■■■■··■·■■·■·■■■·■■■
····························
ZouW Update Check
Version 1.0

RV=Real Version
FV=Fake Version
"""
#import
from urllib.request import urlopen,urlretrieve
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser

#Value
URL='https://raw.githubusercontent.com/PCDC-Guangji/Zou/main/AppVersion.ZouInfo'

#def
def 忽略更新():
    with open('./Settings/Version/UpdateCheck.ZouVersion','w',encoding='utf-8')as 版本写入文件:
        版本写入文件.write(f"['{RV}','{最新版本号}']")
        messagebox.showinfo(title='忽略更新成功',message='重新打开更新检测程序后，操作将生效')

def 安装更新():
    webbrowser.open('https://github.com/PCDC-Guangji/Zou/releases')

#Read
with open('./Settings/Version/UpdateCheck.ZouVersion','r',encoding='utf-8')as 版本文件:
    版本字串=版本文件.read()
    版本列表=eval(版本字串)
    RV=版本列表[0]
    FV=版本列表[1]

#获取版本信息
try:
    ZouInfo文件=urlopen(URL)
    ZouInfo字串=ZouInfo文件.read().decode('utf-8')
    ZouInfo字典=eval(ZouInfo字串)
    最新版本号=ZouInfo字典['ZouW']
except Exception as 错误:
    messagebox.showerror(title='无法读取最新版本信息',message=f'对不起，我们无法读取ZouW的最新版本信息……\n可以检查一下这些问题：\n1.网络连接正常吗？\n2.能正常访问我们的GitHub仓库吗？\n也许，这条错误信息可以帮助问题排查：\n{错误}')
    最新版本号='未知'

#UI
root=Tk()
root.title('UpdateCheck')
root.configure(bg='white')
root.iconphoto(True,PhotoImage(file='./Images/ZouUpdateLogo.png'))
root.resizable(False, False)

ZouW图片=PhotoImage(file='./Images/ZouW.gif')
图片标签=Label(root,image=ZouW图片,bg='white')
图片标签.grid(row=0,column=1)
RV提示标签=Label(root,text='当前使用的版本为：',bg='white')
RV提示标签.grid(row=1,column=0)
RV标签=Label(root,text=RV,bg='white',fg='#33cc99')
RV标签.grid(row=1,column=2)
FV提示标签=Label(root,text=f'当前忽略的版本为：',bg='white')
FV提示标签.grid(row=2,column=0)
FV标签=Label(root,text=FV,bg='white',fg='orange')
FV标签.grid(row=2,column=2)
最新版本提示标签=Label(root,text='当前最新的版本为：',bg='white')
最新版本提示标签.grid(row=3,column=0)
最新版本标签=Label(root,text=最新版本号,bg='white',fg='purple')
最新版本标签.grid(row=3,column=2)
更新提示标签=Label(root,text='已有新版本ZouW',bg='white',fg='red')
忽略更新按钮=ttk.Button(root,text='忽略更新',command=忽略更新)
安装更新按钮=ttk.Button(root,text='安装更新',command=安装更新)

#版本判断
if 最新版本号!=RV and 最新版本号!=FV:
    更新提示标签.grid(row=4,column=1)
    忽略更新按钮.grid(row=5,column=0)
    安装更新按钮.grid(row=5,column=2)

root.mainloop()
