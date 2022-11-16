from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("300x200")

def login():
    username=entry1.get()
    password=entry2.get()

    if (username=='' and password==''):
        messagebox.showinfo("", "Fill in blanks !!!")

    elif (username=="Qais" and password=="Ping"):
        messagebox.showinfo("","Login Sucessful")

    else:
        messagebox.showinfo("Wrong username and password")

global entry1
global entry2

Label(window,text="Username").place(x=20,y=20)
Label(window,text="Password").place(x=20,y=70)

entry1=Entry(window,bd=2)
entry1.place(x=140,y=20)

entry2=Entry(window,bd=2)
entry2.place(x=140,y=70)

Button(window,text="Login",command=login).place(x=100,y=120)


window.mainloop()