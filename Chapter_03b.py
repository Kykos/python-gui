# List boxes

from tkinter import *

def submit():
    print("Your choice of transportation is: ", listbox.get(listbox.curselection()))
    # print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height = listbox.size())

def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

window=Tk()
window.title("I am a ListBox")
window.geometry("500x400")
window.config(background="#400a84")
icon = PhotoImage(file='images\icon.png')
window.iconphoto(TRUE, icon)
listbox = Listbox(window,
                font =("Constantia",15),
                fg = "#f0f4f5",
                bg = "#01211e",
                width = 28,
                relief = RAISED,
                bd =5                      
                )
listbox.pack()

listbox.insert(1, 'Airplane')
listbox.insert(2, 'Boat')
listbox.insert(3, 'Car')
listbox.insert(4, 'Bike')
listbox.insert(5, 'Train')

listbox.config(height=listbox.size())

entrybox = Entry(window)
entrybox.pack()

submitbutton = Button(window, text ='submit', command = submit)
submitbutton.pack()

addbutton = Button(window, text='add', command = add)
addbutton.pack()

deletebutton = Button(window, text='delete', command=delete)
deletebutton.pack()

window.mainloop()