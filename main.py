from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
#--------------------------
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendancemanage import Attendance
from developer import Developer 
from features import Feature


class Face_Recognitionsystem:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoginition System")

#title image
        img = Image.open(r"collection_images\facialrecognition.jpg")
        img = img.resize((1300 , 200) , Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        first_lbl = Label(self.root,image=self.photoimg) 
        first_lbl.place(x=0,y=0,width=1300,height=200)

#background image
        img2 = Image.open(r"collection_images\bg.jpg")
        img2 = img2.resize((1400 , 600) , Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_lbl = Label(self.root,image=self.photoimg2) 
        bg_lbl.place(x=0,y=200,width=1400,height= 600)

        title_lbl = Label(bg_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM ",bd = 5, relief=GROOVE,font=("times new roman",30,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1268,height=45) 

#===========time ==========
        def time():
                string = strftime('%H:%M:%S %p')
                lbl.config(text = string)
                lbl.after(1000,time)

        lbl = Label(title_lbl,font=("times new roman",10,"bold"),bg="white",fg="black")
        lbl.place(x=0,y=0,width=80,height=30)
        time()

#student image button
        img3 = Image.open(r"collection_images\studenticon.jpg")
        img3 = img3.resize((200 , 200) , Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg_lbl,image=self.photoimg3,command=self.student_details,cursor="hand2",bd=5,relief=GROOVE)
        b1.place(x=100,y=100,width=200,height= 200)

        b1_1 = Button(bg_lbl,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        b1_1.place(x=100,y=300,width=200,height=40)

#data Train
        img4 = Image.open(r"collection_images\train_data.jpg")
        img4 = img4.resize((200 , 200) , Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_lbl,image=self.photoimg4,cursor="hand2",command=self.train_data,bd=5,relief=GROOVE)
        b1.place(x=400,y=100,width=200,height=200)

        b1_1 = Button(bg_lbl,text="Train Images",cursor="hand2",command=self.train_data,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        b1_1.place(x=400,y=300,width=200,height=40)
        

#detect face button
        img5 = Image.open(r"collection_images\face_icon.jpg")
        img5 = img5.resize((200 , 200) , Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_lbl,image=self.photoimg5,cursor="hand2",command=self.face_data,bd=5,relief=GROOVE)
        b1.place(x=700,y=100,width=200,height=200)

        b1_1 = Button(bg_lbl,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        b1_1.place(x=700,y=300,width=200,height=40)

#attendance icon
        img6 = Image.open(r"collection_images\attendance_icon.jpg")
        img6 = img6.resize((200 , 200) , Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_lbl,image=self.photoimg6,cursor="hand2",command =self.attendance_data,bd=5,relief=GROOVE)
        b1.place(x=1000,y=100,width=200,height=200)

        b1_1 = Button(bg_lbl,text="Attendance Rep",cursor="hand2",command =self.attendance_data,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        b1_1.place(x=1000,y=300,width=200,height=40)


#Photos
        b2 = Button(bg_lbl,text="Images",cursor="hand2",command=self.open_img,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        b2.place(x= 100,y=370,width=200,height=40)

#Features
        b2 = Button(bg_lbl,text="Features",cursor="hand2",command=self.feature_data,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        b2.place(x= 400,y=370,width=200,height=40)
        
#Developer / Help Desk - Mail ID given
        b2 = Button(bg_lbl,text="Developed By",cursor="hand2",command=self.developer_data,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        b2.place(x= 700,y=370,width=200,height=40)
#Exit
        b2 = Button(bg_lbl,text="Exit",cursor="hand2",command=self.exitt,font=("times new roman",20,"bold"),bd=5,relief=GROOVE)
        b2.place(x= 1000,y=370,width=200,height=40)

    def open_img(self):
            os.startfile("data")
    
    def exitt(self):
            self.exitt = tkinter.messagebox.askyesno("Exit","Are your sure you want to Exit this project?",parent = self.root)
            if self.exitt > 0:
                    self.root.destroy()
            else:
                    return


#===================FUNCTIONS BUTTON====================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Developer(self.new_window)

    def feature_data(self):
        self.new_window = Toplevel(self.root)
        self.app=Feature(self.new_window)

if __name__ =="__main__":
    root = Tk()
    obj = Face_Recognitionsystem(root)
    root.mainloop()

