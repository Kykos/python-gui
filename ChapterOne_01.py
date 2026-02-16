from tkinter import *

window =Tk()
window.title("My First GUI")
window.geometry("600x400")

icon = PhotoImage(file = "images\icon.png")
window.iconphoto(True, icon)

window.config(background= "#27F5F2")

window.mainloop()