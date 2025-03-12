from tkinter import*
import pymysql #pip install pymysql
from tkinter import messagebox,ttk
from dashboard import RMS
import sqlite3
import os
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        
        # self.lbl=Label(self.root,bg="white",bd=10,relief=RAISED)
        # self.lbl.place(x=90,y=120,height=450,width=350)
        
        #frames
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)
        
        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)

        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)

        password=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=250)
        self.txt_password_=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_password_.place(x=250,y=280,width=350,height=35)

        btn_reg=Button(login_frame,text="Register new account?",command=self.register_window,font=("times new roman",14),bg="white",bd=0,fg="#B00857",cursor="hand2").place(x=235,y=320)

        btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman",20,"bold"),fg="white",bg="#B00857",cursor="hand2").place(x=235,y=380,width=180,height=40)



    def register_window(self):
        self.root.destroy()
        import register


    def login(self):
        if self.txt_email.get()=="" or self.txt_password_.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=sqlite3.connect(database="rms.db")
                cur=conn.cursor()
                cur.execute("Select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_password_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid username and password",parent=self.root)
                    
                else:
                    messagebox.showinfo("Success",f"Welcome: {self.txt_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                conn.close()  
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)



root=Tk()
obj=Login_window(root)
root.mainloop()
