from cgitb import reset
from email.mime import application
from logging import root
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import time
import datetime
from datetime import datetime
import random
from numpy import pad
import backend
from tkinter import messagebox
import ttkthemes

class Resort:
    def __init__(self,root):
        self.root = root 
        self.root.title("Baculin InfoLog")
        self.root.geometry("1350x490+0+0")

        MainFrame = Frame(root)
        MainFrame.grid()

        TopFrame = Frame(MainFrame, bd=10, width=1350, height=550, padx=2, relief=RIDGE)
        TopFrame.pack(side=TOP)

        LeftFrame = Frame(TopFrame, bd=5, width=400, height=550, relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        RightFrame = Frame(TopFrame, bd=5, width=820, height=550, relief=RIDGE)
        RightFrame.pack(side=RIGHT)


        RightFrame1 = Frame(RightFrame, bd=5, width=800, height=50, padx=10, relief=RIDGE)
        RightFrame1.grid(row=0, column=0)

        RightFrame2 = Frame(RightFrame, bd=5, width=800, height=100, padx=3, relief=RIDGE)
        RightFrame2.grid(row=1, column=0)

        RightFrame3 = Frame(RightFrame, bd=5, width=800, height=400, padx=4, relief=RIDGE)
        RightFrame3.grid(row=3, column=0)

        BottomFrame = Frame(MainFrame, bd=10, width=1350, height=150, padx=2, relief=RIDGE)
        BottomFrame.pack(side=BOTTOM)
        #
        global cd
        CusID = StringVar()
        FirstName = StringVar()
        Lastname = StringVar()
        Contact = StringVar()
        CusAddress = StringVar()
        Room = StringVar()
        Status = StringVar() #Added Status

        NoOfDays = StringVar()
        AvailableRoom = StringVar()

        DateIn = StringVar()
        DateOut = StringVar()
        TotalDays = StringVar()

        DateIn.set(time.strftime("%d/%m/%Y"))
        DateOut.set(time.strftime("%d/%m/%Y"))

        rand = random.randint(1190, 8000)
        randomReference = str(rand)
        CusID.set(randomReference)

#==================================Button Functions============================================================
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("InfoLog", "Confirm if you want to exit.")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
                self.txtCusID.delete(0,END)
                self.txtFirstname.delete(0,END)
                self.txtSurname.delete(0,END)
                self.txtContact.delete(0,END)
                self.txtAddress.delete(0,END)
                self.txtCheckin.delete(0,END)
                self.txtCheckout.delete(0,END)
                
                self.ddmRoom.set("")

                DateIn.set(time.strftime("%d/%m/%Y"))
                DateOut.set(time.strftime("%d/%m/%Y"))

                rand = random.randint(1190, 8000)
                randomReference = str(rand)
                CusID.set(randomReference)
        #added the Names and Room number on database
        def add():
            if(len(CusID.get()) != 0):
                backend.addData(CusID.get(), FirstName.get(), Lastname.get(), Contact.get(), CusAddress.get(), Room.get(), DateIn.get(), DateOut.get(), Status.get())
                lstReso.delete(0,END)
                lstReso.insert(END, (CusID.get(), FirstName.get(), Lastname.get(), Contact.get(), CusAddress.get(), Room.get(), DateIn.get(), DateOut.get(), Status.get()))

        def deleteRec():
            if(len(CusID.get())!=0):
                backend.deleteData(cd[0])
                reset()
                tkinter.messagebox.showinfo("Baculin InfoLog", "Record deleted successfully.")
                display()              

        def display():

            lstReso.delete(0,END)
            for row in backend.viewData():
                lstReso.insert(END, row, str(""))

        def search():
                lstReso.delete(0,END)
                for row in backend.searchData(CusID.get(),FirstName.get(), Lastname.get(), Contact.get(), CusAddress.get(), Room.get(), DateIn.get(), DateOut.get()):
                        lstReso.insert(END,row,str(""))
        def update():

                if(len(CusID.get()) != 0):
                        backend.deleteData(cd[0])
                if(len(CusID.get()) != 0):
                        backend.addData(CusID.get(), FirstName.get(), Lastname.get(), Contact.get(), CusAddress.get(), Room.get(), DateIn.get(), DateOut.get(), Status.get())
                        lstReso.delete(0, END)
                        lstReso.insert(END, (CusID.get(), FirstName.get(), Lastname.get(), Contact.get(), CusAddress.get(), Room.get(), DateIn.get(), DateOut.get(), Status.get()))
                        tkinter.messagebox.showinfo("Baculin InfoLog", "Record updated successfully.")

        
        def records(root):
            global cd
            searchCdb = lstReso.curselection() [0]
            cd = lstReso.get(searchCdb)

            self.txtCusID.delete(0,END)
            self.txtCusID.insert(END,cd[0])
            self.txtFirstname.delete(0,END)
            self.txtFirstname.insert(END,cd[1])
            self.txtSurname.delete(0,END)
            self.txtSurname.insert(END,cd[2])
            self.txtContact.delete(0,END)
            self.txtContact.insert(END,cd[3])
            self.txtAddress.delete(0,END)
            self.txtAddress.insert(END,cd[4])
            self.ddmRoom.delete(0,END)
            self.ddmRoom.insert(END,cd[5])
            self.txtCheckin.delete(0,END)
            self.txtCheckin.insert(END,cd[6])
            self.txtCheckout.delete(0,END)
            self.txtCheckout.insert(END,cd[7])

        #algorithm to check input of the user
        def checkData(CusID, FirstName, Lastname, Contact, CusAddress, Room, DateIn, DateOut, Status):#gets the data from the input
                row=''
                #gets the data from the input
                #returns empty list or not
                rows=backend.getDataFromDatabase(CusID, FirstName, Lastname, Contact, CusAddress, Room, DateIn, DateOut, Status)

                #added here
                if rows =='RedudantCustomerNo':
                        messagebox.showerror("Error", "Redundant Customer No.")
                        Reset()
                        return True
                elif rows =='RoomTaken':
                        messagebox.showerror("Error", "Room Already Taken. Please Try Again")
                        Reset()
                        return True
                #if same name but different CustomerID, not allowed
                #CustomerName can renew his/her cusID if he/she already check-out then check-in again in other date
                
                elif rows==[]:
                        print("empty list")
                        print(row)
                        return False
                else:
                        print("Walang nangyari sadlyf")
                        return True       

        def addData():

                InDate = DateIn.get() 
                OutDate = DateOut.get()
                Indate = datetime.strptime(InDate, "%d/%m/%Y")
                Outdate = datetime.strptime(OutDate, "%d/%m/%Y")
                NoOfDays.set((Outdate - Indate).days)

                displayID = "Thank you for registering client data to the Baculin InfoLog. The client number is:" + str(CusID.get()) + ". Please provide the number to the client to serve as their identification number. \n\nData Details: \nClient Indentification Number:" + str(CusID.get()) + "\nClient First Name: "+ str(FirstName.get())+ "\nClient Last Name: "+ str(Lastname.get())+ "\nClient Contact:"+ str(Contact.get())+ "\nClient Address:"+ str(CusAddress.get())+ "\nClient Room:"+ str(Room.get())+ "\nCheck-in Date:"+ str(Indate)+ "\nCheck-out Date:"+ str(Outdate)

                #returns True or False if ther is a redudant data
                checkIfRedudantData=checkData(CusID.get(), FirstName.get(), Lastname.get(), Contact.get(), CusAddress.get(), Room.get(), InDate,OutDate, Status.get())



                #if there is redudant data    
                if checkIfRedudantData==True:
                        messagebox.showerror("Error", "Redudant Data")
                        print('Try Again')
                        return 
                        
                # if no redudant data from the checkData function, runs code below
                elif checkIfRedudantData==False:
                # added one tab (to redo just remove one tab) --puebla

                        if  (Outdate - Indate).days > 0:

                                tkinter.messagebox.showinfo("Baculin InfoLog", displayID)
                                NoOfDays.set((Outdate - Indate).days)
                                add()

                        elif (Outdate - Indate).days == 0:

                                lessthanday = tkinter.messagebox.askyesno("Baculin InfoLog", "Are you sure that the client will be staying for less than 24 hours?")

                                if lessthanday > 0:
                                        tkinter.messagebox.showinfo("Baculin InfoLog", displayID)
                                        NoOfDays.set((Outdate - Indate).days)
                                        add()
                                else:
                                        tkinter.messagebox.showinfo("Baculin InfoLog", "Record will not be added to the table.")
                                        return


                        elif (Outdate - Indate).days < 0:
                                tkinter.messagebox.showwarning("Baculin InfoLog", "Negative amount of days staying is not allowed.")
                                return


# #=======================================LEFT WIDGETS==================================================

        self.lblCusID = Label(LeftFrame, font=('arial', 18,'bold'), text="Baculin InfoLog", padx=1)
        self.lblCusID.grid(row=0, column=0, sticky =W)

        self.lblCusID = Label(LeftFrame, font=('arial', 12,'bold'), text="Customer No:", padx=1)
        self.lblCusID.grid(row=2, column=0, sticky =W)
        self.txtCusID =Entry(LeftFrame, font=('arial',12,'bold') ,width =18, textvariable=CusID)
        self.txtCusID.grid(row=2, column=1, pady=3, padx=20)

        self.lblFirstname = Label(LeftFrame, font=('arial', 12,'bold'), text="First Name:", padx=1)
        self.lblFirstname.grid(row=3, column=0, sticky =W)
        self.txtFirstname =Entry(LeftFrame, font=('arial',12,'bold') ,width =18, textvariable= FirstName)
        self.txtFirstname.grid(row=3, column=1, pady=3, padx=20)

        self.lblSurname = Label(LeftFrame, font=('arial', 12,'bold'), text="Surname:", padx=1)
        self.lblSurname.grid(row=4, column=0, sticky =W)
        self.txtSurname =Entry(LeftFrame, font=('arial',12,'bold') ,width =18, textvariable= Lastname)
        self.txtSurname.grid(row=4, column=1, pady=3, padx=20)

        self.lblContact = Label(LeftFrame, font=('arial', 12,'bold'), text="Contact No:", padx=1)
        self.lblContact.grid(row=5, column=0, sticky =W)
        self.txtContact =Entry(LeftFrame, font=('arial',12,'bold') ,width =18, textvariable= Contact)
        self.txtContact.grid(row=5, column=1, pady=3, padx=20)

        self.lblAddress = Label(LeftFrame, font=('arial', 12,'bold'), text="Address:", padx=1)
        self.lblAddress.grid(row=6, column=0, sticky =W)
        self.txtAddress =Entry(LeftFrame, font=('arial',12,'bold') ,width =18, textvariable= CusAddress)
        self.txtAddress.grid(row=6, column=1, pady=3, padx=20)

        self.lblRoom = Label(LeftFrame, font=('arial', 12,'bold'), text="Room No:", padx=1)
        self.lblRoom.grid(row=7, column=0, sticky =W)
        self.ddmRoom = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 12,'bold'), width=16, textvariable=Room)
        self.ddmRoom ['value'] = ('', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        self.ddmRoom.current(0)
        self.ddmRoom.grid(row=7, column=1, pady=3, padx=20)

        self.lblCheckin = Label(LeftFrame, font=('arial', 12,'bold'), text="Check In Date:", padx=1)
        self.lblCheckin.grid(row=8, column=0, sticky =W)
        self.txtCheckin =Entry(LeftFrame, font=('arial',12,'bold') ,width =18, textvariable= DateIn)
        self.txtCheckin.grid(row=8, column=1, pady=3, padx=20)

        self.lblCheckout = Label(LeftFrame, font=('arial', 12,'bold'), text="Check Out Date:", padx=1)
        self.lblCheckout.grid(row=9, column=0, sticky =W)
        self.txtCheckout =Entry(LeftFrame, font=('arial',12,'bold') ,width =18, textvariable= DateOut)
        self.txtCheckout.grid(row=9, column=1, pady=3, padx=20)
        
        self.lblStatus = Label(LeftFrame, font=('arial', 12,'bold'), text="Status:", padx=1) #Added Status
        self.lblStatus.grid(row=10, column=0, sticky =W)
        self.ddmStatus = ttk.Combobox(LeftFrame, state='readonly', font=('arial', 12,'bold'), width=16, textvariable=Status)
        self.ddmStatus ['value'] = ('Check-in', 'Check-Out')
        self.ddmStatus.current(0)
        self.ddmStatus.grid(row=10, column=1, pady=3, padx=20)
#=======================================RIGHT WIDGETS==================================================
        
        self.lblLabel = Label(RightFrame1, font=('arial', 9,'bold'), padx=6, pady=10, text="Customer No\tFirstname\t Surname \t Contact No \t Address \t Room Num \tCheck In Date \t Check Out Date \tStatus")
        self.lblLabel.grid(row=0, column=0, columnspan=17)

        scrollbar= Scrollbar(RightFrame2)
        scrollbar.grid(row=0, column=0,sticky='ns')
        lstReso = Listbox(RightFrame2, width=103, height=14, font=('arial', 10, 'bold'), yscrollcommand= scrollbar.set)
        lstReso.bind('<<ListboxSelect>>', records)
        lstReso.grid(row=0, column=0, padx=7, sticky= 'nsew')
        scrollbar.config(command = lstReso.xview)

#=======================================RIGHT WIDGETS==================================================
        
        self.lblDays = Label(RightFrame3, font=('arial', 12,'bold'), text="No. of Days:", padx=2, pady=2)
        self.lblDays.grid(row=0, column=0, sticky =W)
        self.txtDays =Entry(RightFrame3, font=('arial',12,'bold') ,width =76, textvariable= NoOfDays)
        self.txtDays.grid(row=0, column=1, pady=3, padx=20)

#=======================================WIDGET BUTTONS==================================================

        self.btnTotalandAddData = Button(BottomFrame, bd=4, font=('arial', 16,'bold'),
        width=13, height=2, text='Add', command=addData).grid(row=0, column=0, padx =4,  pady=1)
        #<====0

        self.btnDisplay = Button(BottomFrame, bd=4, font=('arial', 16,'bold'),
        width=13, height=2, text='Display', command= display).grid(row=0, column=1, padx =4,  pady=1)

        self.btnDisplay = Button(BottomFrame, bd=4, font=('arial', 16,'bold'),
        width=13, height=2, text='Update', command= update).grid(row=0, column=2, padx =4,  pady=1)

        self.btnDelete = Button(BottomFrame, bd=4, font=('arial', 16,'bold'),
        width=13, height=2, text='Delete', command= deleteRec).grid(row=0, column=3, padx =4,  pady=1)

        self.btnSearch = Button(BottomFrame, bd=4, font=('arial', 16,'bold'),
        width=13, height=2, text='Search', command=search).grid(row=0, column=4, padx =4,  pady=1)

        self.btnReset = Button(BottomFrame, bd=4, font=('arial', 16,'bold'),
        width=13, height=2, text='Reset', command = Reset).grid(row=0, column=5, padx =4,  pady=1)

        self.btnExit = Button(BottomFrame, bd=4, font=('arial', 16,'bold'),
        width=13, height=2, text='Exit', command = iExit).grid(row=0, column=6, padx =4,  pady=1)                
                
        display()


if __name__=='__main__':
    root=Tk()
    application = Resort (root)
    root.mainloop()
        