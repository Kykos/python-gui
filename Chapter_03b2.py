# List boxes with multiple selection

from tkinter import *

def submit():
    transportation = []
    for index in listbox.curselection():
        transportation.insert(index, listbox.get(index))
    print('Your choice of transportation')
    for index in transportation:
        print(index)

def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height = listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height = listbox.size())

window=Tk()
window.title("I am a ListBox")
window.geometry("500x400")
window.config(background="#01211e")
icon = PhotoImage(file='images\icon.png')
window.iconphoto(TRUE, icon)
listbox = Listbox(window,
                font =("Constantia",15),
                fg = "#f0f4f5",
                bg = "#01211e",
                width = 28,
                relief = RAISED,
                bd =5,
                selectmode = MULTIPLE                     
                )
listbox.pack()

listbox.insert(1, 'Airplane')
listbox.insert(2, 'Boat')
listbox.insert(3, 'Car')
listbox.insert(4, 'Bike')
listbox.insert(5, 'Train')

listbox.config(height=listbox.size())

entrybox = Entry(window, font=("Constantia", 15), width = 28, bg = "#01211e", fg='#f0f4f5')
entrybox.pack()

submitbutton = Button(window, text ='submit', command = submit, font=("Constantia", 15), width = 10, bg = "#01211e", fg="#f0f4f5", activeforeground = "#cff5cf", activebackground ="#124212" )
submitbutton.pack()

addbutton = Button(window, text='add', command = add, font=("Constantia", 15), width = 10, bg = "#01211e", fg='#f0f4f5', activeforeground = "#cff5cf", activebackground ="#124212")
addbutton.pack()

deletebutton = Button(window, text='delete', command=delete, font=("Constantia", 15), width = 10, bg = "#01211e", fg='#f0f4f5', activeforeground = "#cff5cf", activebackground ="#124212" )
deletebutton.pack()

window.mainloop()