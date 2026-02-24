# Drag and Drop
from tkinter import *

def drag_start(event):
    label.startX = event.x              # this is where we click within the label
    label.startY = event.y

def drag_motion(event):
    x = label.winfo_x() - label.startX + event.x
    y = label.winfo_y() - label.startY + event.y
    label.place(x=x, y=y)

window = Tk()

window.title('Drag and Drop')
window.geometry('400x350')
window.config(background='#000080')

icon = PhotoImage(file='images/icon.png')
window.iconphoto(TRUE, icon)

label = Label(window, bg='#1f03ad', width=10, height=5)
label.place(x=0, y=0)

label.bind('<Button-1>', drag_start)
label.bind('<B1-Motion>', drag_motion)

window.mainloop()

