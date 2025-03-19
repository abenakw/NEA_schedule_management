from tkinter import*
import pymysql #pip install pymysql
from tkinter import messagebox,ttk
from dashboard import RMS
import sqlite3
import os

#for testing use kym@gmail.com pass:kym@123, birth place:london
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
        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_password_window,font=("times new roman",14),bg="white",bd=0,fg="red",cursor="hand2").place(x=450,y=320)



        btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman",20,"bold"),fg="white",bg="#B00857",cursor="hand2").place(x=235,y=380,width=180,height=40)

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)


    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                conn=sqlite3.connect(database="rms.db")
                cur=conn.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?",[(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get())])
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select the Correct Security Question / Enter Answer",parent=self.root2)                    
                else:
                    cur.execute("update employee set password=? where email=?",[(self.txt_new_pass.get(),self.txt_email.get())])
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Your password has been reset, Please login with your new password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es: 
                  messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
                
                

    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset your password",parent=self.root)
        else:
            try:
                conn=sqlite3.connect(database="rms.db")
                cur=conn.cursor()
                cur.execute("Select * from employee where email=?",[(self.txt_email.get())])
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the valid email address to reset your password",parent=self.root)                    
                else:
                    conn.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+495+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    
                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)

                    #Forget password
                    question=Label(self.root2,text="Security question",font=("times new roman",20,"bold"),fg="gray").place(x=50,y=100)
                    
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly', justify=CENTER)
                    self.cmb_quest['values']=("Select", "Your First Pet Name","Your Birth Place")
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)
                    
                    
                    answer=Label(self.root2,text="Answer",font=("times new roman",20,"bold"),fg="gray").place(x=50,y=180)
                    self.txt_answer=Entry(self.root2,font=("times new roman",15),fg="white",bg="lightgray")
                    self.txt_answer.place(x=50,y=210,width=250)

                    new_password=Label(self.root2,text="New Password",font=("times new roman",20,"bold"),fg="gray").place(x=50,y=260)
                    self.txt_new_pass=Entry(self.root2,font=("times new roman",15),fg="white",bg="lightgray")
                    self.txt_new_pass.place(x=50,y=290,width=250)


                    btn_change_password=Button(self.root2,text="Reset Password",command=self.forget_password,bg="green", fg="white",font=("times new roman",15,"bold")).place(x=90,y=340)
  
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

        
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
