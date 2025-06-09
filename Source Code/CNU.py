from tkinter import*
from tkinter import messagebox,ttk
import time,shutil

def 强制反卸载程序():
    messagebox.showwarning(title='注意',message='1.您可以通过访问官网重新获取卸载程序，请放心替换。\n2.如果您需要终止替换卸载程序，请不要关闭这个窗口，请按下<Ctrl+Shift+Esc>打开任务管理器，终止本进程。')
    root.title('CNU Tools(正在替换卸载程序)')
    shutil.copy2('unins000F.exe', 'unins000.exe')
    time.sleep(2)
    root.title('CNU Tools(操作完成)')
    messagebox.showinfo(title='提示',message='操作完成！')
    time.sleep(2)
    root.title('CNU Tools')
def 反卸载程序():
    messagebox.showwarning(title='注意',message='1.您可通过<恢复卸载程序>功能恢复卸载程序。\n2.如需要变为强制反卸载，请删除应用安装目录的<unins000.exe.bak>。\n3.为防止学生恢复卸载程序，建议您使用<强制反卸载>替换卸载程序。')
    root.title('CNU Tools(正在创建恢复程序)')
    time.sleep(1)
    shutil.move('unins000.exe', 'unins000.exe.bak')
    root.title('CNU Tools(正在替换卸载程序)')
    shutil.copy2('unins000F.exe', 'unins000.exe')
    time.sleep(1)
    root.title('CNU Tools(操作完成)')
    messagebox.showinfo(title='提示',message='操作完成！')
    time.sleep(2)
    root.title('CNU Tools')
def 恢复卸载程序():
    messagebox.showinfo(title='说明',message='此操作将恢复卸载程序，您可以重新替换卸载程序。')
    root.title('CNU Tools(正在恢复卸载程序)')
    time.sleep(1)
    try:
        shutil.move('unins000.exe.bak', 'unins000.exe')
    except:
        messagebox.showerror(title='错误',message='没有找到恢复程序，这可能是因为您使用了强制反卸载工具。如果确实需要卸载，请前往官网下载卸载程序。')
        root.title('CNU Tools(恢复错误)')
        time.sleep(2)
    else:
        messagebox.showinfo(title='提示',message='操作完成！')
        root.title('CNU Tools(恢复成功)')
        time.sleep(2)
    finally:
        root.title('CNU Tools')

def 关于():
    messagebox.showinfo(title='关于',message='CNU Tools（ZouW反卸载工具）\nV1.0.0.2505\tPowered By PCDC\nWeiBo：@PCDC-Zou')
root=Tk()
root.title('CNU Tools')
root.iconphoto(True, PhotoImage(file='Images/CNULogo.png'))#Logo
root.resizable(False, False)
菜单=Menu(root)
菜单.add_command(label='关于',command=关于)
root.config(menu=菜单)
强制反卸载按钮=ttk.Button(root,text='替换卸载程序，不保留原有卸载程序（推荐）',width=100,command=强制反卸载程序)
强制反卸载按钮.grid(row=0,column=0)
反卸载按钮=ttk.Button(root,text='替换卸载程序，但是保留卸载程序（可逆，但不推荐）',width=100,command=反卸载程序)
反卸载按钮.grid(row=1,column=0)
恢复卸载程序按钮=ttk.Button(root,text='恢复卸载程序（需要保留卸载程序）',width=100,command=恢复卸载程序)
恢复卸载程序按钮.grid(row=2,column=0)
说明=Label(root,text='本程序可以防止学生通过“控制面板”以及“设置”应用卸载ZouW，但是无法防止安全软件强制卸载本软件！\n卸载程序可以从我们的官网获得（但为防止学生操作，此处不提供链接）')
说明.grid(row=3,column=0)
root.mainloop()