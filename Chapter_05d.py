# Grid

from tkinter import *
def getvals():
    print("The value of username is", uservalue.get())
    print("The value of password is", passvalue.get())
    
window = Tk()
window.title("The Grid")
window.geometry('400x350')
window.config(background='#b7787a')

icon = PhotoImage(file='images/icon.png')
window.iconphoto(True, icon)

user = Label(window, text="Username", font=('Lucida Calligraphy', 11), bg="#b7787a", fg="#fcf7f7")
user.grid()
password = Label(window, text="Password", font=('Lucida Calligraphy', 11), bg="#b7787a", fg="#fcf7f7")
password.grid(row=1)

# Set these values to be StringVar
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(window, textvariable=uservalue, width = 20, font=('Lucida Calligraphy', 11), bg="#ddadaf", fg="#652517")
passentry = Entry(window, textvariable=passvalue, width = 20, font=('Lucida Calligraphy', 11), bg="#ddadaf", fg="#652517")

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1) 

Button(text="Submit", command=getvals).grid()

window.mainloop()
