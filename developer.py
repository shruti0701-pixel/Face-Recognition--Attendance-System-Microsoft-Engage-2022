from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoginition System")

        title_lbl = Label(self.root,text="Developed By!!",font=("times new roman",30,"bold"),bg="white",fg="Black")
        title_lbl.place(x=0,y=0,width=1280,height=53)

        img_top= Image.open(r"collection_images\black_stdt.jpg")
        img_top= img_top.resize((1280,1550) , Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_lbl = Label(self.root,image=self.photoimg_top) 
        first_lbl.place(x=0,y=55,width=1280, height=1550)

        main_frame = Frame(first_lbl , bd = 2 , bg = "white")
        main_frame.place(x=400,y=70,width=500,height=400)

        img_in= Image.open(r"collection_images\shrutii.jpg")
        img_in= img_in.resize((200,150) , Image.ANTIALIAS)
        self.photoimg_in = ImageTk.PhotoImage(img_in)

        first_lbl1 = Label(main_frame,image=self.photoimg_in) 
        first_lbl1.place(x=270,y=20,width=200, height=150)

        title_lbl1 = Label(main_frame,text="Hii! I am Shruti!",font=("times new roman",10,"bold"),bg="white",fg="Black")
        title_lbl1.place(x=0,y=5)

        title_lbl2 = Label(main_frame,text="I am sophomore from Sathyabama University!",font=("times new roman",10,"bold"),bg="white",fg="Black")
        title_lbl2.place(x=0,y=30)

        title_lbl2 = Label(main_frame,text="Technologies used in this project are: ",font=("times new roman",10,"bold"),bg="white",fg="Blue")
        title_lbl2.place(x=0,y=65)

        title_lbl2 = Label(main_frame,text="1.Python , 2.OpenCV With Tkinter GUI & ",font=("times new roman",10,"bold"),bg="white",fg="Black")
        title_lbl2.place(x=0,y=85)

        title_lbl2 = Label(main_frame,text="3.MySQL Database. ",font=("times new roman",10,"bold"),bg="white",fg="Black")
        title_lbl2.place(x=0,y=105)

        title_lbl2 = Label(main_frame,text="Algorithms Used: ",font=("times new roman",10,"bold"),bg="white",fg="Blue")
        title_lbl2.place(x=0,y=145)

        title_lbl2 = Label(main_frame,text="1.Haar Cascade Opencv (object/face Detection)",font=("times new roman",10,"bold"),bg="white",fg="Black")
        title_lbl2.place(x=0,y=160)

        title_lbl2 = Label(main_frame,text="2.LBPH algorithm (Face Recognition)",font=("times new roman",10,"bold"),bg="white",fg="Black")
        title_lbl2.place(x=0,y=180)

        title_lbl2 = Label(main_frame,text="Contact Me: shrutipaul2007@gmail.com",font=("times new roman",10,"bold"),bg="white",fg="red")
        title_lbl2.place(x=0,y=240)

        
if __name__ =="__main__":
    root = Tk()
    obj = Developer(root)

    root.mainloop()