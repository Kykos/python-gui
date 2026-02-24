# Mouse events

from tkinter import *
def doSomething(event):
    print('Mouse Coordinates ' + str(event.x) + ', ' + str(event.y))

def doThisInstead(event):
    print('You Released the button')

def doThisToo(event):
    print('Do you like chicken and rise?')

def fineJustGo(event):
    print('You just left the window')

def doSomethingMotion(event):
    print('The mouse is in motion')
window = Tk()

window.title('Mouse Events')
window.geometry('400x350')
window.config(background = '#b7787a')

icon = PhotoImage(file='images/icon.png')
window.iconphoto(TRUE, icon)

# # window.bind('<Button-1>', doSomething) # Left mouse button click
window.bind('<Button-2>', doSomething)             # Scroll wheel button click
window.bind('<Button-3>', doSomething)             # Right mouse button click
window.bind('<ButtonRelease>', doThisInstead)
window.bind('<Enter>', doThisToo)                  # When the mouse enters the window
window.bind('<Leave>', fineJustGo)                 # When the mouse Leaves/exits the window

# the motion event overrides the rest of the events. Use it by iteself (comment out the other event triggers)
window.bind('<Motion>', doSomethingMotion)

window.mainloop()

          
