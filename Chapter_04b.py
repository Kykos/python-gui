from tkinter import *
from tkinter import filedialog

window= Tk()
window.title('File Dialog')
window.geometry('400x400')

icon = PhotoImage(file = 'images\\icon.png')
window.iconphoto(True, icon)
# '\Temp\FoneTool', ExtraProjectFiles
def openFile():
    filepath = filedialog.askopenfilename(initialdir = 'ExtraProjectFiles', 
                                        title='Please choose the file that you want', 
                                        filetypes=(('text files', '*.txt'),
                                        ('all files', '*.*')))
    file = open(filepath, 'r')
    print(file.read())
    file.close()

def saveFile():
    file = filedialog.asksaveasfile(initialdir="ExtraProjectFiles",
        defaultextension='.txt',
    filetypes=[
        ('Text file', '.txt'),
        ('HTML file', '.html'),
        ('All files', '.*')
        
    
    ])

    if file is None:
        return
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()

buttonOpen = Button(window, text = 'Open', command = openFile)
buttonOpen.pack()

buttonSave = Button(text='save', command=saveFile)
buttonSave.pack()

text=Text(window, bg='light yellow', 
          font =('Ink Free', 25),
          height = 8,
          width=20,
          padx=20,
          pady=20,
          fg='purple')
text.pack()

window.mainloop()
