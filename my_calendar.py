from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar

class my_calendarClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Calendar System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()


        def add_event():
            event_date = cal.selection_get()
            event_description = event_entry.get()
            if event_description:
                event_listbox.insert(tk.END, f"{event_date}: {event_description}")
                event_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You need to enter an event description")
                
            
        def clear_events():
            event_listbox.delete(0, tk.END)            

        root = tk.Tk()
        root.title("The Calendar App")

        # This will create the calendar widget
        cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
        cal.pack(pady=20)

        #This will add events and buttons

        event_entry = tk.Entry(root, width=50)
        event_entry.pack(pady=10)

        add_btn = tk.Button(root, text="Add Event", command=add_event)
        add_btn.pack(pady=5)

        # This event will create the listbox
        event_listbox = tk.Listbox(root,width=50, height=10)
        event_listbox.pack(pady=20)


if __name__=="__main__":
    root=Tk()
    obj=my_calendarClass(root)
    root.mainloop()