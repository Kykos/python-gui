# Canvas is a widget that allows us to draw shapes, images, and other complex layouts. It provides a space where we can create and manipulate graphical elements. In this example, we will create a simple canvas and add some shapes to it.

from tkinter import *

window = Tk()

window.title('Canvas')
window.geometry('400x400')
icon = PhotoImage(file= 'images/icon.png')
window.iconphoto(True, icon)

canvas = Canvas(window,height =400, width = 400, bg = '#ddadaf')
roon = canvas.create_line(0,0, 400, 400, fill='blue', width=2)
idgo = canvas.create_line(0, 400, 400, 0, fill='maroon', width=4)
blk = canvas.create_line(50,30, 30, 50, fill='black', width=9)

# create a rectangle
# rect = canvas.create_rectangle(50, 50, 150, 150, fill='yellow', outline='red', width=3)

# create an Oval
oval = canvas.create_oval(200, 50, 300, 150, fill='green', outline='blue', width=3)

# create a polugon
points = [50, 200, 150, 250, 100, 300]
polygon = canvas.create_polygon(points, fill='purple', outline='black', width=3)

# create an arc
arc = canvas.create_arc(200, 200, 300, 300, start=0, extent=150, fill='orange', outline='black', width=3)

# create a image
witch = PhotoImage(file=r'images/witch.png')
canvas.create_image(100, 350, image=witch)

# create text
canvas.create_text(200, 20, text='Hello Canvas', font=('Consolas', 20), fill='red')

#Create a widget on canvas
button = Button(canvas, text='Click Me', font=('Consolas', 14), bg='lightblue')
canvas.create_window(200, 350, window=button)
   

canvas.pack()



window.mainloop()

