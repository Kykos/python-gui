from tkinter import *

window = Tk()
window.title=('A check Button')
window.geometry('500x200')

icon =PhotoImage(file='images\icon.png')
photo = PhotoImage(file="images\PandV.png")
window.iconphoto(True, icon)
window.config(background='#001400')
check_button = Checkbutton(window,text="I agree to something",)

def display():
    if(x.get()==1):
        print("You agree!:)")
    else:
        print("You do not agree :(")

x =IntVar()

check_button = Checkbutton(window, 
                           text='I agree to something',
                           variable =x,
                           onvalue =1,
                           offvalue=0,
                           command= display,
                           font=("Time New Roman", 14),
                           fg = '#001400',
                           bg='#eff5cf',
                           activeforeground='#cff5cf',
                           activebackground='#1b6531',
                           padx = 25,
                           pady = 10,
                           image = photo,
                           compound = LEFT,
                           )

check_button.pack()

window.mainloop()