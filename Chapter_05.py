from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

window = Tk()

window.title('Frames')
window.geometry('400x400')

icon = PhotoImage(file= 'images/icon.png')
window.iconphoto(True, icon)

myStyle =ttk.Style()
myStyle.configure('My.TFrame', background = '#ddadaf')

# Add the Frame
frame = Frame(window, style = 'My.TFrame') 
frame.place(x=25, y=25)

# Creating a photoimage object to use image
witch = PhotoImage(file=r'images/witch.png')
ant = PhotoImage(file=r'images/want.png')
snake = PhotoImage(file=r'images/snake.png')
dragon = PhotoImage(file=r'images/wdragon.png')

# Resize image to fit on button
photoimage1 = witch.subsample(1,1)
photoimage2 = ant.subsample(1,1)
photoimage3 = snake.subsample(1,1)
photoimage4 = dragon.subsample(1,1)

#Instead of setting to window, set eavch button to frame
Button(frame, image=photoimage1).pack(side=TOP)
Button(frame, image=photoimage2).pack(side=LEFT)
Button(frame, image=photoimage3).pack(side=LEFT)
Button(frame, image=photoimage4).pack(side=LEFT)



# frame.pack()

# Button(frame, text='A', font=('Consolas', 20), width=3).pack(side=TOP)
# Button(frame, text='B', font=('Consolas', 20), width=3).pack(side=LEFT)
# Button(frame, text='C', font=('Consolas', 20), width=3).pack(side=LEFT)
# Button(frame, text='D', font=('Consolas', 20), width=3).pack(side=LEFT)


window.mainloop()