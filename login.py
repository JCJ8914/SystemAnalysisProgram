from cgitb import text
import os
import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter
import ttkthemes
from ttkthemes import ThemedStyle
import project
from tkinter import ttk


root = Tk()
root.title("Login to Baculin InfoLog")
root.geometry("200x150+0+0")

def verification():
    con = sqlite3.connect("resort_client.db")
    cur = con.cursor()

    user = username.get()
    passcode = password.get()

    if(user == "" and passcode == "") :
        messagebox.showinfo("", "Blank entries are not allowed.")

    elif(username.get() == "admin" and password.get() == "adminpassword"):

        messagebox.showinfo("","Login successful.")
        os.system("project.py 1")
        root.destroy()

    else :
        messagebox.showwarning("","Incorrect credentials, please try again.")

def exit():
    exitfunction = tkinter.messagebox.askyesno("Login to Baculin InfoLog", "Are you sure you want to exit?")
    if exitfunction > 0:
        root.destroy()
        return

root.style = ThemedStyle()
root.style.set_theme("arc")

username = StringVar()
password = StringVar()

root.programtitle = ttk.Label( text="Baculin InfoLog")
root.programtitle.grid(row=0, column=0, sticky =W)

root.lblUsername = ttk.Label(text="Username:")
root.lblUsername.grid(row=2, column=0, sticky =W)
root.txtUsername =ttk.Entry(root, font=('arial',12) ,width =14, textvariable=username)
root.txtUsername.grid(row=2, column=1)

root.lblPassword = ttk.Label(text="Password:")
root.lblPassword.grid(row=3, column=0, sticky =W)
root.txtPassword =ttk.Entry(root, font=('arial',12) ,width =14, textvariable=password)
root.txtPassword.grid(row=3, column=1)
root.txtPassword.config(show="*")


root.btnLogin = ttk.Button(text='Login', command=verification).grid(row=5, column=0)

root.btnExit = ttk.Button(text='Exit', command=exit).grid(row=5, column=1)

root.mainloop()