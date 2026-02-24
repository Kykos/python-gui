# TEXT Area
from tkinter import *
window =Tk()
window.title('Text Area')
window.geometry('300x250')

icon = PhotoImage(file='images\icon.png')
window.iconphoto(True, icon)

def submit():
    input=text.get("1.0",END)
    print(input)

text = Text(window,
            bg = 'light yellow',
            font=('Ink Free', 25),
            height = 8,
            width = 20,
            padx = 20,
            pady = 20,
            fg = 'purple'           
            
            )
text.pack()

button = Button(window, text="submit", command = submit )
button.pack()

window.mainloop()