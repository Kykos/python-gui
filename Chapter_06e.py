# Animation on Canvas
from tkinter import *

def move_up(event):
    canvas.move(myimage, 0, -10) 

def move_down(event):
    canvas.move(myimage, 0, 10)

def move_left(event):
    canvas.move(myimage, -10, 0)

def move_right(event):
        canvas.move(myimage, 10, 0)

window =Tk()
window.title('Drag Image on the Canvas')
window.geometry('400x350')
window.config(background = '#000080')

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

canvas = Canvas(window, width= 500, height = 500, background = '#000080')
canvas.pack()

photoimage = PhotoImage(file='images/wdragon.png')
myimage = canvas.create_image(0,0, image=photoimage, anchor=NW)

window.mainloop()
