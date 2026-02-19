from tkinter import *
window = Tk()
window.title('This is an entry widget')
window.geometry("600x100")
window.config(background="#400a84")
icon=PhotoImage(file="images\icon.png")
window.iconphoto(True, icon)

def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)
def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1,END)

entry = Entry(window,
             font=("Georgia", 25),
             bg = "#400a84",
             fg="#ffffff", 
             )

entry.insert(0, "Please enter your name")
entry.pack(side=LEFT)

password_label = Label(window,
                    text = "Password:",
                    font = ('Arial', 15, 'bold'),
                    fg = '#a05a5d',            # forground color
                    bg = '#e4bdbf',            # background color
                    relief = RAISED
)
password_label.config(bg='#e4bdbf', fg="black")
password_label.pack()

password = Entry(window,
             font=("Georgia", 15),
             bg = "#400a84",
             fg="#ffffff", 
             show = "*"
             )

password.insert(0, "Please Password")
password.pack(side=BOTTOM)

submitButton = Button(window, text='submit', command = submit)
submitButton.pack(side=RIGHT)

delete_button =Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button =Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()
L