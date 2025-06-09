from tkinter import *
from tkinter import ttk
from pandas import*

def 生成表格(无用参数):
    for col in 列表树['columns']:
        列表树.delete(col)

    列表树['columns']=源文件.columns.tolist()
    for col in 列表树['columns']:
        列表树.heading(col, text=col)
        列表树.column(col, anchor='center', width=100)

    for index,row in 源文件.iterrows():
        列表树.insert('', 'end', values=list(row))


root=Tk(className='LogReader')
root.iconphoto(True,PhotoImage(file='./Images/CSVLogo.png'))
root.state('zoomed')
列表树=ttk.Treeview(root)
列表树.pack(expand=True, fill='both')
列表树['show']='headings'

源文件=read_csv('历史记录.ZouLog', encoding='GBK')
生成表格(源文件)

root.mainloop()