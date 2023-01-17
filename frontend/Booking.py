from tkinter import *
from tkinter import ttk, messagebox
from backend.bookingDBMS import insertbooking, usertable, delete_booking, cust_update_booking
from PIL import ImageTk,Image
from tkcalendar import Calendar,DateEntry
from middleware.bookingMiddleware import booking
from backend import Gobal
from frontend import Loginpage

class Customer_dashboard():
    def __init__(self,root):
        self.root=root
        self.root.resizable(0,False)
        self.root.state('zoomed')
        self.root.title('Customer Page || Welcome {}'.format(Gobal.customerAcount[1]))
        self.root.config(bg='#4CBB17')

        customer_id = Entry(self.root)
        customer_id.insert(0, Gobal.customerAcount[0])

        booking_id = Entry(self.root)

#######################################Background Image################################
#######################################################################################

        small_frame=Frame(root,bg='#4CBB17',width=1800,height=200)
        small_frame.pack(side=TOP, fill=BOTH)

        cust_img=Image.open("C:\\Users\\dipesh\\PycharmProjects\\pythonProject\\Image\\customerdash.jpg")
        photo= ImageTk.PhotoImage(cust_img)
        cust_img_panel=Label(small_frame,image=photo)
        cust_img_panel.image=photo
        cust_img_panel.place(x=40, y=0)



        self.Header_label=Label(small_frame,text="Customer Dashboard",bg="#4CBB17",fg='Black',font=('yu gothic ui',20,'bold'))
        self.Header_label.place(x=550,y=10)

        def logoutfunction():
            self.root.destroy()
            root=Tk()
            Loginpage.Login(root)
            root.mainloop()

        logoutbtn = Button(small_frame, text='Logout', bg='green', activebackground='green', font=('yu gothic ui',20,'bold'), command=logoutfunction)
        logoutbtn.place(x=1400, y=50)

        next_frame = Frame(root)
        next_frame.pack(side= BOTTOM, fill=BOTH, expand=TRUE)

        self.Pickup_label=Label(next_frame,text="Pickup Location :",font=('yu gothic ui',20,'bold'))
        self.Pickup_label.place(x=20,y=150)
        #
        self.Dropoff_label=Label(next_frame,text="DropOff Location :",font=('yu gothic ui',20,'bold'))
        self.Dropoff_label.place(x=20,y=200)
        #
        self.PickupDate_Label=Label(next_frame,text="Pickup Date :",font=('yu gothic ui',20,'bold'))
        self.PickupDate_Label.place(x=20,y=250)
        #
        self.PickupTime_Label=Label(next_frame, text="Pickup Time :", font=('yu gothic ui',20,'bold'))
        self.PickupTime_Label.place(x=20, y=300)
        #
        cmb_Pickup = ttk.Combobox(next_frame, width=30, state='readonly',font=('yu gothic ui',12,'bold'))
        cmb_Pickup['values'] = ('Lagankhel', 'Gwarko', 'Koteswor','Baneswor','Kalanki')
        # cmb_Pickup.current(0)
        cmb_Pickup.place(x=250, y=160)
        #

        cmb_Dropoff =ttk.Combobox(next_frame,width=30,state='readonly',font=('yu gothic ui',13,'bold'))
        cmb_Dropoff['values']=('Kupondole','Pulchwok','Jwalakhel','Ratnapark','Thamel')
        # cmb_Dropoff.current(0)
        cmb_Dropoff.place(x=250,y=210)

        pickupdate = DateEntry(next_frame, bg="white", font=('yu gothic ui',13,'bold'))
        pickupdate.place(x=250, y=260)

        pickuptime = Entry(next_frame, bg='white', font=('yu gothic ui', 13,'bold'))
        pickuptime.place(x=250, y=310)

        def insertBooking12():
            bookingMiddleware1=booking(booking_ID='',pickup_Address=cmb_Pickup.get(),dropOff_Address=cmb_Dropoff.get(), booking_Status='pending',
                                       booking_Date=pickupdate.get(),pickup_Time=pickuptime.get(), userID=customer_id.get())
            result=insertbooking(bookingMiddleware1)
            if result==True:
                messagebox.showinfo("TBS","The Booking is requested")
                custable.delete(*custable.get_children())
                custdas()
            else:
                messagebox.showerror("TBS","Error Occurred")

        #
        request_button = Button(next_frame, text=' Request ', font=('yu gothic ui', 15,'bold'), relief=RAISED,command=insertBooking12)
        request_button.place(x=50, y=360)

        def cancelbooking():
            deleteResult=delete_booking(booking_id.get())
            if deleteResult==True:
                messagebox.showinfo("TBS","Record deleted")
                custable.delete(*custable.get_children())
                custdas()

            else:
                messagebox.showerror("TBS","Error")



        #
        cancel_button = Button(next_frame, text=' Cancel ',command=cancelbooking, font=('yu gothic ui', 15, 'bold'), relief=RAISED)
        cancel_button.place(x=180, y=360)

        def updatedriver():
            cust_edit= booking(pickup_Address=cmb_Pickup.get(),dropOff_Address=cmb_Dropoff.get(),booking_Date=pickupdate.get(),
                               pickup_Time=pickuptime.get(),booking_ID=booking_id.get())
            customerResult=cust_update_booking(cust_edit)
            if customerResult==True:
                msg1= messagebox.showinfo(
                    "Taxi Bookingn System","Update Successful")
                custable.delete(*custable.get_children())
                custdas()
            else:
                msg2=messagebox.showinfo("Taxi Booking System", "Error Occurred")

        #
        update_button = Button(next_frame, text=' Update ', font=('yu gothic ui', 15, 'bold'), relief=RAISED,command=updatedriver)
        update_button.place(x=300, y=360)



        custable = ttk.Treeview(next_frame)
        custable['columns']=('cid', 'pickup_address','drop_address', 'pickup_time', 'pickup_date', 'status')
        custable.column('#0',width=0, stretch=0)
        custable.column('cid', width=0, stretch=0)
        custable.column('pickup_address', width=195, anchor=CENTER)
        custable.column('drop_address', width=195, anchor=CENTER)
        custable.column('pickup_time', width=195, anchor=CENTER)
        custable.column('pickup_date', width=195, anchor=CENTER)
        custable.column('status', width=195, anchor=CENTER)


        custable.heading('#0', text='', anchor=CENTER)
        custable.heading('cid', text='', anchor=CENTER)
        custable.heading('pickup_address', text='Pickup Address', anchor=CENTER)
        custable.heading('drop_address', text='Dropoff Address', anchor=CENTER)
        custable.heading('pickup_time', text='Pickup Time', anchor=CENTER)
        custable.heading('pickup_date', text='Pickup Date', anchor=CENTER)
        custable.heading('status', text='Status', anchor=CENTER)

        custable.pack(side=RIGHT, fill=BOTH)

        def custdas():
           cuspending=usertable(customer_id.get())
           for row in cuspending:
               custable.insert(parent="", index='end', values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        custdas()

        # function to get the item from table
        def selectfromtable(s):
            booking_id.delete(0, END)
            cmb_Pickup.delete(0, END)
            cmb_Dropoff.delete(0, END)
            pickupdate.delete(0, END)
            pickuptime.delete(0, END)

            selectitem=custable.selection()[0]
            booking_id.insert(0, custable.item(selectitem)['values'][0])
            cmb_Pickup.insert(0, custable.item(selectitem)['values'][1])
            cmb_Dropoff.insert(0, custable.item(selectitem)['values'][2])
            pickupdate.insert(0, custable.item(selectitem)['values'][4])
            pickuptime.insert(0, custable.item(selectitem)['values'][3])

        custable.bind('<<TreeviewSelect>>',selectfromtable)



if __name__=='__main__':
    root=Tk()
    Customer_dashboard(root)
    root.mainloop()

