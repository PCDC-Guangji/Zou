from tkinter import*
from tkinter import messagebox,colorchooser
R=0
G=0
B=0
def 选择颜色():
    global R,G,B
    返回元组,确认选择=colorchooser.askcolor(title='选择颜色')
    if 确认选择:
        返回列表=list(返回元组)
        颜色值文本.config(text=返回列表)

root=Tk(className='修改呼叫器设置')
IP提示文本=Label(root,text='服务器IP地址：')
IP提示文本.grid(row=0,column=0)
IP修改框=Entry(root)
IP修改框.grid(row=0,column=1)
颜色提示文本=Label(root,text='颜色：')
颜色提示文本.grid(row=1,column=0)
颜色修改按钮=Button(root,text='选择',command=选择颜色)
颜色修改按钮.grid(row=1,column=1)
颜色值文本=Label(root,text='未选择')
颜色值文本.grid(row=1,column=2)
root.mainloop()