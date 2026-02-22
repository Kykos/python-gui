# Menu bar

from tkinter import *

def openFile():
       print('File is Open')  
def saveFile():
       print('File is Saved')
def quit():
    window.destroy()

def cut():
    print('Cut')
def copy():
    print('Copy')
def paste():
    print('Paste')
      

window = Tk()
window.title('Menu Bar')
window.geometry('400x400')
window.config(background='#b7787a')

icon = PhotoImage(file='images\icon.png')
window.iconphoto(True, icon)

openImage = PhotoImage(file='images\openSmall.png')
saveImage = PhotoImage(file='images\saveSmall.png')
exitImage = PhotoImage(file='images\exitSmall.png') 

menubar = Menu(window)
window.config(menu=menubar)

# File menu
fileMenu =Menu(menubar, tearoff=0, font= ('Lucida Calligraphy',11), bg='#ddadaf', fg='#fcf7f7')
menubar.add_cascade(label='File', menu=fileMenu) 
fileMenu.add_command(label='Open',command=openFile, image=openImage, compound=LEFT)
fileMenu.add_command(label='Save', command=saveFile, image=saveImage, compound=LEFT) 
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=quit, image=exitImage, compound=LEFT)

# Edit menu
editMenu = Menu(menubar, tearoff=0, font= ('Lucida Calligraphy',11), bg='#ddadaf', fg='#fcf7f7')
menubar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label='Copy', command=copy)
editMenu.add_separator()
editMenu.add_command(label='Paste', command=paste)



window.mainloop()






