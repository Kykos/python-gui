from tkinter import *

window = Tk()
window.title=('Radio Buttons')
window.geometry('350x150')

icon =PhotoImage(file='images\icon.png')
window.iconphoto(True, icon)
window.config(background='#e7c6c7')

food = ['sald', 'steak', 'desert']
x= IntVar()

for index in range(len(food)):
    radioButton = Radiobutton(window,
                            font=("Helvetica", 18),
                            bg="#e7c6c7",
                            text  = food[index],
                            variable = x,
                            value=index,
                            )
    radioButton.pack()
window.mainloop()
