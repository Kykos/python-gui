# Drag and Drop Multipe items
from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x    # this is where we click within tha lkabel
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place (x = x, y = y)

window = Tk()

window.title('Drag and Drop')
window.geometry('400x350')
window.config(background='#000080')

icon = PhotoImage(file='images/icon.png')
#window.iconphoto(TRUE, icon)

label = Label(window, bg='#1f03ad', width=10, height=5)
label.place(x=0, y=0)

label2 = Label(window, bg='brown', width=10, height=5)
label2.place(x=100, y=100)

label.bind('<Button-1>', drag_start)
label.bind('<B1-Motion>', drag_motion)

label2.bind('<Button-1>', drag_start)
label2.bind('<B1-Motion>', drag_motion)

window.mainloop()