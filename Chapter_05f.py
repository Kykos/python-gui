from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Window Tabs")
window.geometry('400x400')

icon = PhotoImage(file='images/icon.png')
window.iconphoto(True, icon)

notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.pack(expand=TRUE, fill='both' )

Label(tab1, text='Hello, I am the text tab 1.', width=50, height=25, font=('Lucida Calligraphy', 11), bg='#b7787a', fg='#fcf7f7').pack()
Label(tab2, text='Hello, I am the text tab 2.', width=50, height=25, font=('Lucida Calligraphy', 11), bg='#2F5688', fg='#fcf7f7').pack()    


window.mainloop()
