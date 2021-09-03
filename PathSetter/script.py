  
from tkinter import *
import os


master = Tk()
master.title("calculator")
master.geometry("300x300") 

# The GUI
path_l1 = Label(master,text="Name: ").grid(row=0, column=0)
name = Entry(master, width = 35,borderwidth = 5)
name.grid(row=0, column=1,columnspan = 4,padx = 10,pady = 5)

path_l2 = Label(master,text="Path: ").grid(row=1, column=0)
path_value = Entry(master, width = 35,borderwidth = 5)
path_value.grid(row=1, column=1,columnspan = 4,padx = 10,pady = 5)


out_label = Label(master,text="output")
out_label.grid(row=2, column=1)
# Set path function to set the path

def set_path():

    path_name = name.get() 
    path = path_value.get()
    print("hello")
    if (os.environ.get(path_name)):
        out_label.config(text = "Already set")
    else:
        try:
            os.environ[path_name] = path
        except:
            out_label.config(text = "Failed")
            return
        out_label.config(text = "All set")
        
        
# function to remove

def remove_path():
    path_name = name.get() 
    path = path_value.get()

    if (os.environ.get(path_name)):
        out_label.config(text = "Not found")
    else:
        try:
            os.environ.pop(path_name)
        except:
            out_label.config(text = "Failed")
            return

        out_label.config(text = "Done")


    



Button(master, text ="Set",height = 3,width = 10,command=set_path).grid(row=2, column=1,padx = 10,pady = 5)
Button(master, text ="Remove",height = 3,width = 10,command=remove_path).grid(row=2, column=2,padx = 10,pady = 5)

master.mainloop()


