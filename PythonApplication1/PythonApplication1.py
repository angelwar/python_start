from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("我的第一个GUI程序")
root.geometry("500x300+100+200")
bt = Button(root)
bt["text"] = "点我"
bt.pack()
def songhua(e): #e就是事件对象
    messagebox.showinfo("Message","送你一朵花，亲亲我吧")
    print("送你99朵玫瑰")
bt.bind("<Button-1>",songhua)
root.mainloop() #调用组件的mainLoop（）方法，进入事件循环
