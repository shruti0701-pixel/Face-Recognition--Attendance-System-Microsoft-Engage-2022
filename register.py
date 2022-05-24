from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")


        #============variables==============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security=StringVar()
        self.var_securityans=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()


        self.bg=ImageTk.PhotoImage(file=r"collection_images\register.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="#F2F2F2")
        frame.place(x=200,y=50,width=900,height=570)
        
        get_str = Label(frame,text="Registration",font=("times new roman",30,"bold"),fg="#002B53",bg="#F2F2F2")
        get_str.place(x=350,y=130)

        #label1 
        fname =lb1= Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=100,y=200)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold")) #textvariable=self.var_fname,
        self.txtuser.place(x=103,y=225,width=270)

        #label1 
        cnum =lb1= Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cnum.place(x=530,y=200)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold")) 
        self.txtuser.place(x=533,y=225,width=270)

        # ==================== section 2 -------- 2nd Columan===================

        #label2 
        contact =lb1= Label(frame,text="Contact No:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        contact.place(x=100,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold")) #textvariable=self.var_lname,
        self.txtpwd.place(x=103,y=295,width=270)

        


        #label2 
        email =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=530,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold")) #textvariable=self.var_email,
        self.txtpwd.place(x=533,y=295,width=270)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        security =lb1= Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        security.place(x=100,y=350)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_security,font=("times new roman",15,"bold"),state="readonly") #textvariable=self.var_security,
        self.combo_security["values"]=("Select","Your Mother's Name","Your Favourite Sports","Your Favorite Animal")
        self.combo_security.current(0)
        self.combo_security.place(x=103,y=375,width=270)


        #label2 
        securityans =lb1= Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        securityans.place(x=100,y=420)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_securityans,font=("times new roman",15,"bold")) #textvariable=self.var_securityans,
        self.txtpwd.place(x=103,y=445,width=270)

        # ========================= Section 4-----Column 2=============================

        #label1 
        pwd =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pwd.place(x=530,y=350)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pwd,font=("times new roman",15,"bold"))  #textvariable=self.var_pwd,
        self.txtuser.place(x=533,y=375,width=270)


        #label2 
        cpwd =lb1= Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cpwd.place(x=530,y=420)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpwd,font=("times new roman",15,"bold"))  #textvariable=self.var_cpwd,
        self.txtpwd.place(x=533,y=445,width=270)

        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),fg="#002B53",bg="#F2F2F2")
        checkbtn.place(x=100,y=480,width=270)  #variable=self.var_check,


        # Creating Button Register
        loginbtn=Button(frame,text="Register",command=self.register_data,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=103,y=510,width=270,height=35)  #command=self.reg,

        # Creating Button Login
        loginbtn=Button(frame,text="Login",command=self.back_to_login,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=533,y=510,width=270,height=35)

        #img1=Image.open(r"C:\Users\shruti paul\Desktop\Final Project\collection_images\rounded_image.jpg")
        #img1=img1.resize((90,90),Image.ANTIALIAS)
        #self.photoimage1=ImageTk.PhotoImage(img1)
        #loginbtn=Button(frame,font=("times new roman",15,"bold"),cursor="hand2",borderwidth=0)
        #loginbtn.place(x=533,y=510,width=270,height=35)

    def register_data(self):
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_security.get()=="Select" or self.var_securityans.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!")
        elif(self.var_check.get()==0):
            messagebox.showerror("Error","Please Check the Agree Terms and Conditons!")
        else:
            #messagebox.showinfo("Success","Welcome")
            conn = mysql.connector.connect(host="localhost",username="root",password="shrutipaul*@))&",database="face-recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_security.get(),
                                                                                        self.var_securityans.get(),
                                                                                        self.var_pwd.get()
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)

    def back_to_login(self):
        self.root.destroy()
                 
if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()


