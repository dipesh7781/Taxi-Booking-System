
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

from middleware.regex import namevalidation, emailvalidation, mobilevalidation
from middleware.userMiddleware import User
from backend.userDBMS import registration
from tkinter import messagebox

from frontend import Loginpage


class Registration():
    def __init__(self,window):
        self.window = window
        # self.window.geometry('1166x718')
        self.window.resizable(0,True)
        self.window.state('zoomed')
        self.window.title('Register Page')

        ###################Heading ##############################
        lbl_heading = Label(self.window, text="Customer Registration Page", height=2, font=("Times New Roman", 20, "bold"),
                            bg="black", fg="white", padx=20)
        lbl_heading.pack(side=TOP, fill=BOTH)



        # ============================Background Image===============================
        self.bg_frame=Image.open("C:\\Users\\dipesh\\Desktop\\register background.png")
        photo= ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel =Label(self.window,image=photo)
        self.bg_panel.image=photo
        self.bg_panel.pack(fill='both',expand='yes')

        ##side frame
        menu_frame = Frame(self.window, bd=0)
        menu_frame.place(x=0, y=70, width=390, height=690)

        image = Image.open("C:\\Users\\dipesh\\Desktop\\caucasian-man-with-suitcase-hitc.png")
        image = image.resize((1000, 1000))
        image = ImageTk.PhotoImage(image)
        Image_Label = Label(menu_frame, image=image)
        Image_Label.image = image
        Image_Label.place(x=0, y=0)

#========================Registration page label=======================


        self.Name_Label= Label(self.window,text="Full Name=",bg="#1C86EE",fg="Black", relief= RAISED,font=("Caliber",17,"bold"))
        self.Name_Label.place(x=500,y=120)

        self.Email_Label=Label(self.window,text="Email ID=", bg="#1C86EE", fg="Black", relief= RAISED, font=("Caliber",17,"bold"))
        self.Email_Label.place(x=500, y=200)

        self.Address_Label=Label(self.window, text="Address=", bg="#1C86EE",fg="Black",relief=RAISED,font=("Caliber",17,"bold"))
        self.Address_Label.place(x=500, y=280)

        # self.Gender_Label= Label(self.window, text="Gender=", bg="#1C86EE",fg="Black",relief=RAISED,font=("Caliber",17,"bold"))
        # self.Gender_Label.place(x=200, y=360)

        self.Contact_Label=Label(self.window,text="Phone Number=", bg="#1C86EE",fg="Black",relief=RAISED,font=("Caliber",17,"bold"))
        self.Contact_Label.place(x=1000, y=120)

        self.Password_Label=Label(self.window,text="password=", bg="#1C86EE",fg="Black",relief=RAISED,font=("Caliber",17,"bold"))
        self.Password_Label.place(x=1000,y=200)

        # self.Cabplate_Label=Label(self.window,text="Cab Number=", bg="#1C86EE",fg="Black",relief=RAISED,font=("Caliber",17,"bold"))
        # self.Cabplate_Label.place(x=800,y=280)
        #
        # self.Driverlic_Label=Label(self.window,text="Driver Licesense Number=", bg="#1C86EE",fg="Black",relief=RAISED,font=("Caliber",17,"bold"))
        # self.Driverlic_Label.place(x=800,y=360)

        self.gender_label=Label(self.window,text="Gender=",bg="#1C86EE",fg="Black",relief=RAISED,font=("Caliber",17,"bold"))
        self.gender_label.place(x=1000,y=280)


################################################EntryBoxes=========================================
############################################===============================######################

        Name_Box=Entry(self.window,highlightthickness=0,relief=RAISED,bg="#1C86EE", fg="Black",font=("yu gothic ui",15,"bold"))
        Name_Box.place(x=640, y=120, width=270)

        Email_Box=Entry(self.window,highlightthickness=0,relief=RAISED,bg="#1C86EE", fg="Black",font=("yu gothic ui",15,"bold"))
        Email_Box.place(x=640,y=200,width=270)

        Address_Box=Entry(self.window,highlightthickness=0,relief=RAISED,bg="#1C86EE", fg="Black",font=("yu gothic ui",15,"bold"))
        Address_Box.place(x=640,y=280,width=270)

        Contact_Box=Entry(self.window,highlightthickness=0,relief=RAISED,bg="#1C86EE", fg="Black",font=("yu gothic ui",15,"bold"))
        Contact_Box.place(x=1200,y=120,width=270)

        Password_box=Entry(self.window,highlightthickness=0,relief=RAISED,bg="#1C86EE", fg="Black",font=("yu gothic ui",15,"bold"))
        Password_box.place(x=1150,y=200,width=270)

######################################COMBOBOX #################################
################################################################################
        cmb_gender= ttk.Combobox(window, width=30, state='readonly')
        cmb_gender['values']= ('MALE', 'FEMALE', 'OTHERS')
        cmb_gender.current(0)
        cmb_gender.place(x=1129,y=280,height=30)


####################################Register and Login Button#####################
##################################################################################

        def register():

            name = namevalidation(Name_Box.get())
            email = emailvalidation(Email_Box.get())
            # contact = mobilevalidation(Contact_Box.get())

            if Name_Box.get() != '':
                if Email_Box.get() != '':
                    if Contact_Box.get() != '':
                        if name == True:
                            if email == True:
                                # if contact == True:
                                     user= User(userID='',name=Name_Box.get(),email=Email_Box.get(),contact_number=Contact_Box.get(),password=Password_box.get(),
                                                       gender=cmb_gender.get(),address=Address_Box.get())
                                     result=registration(user)
                                     if result==True:
                                            message1=messagebox.showinfo("Taxi Booking","Registration Successful")
                                     else:
                                        message2=messagebox.showerror("Taxi Booking","Registration Error")
                                # else:
                                #     messagebox.showerror("Taxi Booking", "Invalid contact number")
                            else:
                                messagebox.showerror("Taxi Booking", "Invalid email")
                        else:
                            messagebox.showerror("Taxi Booking", "Invalid Name")
                    # else:
                    #     messagebox.showerror("Taxi Booking", "Empty Contact field")
                else:
                    messagebox.showerror("Taxi Booking", "Empty email field")
            else:
                messagebox.showerror("Taxi Booking", "Empty name field")
        reg_btn= Button(window, width=10, text="Register",highlightthickness=5, relief=RAISED, font=("Times New Roman", 13, "bold underline"), bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='White',command=register)
        reg_btn.place(x=535, y=400)

        def reg():
            self.window.destroy()
            window=Tk()
            Loginpage.Login(window)
            window.mainloop()


        Login_btn=Button(window, text="Login",  font=("yu gothic ui", 13, "bold underline"), fg="White", relief=RAISED,
                                    activebackground="#3047ff" , borderwidth=0, background="#3047ff", cursor="hand2",command=reg)
        Login_btn.place(x=690,y=400,width=90)


class Registration_calling:
    def __init__(self):
        self.window = Tk()

    def registration_page(self):
        Registration(self.window)
        self.window.mainloop()

if __name__ == '__main__':
    # window=Tk()
    # Registration(window)
    # window.mainloop()
    obj = Registration_calling()
    obj.registration_page()