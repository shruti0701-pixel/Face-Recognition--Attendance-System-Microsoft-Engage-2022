from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

#mydata = []
class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Panel")

        title_lbl = Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="grey",fg="black",bd=6,relief=GROOVE)
        title_lbl.place(x=0,y=0,width=1280,height=53)

        Back_Button=Button(title_lbl,text="Back",command=self.root.destroy,font=("arial",11,"bold"),width=17,bg="white",fg="red",bd=6,relief=GROOVE)
        Back_Button.pack(side=RIGHT)

        background = Image.open(r"C:\Users\shruti paul\Desktop\Final Project\collection_images\black_stdt.jpg")
        background = background.resize((1400 , 600) , Image.ANTIALIAS)
        self.photobackground = ImageTk.PhotoImage(background)

        bg_lbl = Label(self.root,image=self.photobackground) 
        bg_lbl.place(x=0,y=54,width=1400,height= 600)

        img_left= Image.open(r"collection_images\face-detection.jpg")
        img_left= img_left.resize((450,700) , Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        first_lbl = Label(self.root,image=self.photoimg_left) 
        first_lbl.place(x=0,y=55,width=450, height=700)

        img_right= Image.open(r"collection_images\smart-attendance.jpg")
        img_right= img_right.resize((550,700) , Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        first_lbl = Label(self.root,image=self.photoimg_right) 
        first_lbl.place(x=850,y=55,width=550, height=700)

       # b1_1 = Button(first_lbl,text="FACE RECOGNITION",command = self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="pink",fg="blue")
       # b1_1.place(x=210,y=495,width=230,height=50)
         
        b1_1 = Button(bg_lbl,text="FACE RECOGNITION",command = self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="pink",fg="blue",bd=5,relief=GROOVE)
        b1_1.place(x=530,y=250,width=230,height=50)

    #==========face recognition rounded button =========
        #img = Image.open(r"collection_images\rounded_image.jpg")
        #img = img.resize(100,60) , Image.ANTIALIAS #ANTIALIAS CONVERTS HIGH LEVEL LANGUAGE INTO LOW LEVEL LANGUAGE
        #self.photoimg = ImageTk.PhotoTk(img)
        #b1_1=Button(bg_lbl,image=self.photoimg,command = self.face_recog,cursor="hand2",borderwidth=0)
        #b1_1.place(x=530,y=250,width=230)





        #b1_1 = customtkinter.CTkButton(file="collection_images\rounded_image.jpg")
 # =================== ATTENDANCE ==========================
    def mark_attendance(self,l,i,j,k):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if ((l not in name_list)) and ((i not in name_list)) and ((j not in name_list)) and ((k not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{l}, {i}, {j},{k}, {dtString}, {d1}, Present")


    #=============== FACE RECOGNITION =====================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])

                confidence = int((100*(1-predict/300)))   #confidence formula as per the algorithm

                conn = mysql.connector.connect(host="localhost",username="root",password="shrutipaul*@))&",database="face-recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Roll_No from student where Reg_No=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                my_cursor.execute("select Name from student where Reg_No=" + str(id))
                j = my_cursor.fetchone()
                j = "+".join(j)

                my_cursor.execute("select Dept from student where Reg_No=" + str(id))
                k = my_cursor.fetchone()
                k= "+".join(k)

                my_cursor.execute("select Reg_No from student where Reg_No=" + str(id))
                l = my_cursor.fetchone()
                l = "+".join(l)       

                if confidence>79: #if confidence is more than image quality will also improve
                    cv2.putText(img,f"Reg_No:{l}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll_No:{i}",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{j}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dept:{k}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(l, i, j,k)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face" , (x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord = [x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade, 1.1,10,(255,255,255),"Face",clf)
            return img

#both detection and recognition has to be called in this module
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognization",img)

            if cv2.waitKey(1) == 13:   #Click on "ENTER" to close the window
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ =="__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()