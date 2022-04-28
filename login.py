import os
from tkinter import *
from tkinter import messagebox
import project

root = Tk()
root.title("Login to InfoLog")
root.geometry("250x125+0+0")

global username
global passcode

username = Entry(root)
username.grid(row=0, column=1)

passcode = Entry(root)
passcode.grid(row=1, column=1)
passcode.config(show="*")

def verification():
    user = username.get()
    password = passcode.get()

    if(user == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")

    elif(user == "admin" and password == "admin"):

        messagebox.showinfo("","Login successful.")
        os.system("project.py 1")
        root.destroy()
        

    else :
        messagebox.showwarning("","Incorrect credentials, please try again.")

Label(root, text="Username").grid(row=0, column=0)
Label(root, text="Password").grid(row=1, column=0)

Button(root, text="Login to InfoLog", command=verification ,height = 3, width = 13).place(x=10, y=50)

root.mainloop()