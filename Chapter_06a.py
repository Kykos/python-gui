# Keyboard Events
from tkinter import *

def doSomething(event):
    # print to the terminal the key that was pressed
    # print("You pressed: " + event.keysym)
    label.config(text="You pressed: " + event.keysym)

window = Tk()

window.title("Keyboard Events")
window.geometry("400x350")

icon = PhotoImage(file="images/icon.png")
window.iconphoto(True, icon)
window.bind("<Key>", doSomething)

label = Label(window, font=('Helvetica', 20), width=150, bg='#ddadaf', fg='#652517')
label.pack()

window.mainloop()
