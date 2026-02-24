# Animation
from tkinter import *

def move_up(event):
    # the -10 is the speed in the up direction, so negative 10
    label.place(x=label.winfo_x(), y = label.winfo_y() - 10)

def move_down(event):
    # the 10 is the speed in the down direction, so positive 10
    label.place(x=label.winfo_x(), y = label.winfo_y() + 10)

def move_left(event):
    # the - 10 is the speed in the up direction, so negative 10
    # except that this is in the x coordinates 
    label.place(x=label.winfo_x()-10, y = label.winfo_y())

def move_right(event):
    # the 10 is the speed in the up direction, so positive 10
    # this is also in the x coordinates 
    label.place(x=label.winfo_x()+10, y = label.winfo_y())

window =Tk()
window.title('Drag Image')
window.geometry('400x350')

icon = PhotoImage(file='images/icon.png')
window.iconphoto=(TRUE, icon)

# Bind to W, S, A, D keys
window.bind('<w>', move_up)
window.bind('<s>', move_down)
window.bind('<a>', move_left)
window.bind('<d>', move_right)

# Bind to the arrow keys
window.bind('<Up>', move_up)
window.bind('<Down>', move_down)
window.bind('<Left>', move_left)
window.bind('<Right>', move_right)

myimage = PhotoImage(file='images/wdragon.png')

label = Label(window, image= myimage)
label.place(x=0,y=0)

window.mainloop()
