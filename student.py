from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoginition System")

        #=================variables================
        self.var_Dept=StringVar()
        self.var_Course=StringVar()
        self.var_Year=StringVar()
        self.var_Sem=StringVar()
        self.var_Reg_No=StringVar()
        self.var_Roll_No=StringVar()
        self.var_Name=StringVar()
        self.var_Date=StringVar()
        self.var_Division=StringVar()
        
        #title image1
        img = Image.open(r"collection_images\black_stdt.jpg")
        img = img.resize((500 , 130) , Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        first_lbl = Label(self.root,image=self.photoimg) 
        first_lbl.place(x=0,y=0,width=500,height=130)
 
        #title img2
        img1 = Image.open(r"collection_images\school.jpg")
        img1 = img1.resize((500 , 130) , Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_lbl = Label(self.root,image=self.photoimg1) 
        first_lbl.place(x=400,y=0,width=500,height=130)

        #title image3
        img2= Image.open(r"collection_images\black_stdt.jpg")
        img2= img2.resize((550,130) , Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_lbl = Label(self.root,image=self.photoimg2) 
        first_lbl.place(x=900,y=0,width=550,height=130)

#background image
        img3 = Image.open(r"collection_images\bg.jpg")
        img3 = img3.resize((1400 , 600) , Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_lbl = Label(self.root,image=self.photoimg3) 
        bg_lbl.place(x=0,y=100,width=1400,height= 600)

        title_lbl = Label(bg_lbl,text="WELCOME TO STUDENT LOGIN PANEL",font=("verdana",30,"bold"),bg="white",fg="black",relief=GROOVE,bd=6)
        title_lbl.place(x=0,y=0,width=1268,height=45)


        main_frame = Frame(bg_lbl , bd = 2 , bg = "white")
        main_frame.place(x=5,y=50,width=1260,height=490)

        #left label frame

        Left_frame = LabelFrame(main_frame,bd=2,bg = "white",relief=RIDGE, text = "Student Details",font=("times new roman",12,"bold"))
        Left_frame.place (x= 6,y= 6,width= 600,height=580)


        img_left= Image.open(r"collection_images\studenticon.jpg")
        img_left= img_left.resize((500,130) , Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        first_lbl = Label(Left_frame,image=self.photoimg_left) 
        first_lbl.place(x=5,y=0,width=500, height=130)

        #current course
        curcourse_frame = LabelFrame(Left_frame,bd=2,bg = "white",relief=RIDGE, text = "Current Course Information",font=("times new roman",12,"bold"))
        curcourse_frame.place (x= 5,y=135,width=590,height=105)

        dep_lbl = Label(curcourse_frame,text="Department:",font=("times new roman",12,"bold"),bg="lightgreen",bd = 2,relief=GROOVE)
        dep_lbl.grid(row=0,column=0,padx=6)

        dep_combo = ttk.Combobox(curcourse_frame,textvariable=self.var_Dept,font=("times new roman",12),state="readonly")
        dep_combo["values"] = ("Select Department","BE" , "BTech","BSC","MSC")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=6,sticky=W)

        #course

        course_lbl = Label(curcourse_frame,text="Course:",font=("times new roman",12,"bold"),bg="lightgreen",bd = 2,relief=GROOVE)
        course_lbl.grid(row=0,column=2,padx=6,sticky=W)

        course_combo = ttk.Combobox(curcourse_frame,textvariable=self.var_Course,font=("times new roman",12),state="readonly")
        course_combo["values"] = ("Select Course","CSE" , "Mechanical" , "Electronics" , "Chemical")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=6,sticky=W)

        #year
        year_lbl = Label(curcourse_frame,text="Year:",font=("times new roman",12,"bold"),bg="lightgreen",bd = 2,relief=GROOVE)
        year_lbl.grid(row=1,column=0,padx=6,sticky=W)

        year_combo = ttk.Combobox(curcourse_frame,textvariable=self.var_Year,font=("times new roman",12),state="readonly")
        year_combo["values"] = ("Select Year","2020-2021" , "2021-2022" , "2022-2023" , "2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=6,sticky=W)

        #semester
        sem_lbl = Label(curcourse_frame,text="Semester:",font=("times new roman",12,"bold"),bg="lightgreen",bd = 2,relief=GROOVE)
        sem_lbl.grid(row=1,column=2,padx=6,sticky=W)

        sem_combo = ttk.Combobox(curcourse_frame,textvariable=self.var_Sem,font=("times new roman",12),state="readonly")
        sem_combo["values"] = ("Select Semester","1" , "2" , "3" , "4" , "5" , "6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=6,sticky=W)


        class_student_frame = LabelFrame(Left_frame,bd=2,bg = "white",relief=RIDGE, text = "Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place (x= 5,y=240,width=590,height=220)

        studid_lbl = Label(class_student_frame,text="Reg No:",font=("times new roman",12,"bold"),bg="lightgreen",bd = 2,relief=GROOVE)
        studid_lbl.grid(row=0,column=0,padx=2,pady=6,sticky=W)

        studid_entry = ttk.Entry(class_student_frame,textvariable=self.var_Reg_No,width=20,font=("times new roman",12,"bold"))
        studid_entry.grid(row=0,column=1,padx=2,pady=6,sticky=W)


        RegNo_lbl = Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="lightgreen",bd = 2,relief=GROOVE)
        RegNo_lbl.grid(row=0,column=2,padx=2,pady=6,sticky=W)

        RegNo_entry = ttk.Entry(class_student_frame,textvariable=self.var_Roll_No,width=20,font=("times new roman",12,"bold"))
        RegNo_entry.grid(row=0,column=3,padx=2,pady=6,sticky=W)

        Name_lbl = Label(class_student_frame,text="Name :",font=("times new roman",12,"bold"),bg="lightgreen",bd = 2,relief=GROOVE)
        Name_lbl.grid(row=2,column=0,padx=2,pady=6,sticky=W)

        Name_entry = ttk.Entry(class_student_frame,textvariable=self.var_Name,width=20,font=("times new roman",12,"bold"))
        Name_entry.grid(row=2,column=1,padx=2,pady=6,sticky=W)

        date_lbl = Label(class_student_frame,text="Date :",font=("times new roman",12,"bold"),bg="lightgreen",bd = 2,relief=GROOVE)
        date_lbl.grid(row=2,column=2,padx=2,pady=6,sticky=W)

        date_entry = ttk.Entry(class_student_frame,width=20,textvariable=self.var_Date,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=2,pady=6,sticky=W)

#Division 
        Division_lbl = Label(class_student_frame,text="Division :",font=("times new roman",12,"bold"),bg="lightgreen",bd = 2,relief=GROOVE)
        Division_lbl.grid(row=3,column=0,padx=2,pady=6,sticky=W)

        Division_combo = ttk.Combobox(class_student_frame,textvariable=self.var_Division,font=("times new roman",12),state="readonly",width=18)
        Division_combo["values"] = ("Select Division","A" , "B","C","D")
        Division_combo.current(0)
        Division_combo.grid(row=3,column=1,padx=2,pady=6,sticky=W)

#radio button
        self.var_radio1 = StringVar()
        radiobutton1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample" , value="Yes")
        radiobutton1.grid(row=4,column=0)
        
        radiobutton1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample" , value="No")
        radiobutton1.grid(row=4,column=1)

#button frame
        btn_frame =Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place (x=0,y=130,width=720,height=80)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",12,"bold"),bg="#F08080",fg="black") 
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update/Rectify",command = self.update_data,width=15,font=("times new roman",12,"bold"),bg="#20B2AA",fg="white") 
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command = self.delete_data,width=15,font=("times new roman",12,"bold"),bg="#F08080",fg="black") 
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command = self.reset_data,width=17,font=("times new roman",12,"bold"),bg="#20B2AA",fg="white") 
        reset_btn.grid(row=0,column=3)

        btn_frame1 =Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place (x=0,y=160,width=720,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command = self.generate_dataset,width= 65,font=("times new roman",12,"bold"),bg="#EEE0E5",fg="black") 
        take_photo_btn.grid(row=0,column=0)
        
        #right label frame

        Right_frame = LabelFrame(main_frame,bd=2,bg = "white",relief=RIDGE, text = "Student Details Data Stored",font=("times new roman",12,"bold"))
        Right_frame.place (x= 620,y= 6,width=630,height=580)

#============TABLE FRAME ==================== 
        table_frame =Frame(Right_frame,bd=2,bg = "white",relief=RIDGE)
        table_frame.place (x= 5,y=15,width=620,height=440) #145

        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("Dept","Course","Year","Sem","Reg_no","Roll_no","Name","Date","Division","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dept",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Sem")
        self.student_table.heading("Reg_no",text="Reg_no")
        self.student_table.heading("Roll_no",text="Roll_no")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Date",text="Date")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"] = "headings"

        self.student_table.column("Dept",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Reg_no",width=100)
        self.student_table.column("Roll_no",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Date",width=100)
        self.student_table.column("Division",width=100)
        self.student_table.column("Photo",width=150)



        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

#==================function declaration=============    
    def add_data(self):
            if self.var_Dept.get()=="Select Department" or self.var_Reg_No.get() == "" or self.var_Name.get() == "":
                    messagebox.showerror("Error","All fields are mandatory",parent = self.root)
            else:
                        try:
                                conn = mysql.connector.connect(host="localhost",username="root",password="shrutipaul*@))&",database="face-recognizer")
                                my_cursor = conn.cursor()
                                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_Dept.get(),
                                                                                                        self.var_Course.get(),
                                                                                                        self.var_Year.get(),
                                                                                                        self.var_Sem.get(),
                                                                                                        self.var_Reg_No.get(),
                                                                                                        self.var_Roll_No.get(),
                                                                                                        self.var_Name.get(),
                                                                                                        self.var_Date.get(),
                                                                                                        self.var_Division.get(),
                                                                                                        self.var_radio1.get()
                                                                                                        ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Sucess","Students details has been added Successfully",parent=self.root)

                        except Exception as es:
                                messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)

#=================== fetch data ======================  
    def fetch_data(self):
            conn = mysql.connector.connect(host="localhost",username="root",password="shrutipaul*@))&",database="face-recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            data = my_cursor.fetchall()

            if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                            self.student_table.insert("",END,values=i)
                    conn.commit()
            conn.close()

#=================== fetch data ====================== 
    def get_cursor(self,event=""):
            cursor_focus=self.student_table.focus()
            content = self.student_table.item(cursor_focus)
            data = content["values"]

            self.var_Dept.set(data[0]),
            self.var_Course.set(data[1]),
            self.var_Year.set(data[2]),
            self.var_Sem.set(data[3]),
            self.var_Reg_No.set(data[4]),
            self.var_Roll_No.set(data[5]),
            self.var_Name.set(data[6]),
            self.var_Date.set(data[7]),
            self.var_Division.set(data[8]),
            self.var_radio1.set(data[9])

#================== update data =========================
    def update_data(self):
            if self.var_Dept.get()=="Select Department" or self.var_Reg_No.get() == "" or self.var_Name.get() =="":
                    messagebox.showerror("Error","All fields are required",parent = self.root)
            else:
                    try:
                            Upadate=messagebox.askyesno("Update" , "Do you want to update student details",parent=self.root)
                            if Upadate>0:
                                    conn = mysql.connector.connect(host="localhost",username="root",password="shrutipaul*@))&",database="face-recognizer")
                                    my_cursor = conn.cursor()
                                    my_cursor.execute("update student set Dept=%s,Course = %s,Year = %s,Sem = %s,Roll_No = %s,Name = %s,Date = %s,Division = %s,Photo = %s where Reg_No = %s",(

                                                                                                                                                self.var_Dept.get(),
                                                                                                                                                self.var_Course.get(),
                                                                                                                                                self.var_Year.get(),
                                                                                                                                                self.var_Sem.get(),                                                                                                                                                
                                                                                                                                                self.var_Roll_No.get(),
                                                                                                                                                self.var_Name.get(),
                                                                                                                                                self.var_Date.get(),
                                                                                                                                                self.var_Division.get(),
                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                self.var_Reg_No.get()
                                                                                                                                        ))

                            else:
                                    if not Upadate:
                                            return 
                            messagebox.showinfo("Sucess" , "Student details successfully updated!", parent=self.root)
                            conn.commit()
                            self.fetch_data()
                            conn.close()
                    except Exception as es:
                            messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)
# delete function 
    def delete_data(self):
            if self.var_Reg_No.get() =="":
                    messagebox.showerror("Error" , "Student Reg must be required",parent = self.root)
            else:
                    try:
                            delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student" , parent= self.root)
                            if delete>0:
                                    conn = mysql.connector.connect(host="localhost",username="root",password="shrutipaul*@))&",database="face-recognizer")
                                    my_cursor = conn.cursor()
                                    sql = "delete from student where Reg_No = %s"
                                    val = (self.var_Reg_No.get(),)
                                    my_cursor.execute(sql,val)
                            else:
                                    if not delete:
                                            return
                            conn.commit()
                            self.fetch_data()
                            conn.close()
                            messagebox.showinfo("Delete" , "Successfully deleted student details" , parent=self.root)
 
                    except Exception as es:
                            messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)

#reset function
    def reset_data(self):
            self.var_Dept.set("Select Department")
            self.var_Course.set("Select Course")
            self.var_Year.set("Select Year")
            self.var_Sem.set("Select Semester")
            self.var_Reg_No.set("")
            self.var_Roll_No.set("")
            self.var_Name.set("")
            self.var_Date.set("")
            self.var_Division.set("Select Division")
            self.var_radio1.set("")
            
#================Generate data set  Take photo sample=============
    def generate_dataset(self):
            if self.var_Dept.get()=="Select Department" or self.var_Reg_No.get() == "" or self.var_Name.get() == "":
                    messagebox.showerror("Error","All fields are required",parent = self.root)
            else:
                    try:
                            conn = mysql.connector.connect(host="localhost",username="root",password="shrutipaul*@))&",database="face-recognizer")
                            my_cursor = conn.cursor()
                            my_cursor.execute("select * from student")
                            myresult = my_cursor.fetchall()
                            id = 0
                            for x in myresult:
                                    id += 1
                            my_cursor.execute("update student set Dept=%s,Course = %s,Year = %s , Sem = %s, Roll_No = %s , Name = %s , Date = %s , Division = %s , Photo = %s where Reg_No = %s ",(
                                                                                                                                                                self.var_Dept.get(),
                                                                                                                                                                self.var_Course.get(),
                                                                                                                                                                self.var_Year.get(),
                                                                                                                                                                self.var_Sem.get(),                                                                                                                                                
                                                                                                                                                                self.var_Roll_No.get(),
                                                                                                                                                                self.var_Name.get(),
                                                                                                                                                                self.var_Date.get(),
                                                                                                                                                                self.var_Division.get(),
                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                self.var_Reg_No.get() == id + 1
                                                                                                                                                           ))
                            conn.commit()
                            self.fetch_data()
                            self.reset_data()
                            conn.close()

   #====================== Load predefined data on face frontals from opencv ==========================
                            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                            def face_croped(img):
                                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                    faces =face_classifier.detectMultiScale(gray,1.3,5)
                                   #scaling factor = 1.3
                                   #Minimum neighbour = 5

                                    for(x,y,w,h) in faces:
                                            face_croped = img[y:y+h,x:x+w]
                                            return face_croped
                            cap = cv2.VideoCapture(0)
                            img_id = 0
                            while True:
                                    ret,my_frame =cap.read()
                                    if face_croped(my_frame) is not None:
                                            img_id += 1
                                            face = cv2.resize(face_croped(my_frame),(450,450))
                                            face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) 
                                            file_name_path = "data/user." + str(id) + "."+str(img_id)+".jpg" 
                                            cv2.imwrite(file_name_path,face)
                                            cv2.putText(face,str(img_id),(50 , 50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                            cv2.imshow("Cropped Face" , face)

                                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                                            break
                            cap.release()
                            cv2.destroyAllWindows()

                            messagebox.showinfo("Result" , "Generating data set completed!!")
                    except Exception as es:
                            messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)




if __name__ =="__main__":
    root = Tk()
    obj = Student(root)

    root.mainloop()