import OCR
from tkinter import *
import tkinter.filedialog

result=''

root = Tk()
root.title('文字识别系统')
root.geometry('800x450')

#获取图片路径
def img_convert_str():
    img_path = tkinter.filedialog.askopenfilename()
    global result
    result = OCR.img_to_str(img_path)
    result_text.insert(INSERT, result)

#获取识别模式
def get_model():
    OCR.model=var.get()

#主菜单
main_menu = Menu(root)
main_menu.add_command(label="打开图片",command=img_convert_str)
main_menu.add_command(label="退出",command=root.destroy)

var = tkinter.IntVar()
var.set(2)

r1=tkinter.Radiobutton(root,text="低精度",value=1,variable=var,command=get_model)
r1.pack()
r2=tkinter.Radiobutton(root,text="高精度",value=2,variable=var,command=get_model)
r2.pack()
r3=tkinter.Radiobutton(root,text="手写识别",value=3,variable=var,command=get_model)
r3.pack()

r1.place(relx=0,rely=0,relheight=0.1,relwidth=0.3)
r2.place(relx=0.3,rely=0,relheight=0.1,relwidth=0.3)
r3.place(relx=0.6,rely=0,relheight=0.1,relwidth=0.3)

result_text = Text(root,relief=SUNKEN)
result_text.place(relx=0.05,rely=0.1,relheight=0.7,relwidth=0.9)

root.config(menu=main_menu)

root.mainloop()
