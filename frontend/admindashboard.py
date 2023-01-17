import tkinter
from tkinter import Tk, Label, TOP, BOTH, Frame, Button, Image, RIGHT
import Registrationpage

from PIL import ImageTk,Image
import driver_registration
import viewbooking
import assigndriver
from frontend import Loginpage


class admin_dashboard():
    def __init__(self,root):
        self.root=root
        self.root.resizable(0,False)
        self.root.state('zoomed')
        # self.root.title('Customer Page || Welcome {}'.format(Gobal.customerAcount[1]))
        self.root.config(bg='white')

################Heading###################
        lbl_heading = Label(self.root, text="Admin Dashboard", height=5, font=("Times New Roman", 20, "bold"),
                            bg="black", fg="white", padx=20)
        lbl_heading.pack(side=TOP, fill=BOTH)


        adimage = Image.open("C:\\Users\\dipesh\\Desktop\\adminimg (4).jpg")
        photo = ImageTk.PhotoImage(adimage)
        bg_panel = Label(self.root, image=photo)
        bg_panel.image = photo
        bg_panel.pack(fill='both', expand='yes')


        ##side frame
        menu_frame = Frame(self.root, bd=5, bg="yellow")
        menu_frame.place(x=0, y=680, width=1600, height=200)

###################ADD CUSTOMER#########################################################

        def addCustomer():
            window = tkinter.Toplevel()
            Registrationpage.Registration(window)
            window.mainloop()


        addcust_btn = Button(root, text="AddCustomer", font=("itallic", 15, "bold"),
                              bg="#A0A0A0", fg="black",command=addCustomer)
        addcust_btn.place(x=10, y=685, width=160, height=160)

###############ADD DRIVER#################################################################

        def addDriver():
            self.root.destroy()
            window=Tk()
            driver_registration.Registration(window)
            window.mainloop()

        adddriv_btn = Button(root, text="AddDriver",  font=("itallic", 15, "bold"), bg="#A0A0A0",
                               fg="black", command= addDriver)
        adddriv_btn.place(x=310, y=685, width=160, height=160)

#########################view booking##############################

        def viewbookingfunction():
            root=tkinter.Toplevel()
            viewbooking.ViewBooking(root)
            root.mainloop()
        viewbook_btn = Button(root, text="ViewBooking", font=("itallic", 15, "bold"),
                                 bg="#A0A0A0", fg="black", command=viewbookingfunction)
        viewbook_btn.place(x=710, y=685, width=160, height=160)

################ASSIGN BOOKING###################################

        def assigndriverfunction():
            self.root.destroy()
            root=Tk()
            assigndriver.AssignDriver(root)
            root.mainloop()
        assignbook_btn = Button(root, text="AssignDriver", font=("itallic", 15, "bold"),bg="#A0A0A0", fg="black", command=assigndriverfunction)
        assignbook_btn.place(x=1010, y=685,width=160, height=160)

############LOGOUT BUTTON########################################

        def logoutfunction():
            self.root.destroy()
            root = Tk()
            Loginpage.Login(root)
            root.mainloop()

        logout_btn = Button(root, text="Logout",  font=("itallic", 15, "bold"), bg="#A0A0A0",
                            fg="black", command=logoutfunction)
        logout_btn.place(x=1350, y=70, width=160, height=30)

        bg_panel.mainloop()



if __name__=='__main__':
    root=Tk()
    admin_dashboard(root)
    root.mainloop()

