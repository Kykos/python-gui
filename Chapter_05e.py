# Create new Window
from tkinter import *

def create_window():
    new_window = Tk()
    new_window.geometry("320x300")
    new_window.title("I am a New Window")
    new_window.config(background='#b7787a')
    window.destroy()

window =Tk()
window.title('New WIndows')
window.geometry("400x350")

window.config(background="#2f5688")

icon = PhotoImage(file="images/icon.png")
window.iconphoto(True, icon)

Button(window, text='Click here for the new window!', command=create_window, font=('Lucida Calligraphy', 11),bg='#25375F', fg='white').pack()
window.mainloop()

       