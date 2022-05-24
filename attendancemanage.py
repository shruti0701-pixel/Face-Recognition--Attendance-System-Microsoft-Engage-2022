from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recoginition System")

#====================variables====================
        self.var_atten_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_attendance = StringVar()


        #title image1
        img = Image.open(r"collection_images\black_stdt.jpg")
        img = img.resize((500 , 130) , Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        first_lbl = Label(self.root,image=self.photoimg) 
        first_lbl.place(x=0,y=0,width=500,height=130)

        #title img2
        img1 = Image.open(r"collection_images\attendancesheet.jpg")
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

        img3 = Image.open(r"collection_images\background.jpg")
        img3 = img3.resize((1400 , 600) , Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_lbl = Label(self.root,image=self.photoimg3) 
        bg_lbl.place(x=0,y=100,width=1400,height= 600)

        title_lbl = Label(bg_lbl,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="black",bd=6,relief=GROOVE)
        title_lbl.place(x=0,y=0,width=1268,height=45)

        main_frame = Frame(bg_lbl , bd = 2 , bg = "white")
        main_frame.place(x=5,y= 48,width=1260,height=490)

        Left_frame = LabelFrame(main_frame,bd=2,bg = "white",relief=RIDGE, text = "Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place (x= 6,y= 6,width= 600,height=580)


        img_left= Image.open(r"collection_images\attendancesheet.jpg")
        img_left= img_left.resize((500,130) , Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        first_lbl = Label(Left_frame,image=self.photoimg_left) 
        first_lbl.place(x=5,y=0,width=500, height=130)

        left_insideframe = Frame(Left_frame , bd = 2 ,relief=RIDGE, bg = "white")
        left_insideframe.place(x=5,y= 135,width= 585 ,height= 310)
        
        #Labels and entry

        attendance_id = Label(left_insideframe,text="ATTENDANCE ID:",font=("comicsansns 11 bold"),bg="white")
        attendance_id.grid(row=0,column=0,padx=2,pady=6,sticky=W)

        attendance_entry = ttk.Entry(left_insideframe,width=20,font=("comicsansns 11 bold"),textvariable=self.var_atten_id)
        attendance_entry.grid(row=0,column=1,padx=2,pady=6,sticky=W)

        attendanceroll_id = Label(left_insideframe,text="ROLL NO:",font=("comicsansns 11 bold"),bg="white")
        attendanceroll_id.grid(row=0,column=2,padx=2,pady=6,sticky=W)

        attendance_entry = ttk.Entry(left_insideframe,width=20,font=("comicsansns 11 bold"),textvariable=self.var_roll)
        attendance_entry.grid(row=0,column=3,padx=3,pady=6,sticky=W)

        name = Label(left_insideframe,text="NAME:",font=("comicsansns 11 bold"),bg="white")
        name.grid(row=1,column=0,padx=2,pady=6,sticky=W)

        name_entry= ttk.Entry(left_insideframe,width=20,font=("comicsansns 11 bold"),textvariable=self.var_name)
        name_entry.grid(row=1,column=1,padx=2,pady=6,sticky=W)

        dept = Label(left_insideframe,text="DEPT:",font=("comicsansns 11 bold"),bg="white")
        dept.grid(row=1,column=2,padx=2,pady=6,sticky=W)

        dept_entry= ttk.Entry(left_insideframe,width=20,font=("comicsansns 11 bold"),textvariable=self.var_dep)
        dept_entry.grid(row=1,column=3,padx=2,pady=6,sticky=W)

        date = Label(left_insideframe,text="DATE:",font=("comicsansns 11 bold"),bg="white")
        date.grid(row=2,column=0,padx=2,pady=6,sticky=W)

        date_entry= ttk.Entry(left_insideframe,width=20,font=("comicsansns 11 bold"),textvariable=self.var_date)
        date_entry.grid(row=2,column=1,padx=2,pady=6,sticky=W)

        time = Label(left_insideframe,text="TIME:",font=("comicsansns 11 bold"),bg="white")
        time.grid(row=2,column=2,padx=2,pady=6,sticky=W)

        time_entry= ttk.Entry(left_insideframe,width=20,font=("comicsansns 11 bold"),textvariable=self.var_time)
        time_entry.grid(row=2,column=3,padx=2,pady=6,sticky=W)

        attendancestatus_lbl = Label(left_insideframe,text="ATTENDANCE:",font=("comicsansns 11 bold"),bg="white")
        attendancestatus_lbl.grid(row=3,column=0,padx=2,pady=6,sticky=W)

        attendancestatus_combo = ttk.Combobox(left_insideframe,font=("comicsansns 11"),state="readonly",width=18,textvariable=self.var_attendance)
        attendancestatus_combo["values"] = ("Status","PRESENT" ,"ABSENT")
        attendancestatus_combo.current(0)
        attendancestatus_combo.grid(row=3,column=1,padx=2,pady=6,sticky=W)

        btn_frame =Frame(left_insideframe,bd=2,relief=RIDGE,bg="white")
        btn_frame.place (x=30,y=200,width=450,height=35)

        import_btn=Button(btn_frame,text="Import/View data",command=self.importCsv,width=15,font=("times new roman",12,"bold"),bg="black",fg="white") 
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=15,font=("times new roman",12,"bold"),bg="black",fg="white") 
        export_btn.grid(row=0,column=1)

        #update_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",12,"bold"),bg="black",fg="white") 
        #update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset,width=17,font=("times new roman",12,"bold"),bg="black",fg="white") 
        reset_btn.grid(row=0,column=2)


#Right side frame
        Right_frame = LabelFrame(main_frame,bd=2,bg = "white",relief=RIDGE, text = "Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place (x= 620,y= 6,width=630,height=580)

        table_frame =Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place (x=5,y=5,width=610,height=440)

        #===========scrollbar table ============

        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","department","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM ,fill=X)
        scroll_y.pack(side=RIGHT ,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text = "Attendance ID")
        self.AttendanceReportTable.heading("roll",text = "Roll")
        self.AttendanceReportTable.heading("name",text = "Name")
        self.AttendanceReportTable.heading("department",text = "Department")
        self.AttendanceReportTable.heading("date",text = "Date")
        self.AttendanceReportTable.heading("time",text = "Time")
        self.AttendanceReportTable.heading("attendance",text = "Attendance")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id",width = 100)
        self.AttendanceReportTable.column("roll",width = 100)
        self.AttendanceReportTable.column("name",width = 100)
        self.AttendanceReportTable.column("department",width = 100)
        self.AttendanceReportTable.column("date",width = 100)
        self.AttendanceReportTable.column("time",width = 100)
        self.AttendanceReportTable.column("attendance",width = 100)

        self.AttendanceReportTable.heading("id",text="Attendance ID")

        self.AttendanceReportTable.pack(fill = BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
#================== fetch data =========================

    def fetchData(self,rows):
        self.AttendanceReportTable.update(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
#import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL Files","*.*")),parent=self.root)
        with open(filename) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

#export CSV
    def exportCsv(self):
        try:
            if len(mydata) <1:
                messagebox.showerror("No Data" , "No Data Found to export",parent=self.root)
                return False
            filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL Files","*.*")),parent=self.root)
            with open(filename,mode="w",newline="") as myfile:
                export_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    export_write.writerow(i)
                messagebox. showinfo("Data Export","Your data is exported to " + os.path.basename(filename)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent = self.root)

    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])  
        self.var_roll.set(rows[1])  
        self.var_name.set(rows[2])  
        self.var_dep.set(rows[3])  
        self.var_date.set(rows[4])  
        self.var_time.set(rows[5])   
        self.var_attendance.set(rows[6])  

    def reset(self):
        self.var_atten_id.set("")  
        self.var_roll.set("")  
        self.var_name.set("")  
        self.var_dep.set("")  
        self.var_date.set("")  
        self.var_time.set("")   
        self.var_attendance.set("") 


if __name__ =="__main__":
    root = Tk()
    obj = Attendance(root)

    root.mainloop() 