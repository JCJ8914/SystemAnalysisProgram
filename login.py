from cgitb import text
import os
from tkinter import *
from tkinter import messagebox
import tkinter
import project
import loginbackend

def verification():
    user = username.get()
    passcode = password.get()

    if(user == "" and passcode == "") :
        messagebox.showinfo("", "Blank Not allowed")

    elif(user == "admin" and passcode == "admin"):

        messagebox.showinfo("","Login successful.")
        os.system("project.py 1")
        root.destroy()
        
    else :
        messagebox.showwarning("","Incorrect credentials, please try again.")

def exit():
    exitfunction = tkinter.messagebox.askyesno("Login to InfoLog", "Are you sure you want to exit?")
    if exitfunction > 0:
        root.destroy()
        return


root = Tk()
root.title("Login to InfoLog")
root.geometry("350x150+0+0")

username = StringVar()
password = StringVar()

root.lblUsername = Label(font=('arial', 12, 'bold'), text="Username:", padx=1)
root.lblUsername.grid(row=0, column=0, sticky =W)
root.txtUsername =Entry(root, font=('arial',12) ,width =18, textvariable=username)
root.txtUsername.grid(row=0, column=1)

root.lblPassword = Label(font=('arial', 12, 'bold'), text="Password:", padx=1)
root.lblPassword.grid(row=1, column=0, sticky =W)
root.txtPassword =Entry(root, font=('arial',12) ,width =18, textvariable=password)
root.txtPassword.grid(row=1, column=1)
root.txtPassword.config(show="*")


root.btnLogin = Button(bd=2, font=('arial', 16, 'bold'),
width=10, height=2, text='Login', command=verification).grid(row=5, column=0)

root.btnExit = Button(bd=2, font=('arial', 16, 'bold'),
width=10, height=2, text='Exit', command=exit).grid(row=5, column=1)

root.mainloop()