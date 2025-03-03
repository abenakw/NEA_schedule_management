from tkinter import *
#unnecessary i think # from PIL import Image,ImageTk #pip install pillow
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #icons (install pillow)6
        #instead of massive logo photo, find a way to add a live calendar, so it shows the tutor
        #their upcoming sessions, and also allows them to click the calendar to make edits
        #(around 10 mins into video, i didnt add some of the code, unnecessary) self.logo_dash=Image.open("")


        #titles
        title=Label(self.root,text="Student Result Management System",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

        #menu
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)

#command=self.add_course below, redirects the user to the course page
        btn_course=Button(M_Frame,text="Courses",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2", command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="Students",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="View Student Results",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1120,y=5,width=200,height=40)


        #content window(19 mins onwards)
        #i dont think the images are necessary, alternative?

        #update details
        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_student.place(x=710,y=530,width=300,height=100)

        self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)

#pick your own colours later, perhpas go for a modern theme
        #footer, i dont think its necessary, about 17 mins into vid)

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
        
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win) 
        
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)   
        
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)   
                          
   
if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()

