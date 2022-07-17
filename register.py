from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class register:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Register')

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()


        # Background
        self.bg = ImageTk.PhotoImage(file=r'bgimg.jpg')
        bg_lbl = Label(self.root,image = self.bg)
        bg_lbl.place(x=0,y=0,width=1530,height=790)

        # Left Image
        user_img = Image.open(r'user.jpg')
        user_img = user_img.resize((420,450),Image.ANTIALIAS)
        self.userimg = ImageTk.PhotoImage(user_img)
        left_lbl = Label(self.root,image = self.userimg)
        left_lbl.place(x=75,y=150,width=420,height=450)

        # Register Frame
        frame = Frame(self.root,bg='white')
        frame.place(x=590,y=100,width=800,height=550)

        register_lbl = Label(frame,text="REGISTER HERE",font=('times new roman',15,'bold'),fg="green",bg="white")
        register_lbl.place(x=20,y=20)

        # Row1
        fname = Label(frame,text='First Name',font=('times new roman',15,'bold'),fg='black',bg='white')
        fname.place(x=50,y=100)

        fname_entry = ttk.Entry(frame,textvariable=self.var_fname,width=22,font=('times new roman',14,'bold'))
        fname_entry.place(x=50,y=130,width=250)

        l_name = Label(frame,text='Last Name',font=('times new roman',15,'bold'),fg='black',bg='white')
        l_name.place(x=370,y=100)

        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname,width=22,font=('times new roman',14,'bold'))
        self.txt_lname.place(x=370,y=130,width=250)

        # Row2
        contact = Label(frame,text='Contact No',font=('times new roman',15,'bold'),fg='black',bg='white')
        contact.place(x=50,y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact,width=22,font=('times new roman',14,'bold'))
        self.txt_contact.place(x=50,y=200,width=250)

        email = Label(frame,text='Email',font=('times new roman',15,'bold'),fg='black',bg='white')
        email.place(x=370,y=170)

        self.txt_lname = ttk.Entry(frame,textvariable=self.var_email,width=22,font=('times new roman',14,'bold'))
        self.txt_lname.place(x=370,y=200,width=250)

        # Row3
        security_Q = Label(frame,text='Select Security Questions',font=('times new roman',15,'bold'),fg='black',bg='white')
        security_Q.place(x=50,y=240)

        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ,font=('times new roman',15,'bold'),width=17,state='readonly')
        self.combo_security_Q['values']=('Select','Your Birth Place','Your Girlfriend Name','Your Pet Name')
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50,y=270,width=250)

        security_A = Label(frame,text='Security Answer',font=('times new roman',15,'bold'),fg='black',bg='white')
        security_A.place(x=370,y=240)

        self.txt_security = ttk.Entry(frame,textvariable=self.var_SecurityA,width=22,font=('times new roman',14,'bold'))
        self.txt_security.place(x=370,y=270,width=250)

        # Password
        pswd = Label(frame,text='Password',font=('times new roman',15,'bold'),fg='black',bg='white')
        pswd.place(x=50,y=310)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass,width=22,font=('times new roman',14,'bold'))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd = Label(frame,text='Confirm Password',font=('times new roman',15,'bold'),fg='black',bg='white')
        confirm_pswd.place(x=370,y=310)

        self.txt_lname = ttk.Entry(frame,textvariable=self.var_confpass,width=22,font=('times new roman',14,'bold'))
        self.txt_lname.place(x=370,y=340,width=250)

        # Check Button
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check,text = 'I Agree terms and Conditions',font=('times new roman',15,'bold'),bg='white',onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        # Buttons
        img = Image.open("registerimg.jpg")
        img = img.resize((200,50),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame,command=self.register_data,image=self.photoimage,borderwidth=0,cursor='hand2',font=('times new roman',15,'bold'),bg='white')
        b1.place(x=70,y=420,width=200)

        img1 = Image.open("loginimg.jpg")
        img1 = img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame,command=self.return_login,image=self.photoimage1,borderwidth=0,cursor='hand2',font=('times new roman',15,'bold'),bg='white')
        b1.place(x=390,y=420,width=200)

    # Function Declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions",parent=self.root)
        else:
            conn = mysql.connector.connect(host="127.0.0.1",user="root",password="jemish@123",database="test")
            my_cursor = conn.cursor()
            query = ("select * from login where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_SecurityA.get(),
                    self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully",parent=self.root)

    def return_login(self):
        self.root.destroy()

if __name__=="__main__":
    root = Tk()
    obj = register(root)
    root.mainloop()