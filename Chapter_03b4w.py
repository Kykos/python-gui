from tkinter import *
from tkinter import messagebox

window =Tk()
window.title('Message Boxes')
window.geometry('300x200')

icon = PhotoImage(file='images\icon.png')
window.iconphoto(True, icon) 

label = Label(window, text='Various message boxes')
label.pack()

'''
def click():
    messagebox.showinfo(title='Info Message ', message="This is a message")

def click():
    messagebox.showwarning(title='Warning Message', message="I am Warning You!")  

def click():
    messagebox.showerror(title='Error Message', message="Danger, Danger!")

def click():
    if messagebox.askokcancel(title='ask ok cancel', message='What do you want to do?'):
        print('Continue')
    else:
        print('Stop! I Want Out of Here!')

def click():
    if messagebox.askretrycancel(title='ask retry cancel', message='Do you want to try again?'):
        print('You tried again')
    else:
        print('Stop! I Want Out of Here!')

def click():
    if messagebox.askyesno(title='ask yes/no', message='Do you like chicken?'):
        print('You like chicken')
    else:
        print("Why don't you like chicken?")

def click():
    answer = messagebox.askyesnocancel(title= 'Yes no cancel', message ='Do you like Python & Tkinter?')
    if(answer==True):
        print('You like to code!') 
    elif(answer==False):
        print('Then you need to take another computer programming language. Please try C+!')
    else:
        print('I need some answer here!')

'''

# To custom set an icon in the message box
def click():
    answer = messagebox.askyesnocancel(title= 'Yes no cancel', 
                                    message ='Do you like Python & Tkinter?',
                                    icon='error' )

    if(answer==True):
        print('You like to code!') 
    elif(answer==False):
        print('Then you need to take another computer programming language. Please try C+!')
    else:
        print('I need some answer here!')

button = Button(window, text ='click me!', command=click)
button.pack()


window.mainloop()