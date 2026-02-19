# Various types of window messages
from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("I am a ListBox")
window.geometry("500x400")
window.config(background="#01211e")
icon = PhotoImage(file='images\icon.png')
window.iconphoto(TRUE, icon)

def click1():
    messagebox.showinfo(title='Info Message ', message = "This is a message")

def click2():
    messagebox.showwarning(title='Warning Message ', message = "This is a Warning")

def click3():
    messagebox.showerror(title='Error Message ', message = "This is an Error")

messagebutton = Button(window, text='Message', command = click1, font=("Constantia", 15), width = 10, bg = "#01211e", fg='#f0f4f5', activeforeground = "#cff5cf", activebackground ="#124212")
messagebutton.pack()

warningbutton = Button(window, text='Warning', command = click2, font=("Constantia", 15), width = 10, bg = "#01211e", fg='#f0f4f5', activeforeground = "#cff5cf", activebackground ="#124212")
warningbutton.pack()

errorbutton = Button(window, text='Error', command = click3, font=("Constantia", 15), width = 10, bg = "#01211e", fg='#f0f4f5', activeforeground = "#cff5cf", activebackground ="#124212")
errorbutton.pack()

window.mainloop()