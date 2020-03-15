import OCR
from tkinter import *
import tkinter.filedialog

result=''
img_path=''
root = Tk()
root.title('文字识别系统')
root.geometry('800x450')

#设置appid apikey secretky的缺省值
appid_v = tkinter.StringVar(value='17897236')
apikey_v = tkinter.StringVar(value='pDmRkoOlqUCQliqxm6wwp4sr')
secretkey_v = tkinter.StringVar(value='q24kqnZA0dZ1GvnaSAXBc09offm7GjfD')

#获取图片路径
def get_path():
    global img_path
    img_path = tkinter.filedialog.askopenfilename()

#图片转文字
def img_convert_str():
    global result,img_path
    appid_str=appid.get()
    apikey_str=apikey.get()
    secretkey_str=secretkey.get()
    result = OCR.img_to_str(img_path,appid_str,apikey_str,secretkey_str)
    result_text.insert(INSERT, result)

#获取识别模式
def get_model():
    OCR.model=var.get()

#主菜单
main_menu = Menu(root)
main_menu.add_command(label="打开图片",command=get_path)
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

label_1=tkinter.Label(root,text='更换API（可选）:')
label_1.place(relx=0.03,rely=0.8,relheight=0.05,relwidth=0.2)

#窗口底部放置三个标签
l_appid=tkinter.Label(root,text='AppID:')
l_appid.place(relx=0.05,rely=0.87,relheight=0.05,relwidth=0.1)
l_apikey=tkinter.Label(root,text='ApiKey:')
l_apikey.place(relx=0.35,rely=0.87,relheight=0.05,relwidth=0.1)
l_secretkey=tkinter.Label(root,text='SecretKey:')
l_secretkey.place(relx=0.65,rely=0.87,relheight=0.05,relwidth=0.1)

#窗口底部放置三个输入框
appid=tkinter.Entry(root,show = None,textvariable=appid_v)
appid.place(relx=0.15,rely=0.87,relheight=0.05,relwidth=0.2)
apikey=tkinter.Entry(root,show = None,textvariable=apikey_v)
apikey.place(relx=0.45,rely=0.87,relheight=0.05,relwidth=0.2)
secretkey=tkinter.Entry(root,show = None,textvariable=secretkey_v)
secretkey.place(relx=0.75,rely=0.87,relheight=0.05,relwidth=0.2)

#窗口底部放置一个按钮
trans_b=tkinter.Button(root,text='转换文字',command=img_convert_str)
trans_b.place(relx=0.85,rely=0.93 ,relheight=0.05,relwidth=0.1)
root.config(menu=main_menu)

root.mainloop()
