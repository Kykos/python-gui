# SLiding scale
from tkinter import *

def submit():
    print('The temperature is ' + str(scale.get()) + ' degrees F')

window = Tk()
window.title('Thermometer')
window.geometry('400x800')

icon = PhotoImage(file='images/icon.png')
window.iconphoto=(TRUE, icon)

hotImage = PhotoImage(file='images/hot.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
             from_ = 100,
             to = 0,
             length=600,
             orient = VERTICAL, 
             background ='#25375F',
             foreground = '#fcf7f7',
             font =('Helvetica', 14),
             troughcolor = '#fcf7f7',
             activebackground = '#25375F',
             tickinterval = 10
              )
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

coldImage = PhotoImage(file='images/cold.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window, text='submit', command = submit)
button.pack()

window.mainloop()
