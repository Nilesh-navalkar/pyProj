

# # from sqlalchemy import create_engine
# import pandas as pd

# # from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# # # mydb =  conn=mysql.connector.connect(host="127.0.0.1",username="root",password="jemish@123",database="test")
# # # mycursor = mydb.cursor()

# # my_conn = create_engine("mysql+mysqldb://root:jemish@123@127.0.0.1/test")

# # query="select distinct(class) as class FROM student"
# # my_data=my_conn.execute(query)
# # my_list =  [r for r in my_data] #for unique class in db

# # import tkinter as tk
# # from tkinter import ttk
# # my_w = tk.Tk()    #window
# # my_w.geometry("400x450") 
# # my_w.title("Graph")

# # def my_up(*args):
# #     query="select Name, mark from student " 
# #     df=pd.raed_sql(query,my_conn,index_col='name')
# #     fig1=df.plot.line(title="Mark",y='mark',
# #         figsize=(3,3)).get_figure();
# #     plot1=FigureCanvasTkAgg(fig1,my_w)
# #     plot1.get_tk_widget().grid(row=2,column=2,columnspan=2,padx=30,pady=3)

# # sel=tk.StringVar()
# # cb1 = ttk.Combobox(my_w, values=my_list, width=15,textvariable=sel) #sel is used for new upadted value
# # cb1.grid(row=1,column=1)
# import mysql.connector
# import tkinter  as tk 
# from tkinter import * 

# my_cursor = my_connect.cursor()
# ####### end of connection ####

# my_w = tk.Tk()
# my_w.geometry("400x200") 

# # add one Label 
# l1 = tk.Label(my_w,  text='Enter Student ID: ', width=25 )  
# l1.grid(row=1,column=1) 

# # add one text box
# t1 = tk.Text(my_w,  height=1, width=4,bg='yellow') 
# t1.grid(row=1,column=2) 

# b1 = tk.Button(my_w, text='Show Details', width=15,bg='red',
#     command=lambda: my_details(t1.get('1.0',END)))
# b1.grid(row=1,column=4) 

# my_str = tk.StringVar()
# # add one Label 
# l2 = tk.Label(my_w,  textvariable=my_str, width=30,fg='red' )  
# l2.grid(row=3,column=1,columnspan=2) 
# from sqlalchemy import create_engine
# from sqlalchemy.exc import SQLAlchemyError
            
# my_conn = create_engine("mysql+mysqldb://root:password@localhost/db_name")

# my_str.set("Output")

# def my_details(id):
  
#         try:
#             my_cursor.execute("SELECT marks FROM student")
#             student = my_cursor.fetchone()
#             #print(student)
#             my_str.set(student)
    
     
# my_w.mainloop()

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk,ImageDraw

import mysql.connector
from tkinter import messagebox
from student import student
# from register import register

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r'bgimg.jpg')
        lbl_bg = Label(self.root,image = self.bg)
        lbl_bg.place(x=0,y=0,width=1530,height=790)

        frame = Frame(self.root,bg='white')
        frame.place(x=610,y=170,width=340,height=450)

        # img1 = Image.open(r"loginicon.jpg")
        # img1 = img1.resize((100,100),Image.ANTIALIAS)
        # self.photoimage1 = ImageTk.PhotoImage(img1)
        # lblimg1 = Label(image = self.photoimage1, bg="white",borderwidth=0)
        # lblimg1.place(x=730,y=175,width=100,height=100)

        get_str = Label(frame,text='Get Started',font=('times new roman',20,'bold'),bg='white',fg='black')
        get_str.place(x=95,y=100)

        #label
        username = Label(frame,text='Email',font=('times new roman',15,'bold'),bg='white',fg='black')
        username.place(x=70,y=155)

        self.txtuser = ttk.Entry(frame,font=('times new roman',15,'bold'))
        self.txtuser.place(x=40,y=180,width=270)

        password = Label(frame,text='Password',font=('times new roman',15,'bold'),bg='white',fg='black')
        password.place(x=70,y=225)

        self.txtpass = ttk.Entry(frame,font=('times new roman',15,'bold'))
        self.txtpass.place(x=40,y=250,width=270)

        # Icon Imgaes
        # img2 = Image.open(r"emailicon.png")
        # img2 = img2.resize((25,25),Image.ANTIALIAS)
        # self.photoimage2 = ImageTk.PhotoImage(img2)
        # lblimg2 = Label(image = self.photoimage2, bg="white",borderwidth=0)
        # lblimg2.place(x=650,y=323,width=25,height=25)

        # img3 = Image.open(r"lockicon.png")
        # img3 = img3.resize((25,25),Image.ANTIALIAS)
        # self.photoimage3 = ImageTk.PhotoImage(img3)
        # lblimg3 = Label(image = self.photoimage3, bg="white",borderwidth=0)
        # lblimg3.place(x=650,y=395,width=25,height=25)

        # Button
        loginbtn = Button(frame,text='Login',command=self.login,font=('times new roman',15,'bold'),width=13,bg='red',fg='black',activeforeground="black",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # registerbtn = Button(frame,text='New User Register',command=self.register_window,borderwidth=0,font=('times new roman',12,'bold'),width=13,bg='white',fg='black',activeforeground="black",activebackground="white")
        # registerbtn.place(x=20,y=350,width=160)

        # forgetbtn = Button(frame,text='Forget Password',command=self.forgot_password_window,borderwidth=0,font=('times new roman',12,'bold'),width=13,bg='white',fg='black',activeforeground="black",activebackground="white")
        # forgetbtn.place(x=10,y=380,width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="R@#ul051102",database="employee_management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main = messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app = student(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()