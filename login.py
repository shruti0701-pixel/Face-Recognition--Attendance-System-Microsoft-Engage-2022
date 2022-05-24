from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognitionsystem
from register import Register
import os

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

#========================variables ========================
        self.var_email=StringVar()
        self.var_pwd=StringVar()
        self.var_security=StringVar()
        self.var_securityans=StringVar()
        self.var_pwd=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"collection_images\login_background.jpg")
       
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        #================================
        img1 = Image.open(r"collection_images\school.jpg")
        img1 = img1.resize((560 , 130) , Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_lbl = Label(self.root,image=self.photoimg1) 
        first_lbl.place(x=400,y=0,width=560,height=130)


         #===================================
        frame1= Frame(self.root,bg="#002B53")        #002B53
        frame1.place(x=500,y=140,width=340,height=450)

        img1=Image.open(r"collection_images\login_icon1.jpg")
        img1=img1.resize((90,90),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        lb1img1.place(x=620,y=150, width=90,height=90)

        get_str = Label(frame1,text="Enter your Username and Password to access ",font=("times new roman",12,"bold"),fg="white",bg="#002B53")
        get_str.place(x=20,y=120)

        get_str = Label(frame1,text=" data panel....",font=("times new roman",12,"bold"),fg="white",bg="#002B53")
        get_str.place(x=130,y=140)

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)

         # Creating Button Login
        loginbtn=Button(frame1,text="Login",font=("times new roman",15,"bold"),command = self. login,bd=0,relief=RIDGE,fg="#002B53",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=320,width=270,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,text="New User Register",command=self.reg,font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=25,y=370,width=130,height=20)


        # Creating Button Forget command = self. login_button
        loginbtn=Button(frame1,text="Forgot Password",command = self. forgot_pwd,font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=145,y=370,width=130,height=20)

# this function is used open the register window.
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

#login button
    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Fields are Required!")
        #elif self.txtuser.get()=="shruti@123" and self.txtpwd.get()=="1234":
         #   messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        elif self.txtuser.get()!="shruti@123" or self.txtpwd.get()!="1234": #enter your username(email id) and password
            messagebox.showerror("Error","Please Check Username or Password !")
        else:    
            #messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(host="localhost",username="root",password="shrutipaul*@))&",database="face-recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email = %s and password=%s",(
                                                                                    self.var_email.get(),
                                                                                    self.var_pwd.get()
                                                                                ))
            row = my_cursor.fetchone()
            if row != None:                                                                         
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                open_main = messagebox.askyesno("Yes/No","Login")
                if open_main>0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognitionsystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #=============================reset password =========================
    def reset_pass(self):
            if self.var_security.get()=="Select":
                messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
            elif(self.var_securityans.get()==""):
                messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
            elif(self.var_pwd.get()==""):
                messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
            else:
                conn = mysql.connector.connect(host="localhost",username="root",password="shrutipaul*@))&",database="face-recognizer")
                my_cursor = conn.cursor()
                query=("select * from register where email=%s and securityque=%s and securityans=%s")
                value=(self.txtuser.get(),self.var_security.get(),self.var_securityans.get())
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
                else:
                    query=("update register set password=%s where email=%s")
                    value=(self.var_pwd.get(),self.txtuser.get())
                    my_cursor.execute(query,value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info","Successfully Your password has been reset, Please login with new Password!",parent=self.root2)
                    self.root2.destroy()

    # =====================Forget window=========================================
    def forgot_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="shrutipaul*@))&",database="face-recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forgot Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                securitylabel =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                securitylabel.place(x=70,y=80)

                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_security,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Mother's Name","Your Favourite Sports","Your Favorite Animal")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_securityans,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)

            

if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()