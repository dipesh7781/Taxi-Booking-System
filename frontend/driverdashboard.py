from tkinter import *
from tkinter import ttk, messagebox

from backend import Gobal
from backend.bookingDBMS import drivernewbooking, driveroldbooking, completebooking
from backend.driverDBMS import driverstatusupdate
from frontend import Loginpage
from middleware.bookingMiddleware import booking
from middleware.driverMiddleware import Driver


class DriverDashboard():
    def __init__(self,driver):
        self.driver = driver
        self.driver.geometry("1100x700")
        self.driver.title("DriverDashboard")
        self.driver.config(bg="white")

        ################pannel###############

        lbl_heading = Label(self.driver, text="DriverDashboard", font=("Times New Roman", 20,"bold"), bg="#E5CCFF", fg="black",anchor="c", padx=20)
        lbl_heading.place(x=0, y=0, relwidth=1, height=60)

        didtxt= Entry(self.driver)
        didtxt.insert(0, Gobal.currentDriver[0])

        bidtxt = Entry(self.driver)

    #################labelframe1#################
        newtrip = LabelFrame(self.driver, font=("Times New Roman", 12, "bold"), bd=2, relief=SUNKEN, bg="white")
        newtrip.place(x=30, y=70, width=1050, height=250)
        newtrip_headinglbl= Label(newtrip, text="PendingTrip",font=("Times New Roman", 12, "bold"),bg="#FFCCE5",fg="black")
        newtrip_headinglbl.pack(side=TOP, fill=X)


    ##############labelframe2#################
        oldtrip = LabelFrame(self.driver, font=("Times New Roman", 12, "bold"), bd=2, relief=SUNKEN, bg = "white")
        oldtrip.place(x=30, y=330, width=1050, height=250)
        oldtrip_headinglbl = Label(oldtrip, text="Completed Trip", font=("Times New Roman", 12, "bold"), bg="#CCCCFF",fg="black")
        oldtrip_headinglbl.pack(side=TOP, fill=X)

        treeview = ttk.Treeview(newtrip, height=13)
        treeview.pack(side=BOTTOM, fill=BOTH)

        treeview['columns'] = ('bid', 'pickup_address', 'drop_address', 'pickup_time',
                               'pickup_date')

        treeview.column('#0', width=0, stretch=0)
        treeview.column('bid', width=100, anchor=CENTER)
        treeview.column('pickup_address', width=100, anchor=CENTER)
        treeview.column('drop_address', width=100, anchor=CENTER)
        treeview.column('pickup_time', width=100, anchor=CENTER)
        treeview.column('pickup_date', width=100, anchor=CENTER)

        treeview.heading('#0', text='', anchor=CENTER)
        treeview.heading('bid', text='Booking ID', anchor=CENTER)
        treeview.heading('pickup_address', text='Pickup', anchor=CENTER)
        treeview.heading('drop_address', text='Dropoff', anchor=CENTER)
        treeview.heading('pickup_time', text='Time', anchor=CENTER)
        treeview.heading('pickup_date', text='Date', anchor=CENTER)

        treeview1 = ttk.Treeview(oldtrip, height=13)
        treeview1.pack(side=BOTTOM, fill=BOTH)

        def getvalueintreeview():
            newbooking= booking(driverID=didtxt.get())
            drivernewbookingresult=drivernewbooking(newbooking)
            for row in drivernewbookingresult:
                treeview.insert(parent='', index='end', values=(row[0], row[1], row[2], row[5], row[4]))
        getvalueintreeview()




        treeview1['columns'] = ('bid', 'pickup_address', 'drop_address', 'pickup_time',
                               'pickup_date')

        treeview1.column('#0', width=0, stretch=0)
        treeview1.column('bid', width=100, anchor=CENTER)
        treeview1.column('pickup_address', width=100, anchor=CENTER)
        treeview1.column('drop_address', width=100, anchor=CENTER)
        treeview1.column('pickup_time', width=100, anchor=CENTER)
        treeview1.column('pickup_date', width=100, anchor=CENTER)

        treeview1.heading('#0', text='', anchor=CENTER)
        treeview1.heading('bid', text='Booking ID', anchor=CENTER)
        treeview1.heading('pickup_address', text='Pickup', anchor=CENTER)
        treeview1.heading('drop_address', text='Dropoff', anchor=CENTER)
        treeview1.heading('pickup_time', text='Time', anchor=CENTER)
        treeview1.heading('pickup_date', text='Date', anchor=CENTER)

        def getvalueintreeview1():

            driveroldbookingresult=driveroldbooking(didtxt.get())
            for x in driveroldbookingresult:
                treeview1.insert(parent='', index='end', values=(x[0], x[1], x[2], x[5], x[4]))
        getvalueintreeview1()

        def getdatafromtreeview(a):
            bidtxt.delete(0, END)
            selectitem = treeview.selection()[0]
            bidtxt.insert(0, treeview.item(selectitem)['values'][0])


        treeview.bind('<<TreeviewSelect>>', getdatafromtreeview)

        def completebookingfunction():
            completebookingresult=completebooking(bidtxt.get())
            assdriver = Driver(driverID=didtxt.get(), status='Available')
            driverstatusresult = driverstatusupdate(assdriver)
            if completebookingresult == True:
                messagebox.showinfo("TBS","Booking Completed")
                treeview.delete(*treeview.get_children())
                treeview1.delete(*treeview1.get_children())
                getvalueintreeview()
                getvalueintreeview1()
            else:
                messagebox.showerror("TBS", "Error Occurred!")

        complete_btn = Button(self.driver, text="Complete", font=("Times New Roman", 12, "bold"), bg="#FFFFCC", command=completebookingfunction)
        complete_btn.place(x=950, y=600)

        def logoutfunction():
            self.driver.destroy()
            root = Tk()
            Loginpage.Login(root)
            root.mainloop()

        logout_btn = Button(lbl_heading, text="Logout", font=("Times New Roman", 12, "bold"), bg="#FFFFCC", command=logoutfunction)
        logout_btn.place(x=950, y=15)









if __name__ == '__main__':
    driver = Tk()
    DriverDashboard(driver)
    driver.mainloop()



