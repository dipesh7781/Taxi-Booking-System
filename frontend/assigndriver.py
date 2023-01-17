from tkinter import *
from tkinter import ttk, messagebox
from backend import driverDBMS
from backend.bookingDBMS import bookingtable55, assigndriverupdate
from backend.driverDBMS import driverstatusupdate
from middleware.bookingMiddleware import booking
from middleware.driverMiddleware import Driver

class AssignDriver():
    def __init__(self, root):
        self.root = root
        self.root.title('All Booking')
        frame_width = 900
        frame_height = 500
        root.resizable(0, 0)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (frame_width / 2))
        y_cordinate = int((screen_height / 2) - (frame_height / 2))
        root.geometry('{}x{}+{}+{}'.format(frame_width, frame_height, x_cordinate + 120, y_cordinate))

        bid_frame = LabelFrame(root, text="Booking ID")
        bid_frame.place(x=10, y=10)

        bid_txt = Entry(bid_frame)
        bid_txt.pack()

        paddress_frame = LabelFrame(root, text='Pickup Address')
        paddress_frame.place(x=310, y=10)

        paddress_txt = Entry(paddress_frame)
        paddress_txt.pack()

        daddress_label = LabelFrame(root, text="Drop Address")
        daddress_label.place(x=610, y=10)

        daddress_txt1 = Entry(daddress_label)
        daddress_txt1.pack()

        date_label = LabelFrame(root, text="Pickup Date")
        date_label.place(x=10, y=120)

        date_txt = Entry(date_label)
        date_txt.pack()

        time_label = LabelFrame(root, text="Pickup Time")
        time_label.place(x=310, y=120)

        time_txt = Entry(time_label)
        time_txt.pack()

        driver_label = LabelFrame(root, text='Assign Driver')
        driver_label.place(x=610, y=120)

        def driverdata():
            result = driverDBMS.availabledriver111()
            data = [r for r, in result]
            driver_txt.config(values=data)
            driver_txt.pack()

        driver_txt = ttk.Combobox(driver_label)
        driverdata()


        def confirmbookingfunction():
            confirmbook = booking(booking_ID=bid_txt.get(), driverID=driver_txt.get())
            confirmbookingresult=assigndriverupdate(confirmbook)
            assdriver=Driver(driverID=driver_txt.get(), status='Unavailable')
            driverstatusresult=driverstatusupdate(assdriver)
            if confirmbookingresult==True:
                messagebox.showinfo("Taxi Booking", "Driver Assigned Successfully!!")
                treeview.delete(*treeview.get_children())
                bookingtable()
                driver_txt.delete(0, END)
                driverdata()
            else:
                messagebox.showerror("Taxi Booking", "Error Occurred!!")

        confirmbtn= Button(root, text='Confirm', font=('Times New Roman', 14, 'bold'), command=confirmbookingfunction)
        confirmbtn.place(x=800, y=120)

        treeview = ttk.Treeview(root, height=15)
        treeview['columns']=('bid','pickupaddress', 'dropaddress', 'pickupdate', 'pickuptime')
        treeview.column('#0', width=0, stretch=0)
        treeview.column('bid', width=100, anchor=CENTER)
        treeview.column('pickupaddress', width=100, anchor=CENTER)
        treeview.column('dropaddress', width=100, anchor=CENTER)
        treeview.column('pickupdate', width=100, anchor=CENTER)
        treeview.column('pickuptime', width=100, anchor=CENTER)

        treeview.heading('#0', text='', anchor=CENTER)
        treeview.heading('bid', text='Booking Id', anchor=CENTER)
        treeview.heading('pickupaddress', text='Pickup Address', anchor=CENTER)
        treeview.heading('dropaddress', text='Drop Address', anchor=CENTER)
        treeview.heading('pickupdate', text='Pickup Date', anchor=CENTER)
        treeview.heading('pickuptime', text='Pickup Time ', anchor=CENTER)
        treeview.pack(side=BOTTOM, fill=BOTH)

        def bookingtable():
            result=bookingtable55()

            for x in result:
                treeview.insert(parent='', index='end', values=(x[0],x[1],x[2],x[4],x[5]))

        bookingtable()

        def getdata(a):
            bid_txt.delete(0, END)
            paddress_txt.delete(0, END)
            daddress_txt1.delete(0, END)
            date_txt.delete(0, END)
            time_txt.delete(0, END)

            item=treeview.selection()[0]

            bid_txt.insert(0, treeview.item(item)['values'][0])
            paddress_txt.insert(0, treeview.item(item)['values'][1])
            daddress_txt1.insert(0, treeview.item(item)['values'][2])
            date_txt.insert(0, treeview.item(item)['values'][3])
            time_txt.insert(0, treeview.item(item)['values'][4])

        treeview.bind('<<TreeviewSelect>>', getdata)





if __name__ == '__main__':
    root = Tk()
    AssignDriver(root)
    root.mainloop()