from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Feature:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoginition System")

        title_lbl = Label(self.root,text="Features!!",font=("times new roman",30,"bold"),bg="white",fg="Black")
        title_lbl.place(x=0,y=0,width=1280,height=53)

        img_top= Image.open(r"collection_images\black_stdt.jpg")
        img_top= img_top.resize((1280,1550) , Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_lbl = Label(self.root,image=self.photoimg_top) 
        first_lbl.place(x=0,y=55,width=1280, height=1550)

        main_frame = Frame(first_lbl , bd = 2 , bg = "white")
        main_frame.place(x=400,y=70,width=500,height=400)

       # title_lbl1 = Label(main_frame,text="WELCOME BACK!!",font=("comicsansns 13 bold"),bg="white",fg="Green")
        #title_lbl1.place(x=0,y=5)

        title_lbl2 = Label(main_frame,text="The features that I have included in my project are:",font=("comicsansns 13 bold"),bg="white",fg="green")
        title_lbl2.place(x=0,y=20)

        title_lbl2 = Label(main_frame,text="1] Logging Security System (Username & Password)",font=("comicsansns 11 bold"),bg="white",fg="Black")
        title_lbl2.place(x=0,y=55)

        title_lbl2 = Label(main_frame,text="2]Real time face detection and recognition ",font=("comicsansns 11 bold"),bg="white",fg="Black")
        title_lbl2.place(x=0,y=75)

        title_lbl2 = Label(main_frame,text="3] Home Page:",font=("comicsansns 11 bold"),bg="white",fg="Black")
        title_lbl2.place(x=0,y=95)

        title_lbl2 = Label(main_frame,text="   -> Student management system (Save, Take Photo Samples, Update,)",font=("comicsansns 11 bold"),bg="white",fg="Black")
        title_lbl2.place(x=0,y=115)

        title_lbl2 = Label(main_frame,text="        Delete, Reset)",font=("comicsansns 11 bold"),bg="white",fg="Black")
        title_lbl2.place(x=0,y=135)

        title_lbl2 = Label(main_frame,text="   -> Train Photo Samples ",font=("comicsansns 11 bold"),bg="white",fg="Black")
        title_lbl2.place(x=0,y=155)

        title_lbl2 = Label(main_frame,text="   -> Take Attendance with Face Detection ",font=("comicsansns 11 bold"),bg="white",fg="Black")
        title_lbl2.place(x=0,y=175)

        title_lbl2 = Label(main_frame,text="   -> Attendance Report (Excel file & MySQL database)",font=("comicsansns 11 bold"),bg="white",fg="black")
        title_lbl2.place(x=0,y=195)

        title_lbl2 = Label(main_frame,text="   -> Developer Page",font=("comicsansns 11 bold"),bg="white",fg="black")
        title_lbl2.place(x=0,y=215)

        title_lbl2 = Label(main_frame,text="   -> Exit (from System)",font=("comicsansns 11 bold"),bg="white",fg="black")
        title_lbl2.place(x=0,y=235)

        title_lbl2 = Label(main_frame,text="                              THANK YOU!",font=("comicsansns 15 bold"),bg="white",fg="Green")
        title_lbl2.place(x=0,y=300)

if __name__ =="__main__":
    root = Tk()
    obj = Feature(root)
    root.mainloop()