from tkinter import *
import os


master = Tk()
master.title("Path Setter")
master.geometry("300x150") 


# The GUI
path_label = Label(master,text="Path: ").grid(row=0, column=0)
path_value = Entry(master, width = 35,borderwidth = 5)
path_value.grid(row=0, column=1,columnspan = 4,padx = 10,pady = 5)


out_label = Label(master,text="output")
out_label.grid(row=2, column=1)


# Set path function to set the path
def set_path():
    path = path_value.get() # taking the path value from user
    
    try:
        os.environ['PATH'] += r'{}'.format(path)
    except:
        out_label.config(text = "Failed")
        return

    out_label.config(text = "All set")

    
        
Button(master, text ="Set",height = 3,width = 10,command=set_path).grid(row=2, column=1,padx = 10,pady = 5)

master.mainloop()


