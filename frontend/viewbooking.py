from tkinter import *
from tkinter import ttk

from backend.bookingDBMS import bookingtable56


class ViewBooking():
    def __init__(self, root):
        self.root=root
        self.root.title('All Booking')
        frame_width = 1000
        frame_height=550
        root.resizable(0,0)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width/2)-(frame_width/2))
        y_cordinate = int((screen_height/2)-(frame_height/2))
        root.geometry('{}x{}+{}+{}'.format(frame_width, frame_height, x_cordinate+120, y_cordinate))

        treeview = ttk.Treeview(root, height=15)
        treeview['columns'] = ('bid', 'pickupaddress', 'dropaddress', 'pickupdate', 'pickuptime')
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
        treeview.pack(side=BOTTOM, fill=BOTH,expand=2)

        def bookingtable():
            result56=bookingtable56()

            for x in result56:
                treeview.insert(parent='', index='end', values=(x[0],x[1],x[2],x[4],x[5]))
        bookingtable()





if __name__ =='__main__':
    root=Tk()
    ViewBooking(root)
    root.mainloop()