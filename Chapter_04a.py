# Color Chooser
from tkinter import *
from tkinter import colorchooser

window = Tk()
window.title('Color Chooser')
window.geometry('400x400')
icon = PhotoImage(file='images\icon.png')
window.iconphoto(True, icon)

# The two click functions are identical
# def click():
#     color = colorchooser.askcolor()
#     colorHEX = color[1]
#     print(colorHEX)
#     window.config(bg=colorHEX)

def click():
    window.config(bg=colorchooser.askcolor()[1])    

button = Button(text='click me!',
                command = click
                )

button.pack()
window.mainloop()

