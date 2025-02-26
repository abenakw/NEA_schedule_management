from tkinter import *
#unnecessary i think # from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox
import pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.focus_force()