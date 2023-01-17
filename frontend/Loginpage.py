from tkinter import *
from tkinter import messagebox

from PIL  import ImageTk, Image
import Registrationpage as rp
from middleware.userMiddleware import User
from backend.loginDBMS import login, login3, login2
from backend import Gobal
import Booking
from middleware.driverMiddleware import Driver
from middleware.adminMiddleware import Admin
from frontend import admindashboard
from frontend import driverdashboard

class Login:
    def __init__(self,window):
        self.window =window
        self.window.geometry('1166x718')
        self.window.resizable(0,False)
        self.window.state('zoomed')

        self.window.title('Login Page')

#==============Background Image===============
        self.bg_frame= Image.open('C:\\Users\\dipesh\\Desktop\\Taxibackground.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window,image=photo)
        self.bg_panel.image= photo
        self.bg_panel.pack(fill='both',expand='yes')

        #===========LoginFrame=============
        self.login_frame= Frame(self.window,bg='Black',width=950,height=600)
        self.login_frame.place(x=200,y=70)
        self.heading= Label (self.login_frame, text= "Login", font='caliber',bg="Red", fg='white', relief=RAISED).place (x=325,y=20,width=300,height=30)

#==================Image vector=======
        self.side_image = Image.open("C:\\Users\\dipesh\\Desktop\\login image.png")
        photo=ImageTk.PhotoImage(self.side_image)
        self.side_image_label= Label(self.login_frame,image=photo,bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5,y=180)

#=====================SIGN in lABEL============
        self.sign_in_Label=Label(self.login_frame,text="Sign In",bg="Black",fg="white",font=("yu gothic ui",17,"bold"))
        self.sign_in_Label.place(x=650,y=240)

#===============SIgn In Image===============================
        self.sign_in_image = Image.open("C:\\Users\\dipesh\\Desktop\\hyy.png")
        photo= ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_Label = Label(self.login_frame, image=photo,bg='#040405')
        self.sign_in_image_Label.image= photo
        self.sign_in_image_Label.place(x=620,y=130)
#================Username================
#========================================

        self.username_label= Label(self.login_frame,text="UserEmail",bg="#040405",fg="#bdb9b1" ,font=("yu gothic ui",15,"bold"))
        self.username_label.place(x=550,y=300)

        username_entry = Entry(self.login_frame, highlightthickness=0,relief=FLAT ,bg="#040405", fg="White",font=("yu gothic ui",13,"bold"))
        username_entry.place(x=580, y=335, width=270)
        self.username_line = Canvas(self.login_frame, width=280, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)

#=====================Username icon Image=================
        self.username_img =Image.open("C:\\Users\\dipesh\\Desktop\\username_icon.png")
        photo =ImageTk.PhotoImage(self.username_img)
        self.username_img_label=Label(self.login_frame,image=photo,bg='#040405')
        self.username_img_label.image =photo
        self.username_img_label.place(x=550,y=332)

#=========================PasswordLabel===============
        self.password_label=Label(self.login_frame,text="Password", bg="#040405", fg="white", font=("yu gothic ui",12,"bold"))
        self.password_label.place(x=550,y=380)

###########################Password Entry#############################
        self.password_entry =Entry(self.login_frame,highlightthickness=0,relief=FLAT,bg="#040405",fg="white",font=("yu gothic ui",12,"bold"),show="*")
        self.password_entry.place(x=580,y=416,width=244)
        self.password_line = Canvas(self.login_frame,width=300,height=2.0,bg="#bdb9b1",highlightthickness=0)
        self.password_line.place(x=550, y=440)

        # =========================Login Button=======================
        def loginfunction():
            user_login=User(email=username_entry.get(),password=self.password_entry.get())
            user1=login(user_login)

            driver_login = Driver(email=username_entry.get(), password=self.password_entry.get())
            driverresult=login3(driver_login)

            admin_login = Admin(email=username_entry.get(), password=self.password_entry.get())
            adminresult=login2(admin_login)

            if user1 != None:
                Gobal.customerAcount = user1
                messagebox.showinfo("TBS", "Welcome {}".format(username_entry.get()))
                self.window.destroy()
                root=Tk()
                Booking.Customer_dashboard(root)
                root.mainloop()
            elif driverresult != None:
                messagebox.showinfo("TBS", "Welcome {}".format(driverresult[1]))
                Gobal.currentDriver = driverresult
                self.window.destroy()
                driver=Tk()
                driverdashboard.DriverDashboard(driver)
                driver.mainloop()
            elif adminresult !=None:
                messagebox.showinfo("TBS", "Welcome {}".format(adminresult[1]))
                Gobal.currentAdmin = adminresult
                self.window.destroy()
                root = Tk()
                admindashboard.admin_dashboard(root)
                root.mainloop()

            else:
                messagebox.showerror("TBS", 'Wrong Username or Password')


        self.login_btn = Image.open("C:\\Users\\dipesh\\Desktop\\btn1.png")
        photo = ImageTk.PhotoImage(self.login_btn)
        self.login_btn_label = Label(self.login_frame, image=photo, bg='#040405')
        self.login_btn_label.image = photo
        self.login_btn_label.place(x=550, y=450)
        self.login = Button(self.login_btn_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=loginfunction)
        self.login.place(x=20, y=10)
        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        self.forgot_button = Button(self.login_frame, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#040405"
                                    , borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=630, y=510)

        # =========== Sign Up ==================================================
        self.sign_label = Label(self.login_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file="C:\\Users\\dipesh\\Desktop\\register.png")
        self.signup_button_label = Button(self.login_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405", command= self.open_signup_page)
        self.signup_button_label.place(x=670, y=555, width=111, height=35)

        #======================Password Image====================
        self.password_img=Image.open("C:\\Users\\dipesh\\Desktop\\password_icon.png")
        photo =ImageTk.PhotoImage(self.password_img)
        self.password_img_label = Label(self.login_frame, image=photo,bg='#040405')
        self.password_img_label =photo
        # self.password_img_label.place(x=550, y=414)


#============ show/hide password==========
        self.show_image = ImageTk.PhotoImage \
            (file= "C:\\Users\\dipesh\\Desktop\\show.png")

        self.hide_image = ImageTk.PhotoImage \
            (file="C:\\Users\\dipesh\\Desktop\\hide.png")

        self.show_button= Button(self.login_frame,image=self.hide_image,command=self.show,relief=FLAT,activebackground="white",borderwidth=0,background="white",cursor="hand2")
        self.show_button.place(x=860,y=420)

    def show(self):
        self.hide_button = Button(self.login_frame,image= self.hide_image,command=self.hide,relief=FLAT,activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860,y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button= Button(self.login_frame,image=self.show_image,command=self.show,relief=FLAT,activebackground="white"
                                ,borderwidth=0,background="white",cursor="hand2")
        self.show_button.place(x=860,y=420)
        self.password_entry.config(show='*')

    def open_signup_page(self):
        self.window.destroy()
        obj = rp.Registration_calling()
        obj.registration_page()


if __name__ == '__main__':
    window=Tk()
    Login(window)
    window.mainloop()

