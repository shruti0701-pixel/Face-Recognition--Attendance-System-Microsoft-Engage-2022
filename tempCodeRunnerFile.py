img1 = Image.open(r"C:\Users\shruti paul\Desktop\Final Project\collection_images\school.jpg")
        img1 = img1.resize((500 , 130) , Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_lbl = Label(self.root,image=self.photoimg1) 
        first_lbl.place(x=400,y=0,width=500,height=130)