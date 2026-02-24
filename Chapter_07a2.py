# Progress Bar
from tkinter import *
from tkinter.ttk import *
import time
def start():
    GB = 100
    download = 0
    speed = 1
    bar['value']=0
    while(download < GB):
        time.sleep(0.1)
        bar['value'] +=(speed/GB)*100   # increase by 10
        download += speed
        percent.set(str(int((download/GB)*100))+'%')
        text.set(str(int((download/GB)*100))+'/'+str(GB) + ' GB completed')
        window.update_idletasks()

window =Tk()

window.title('Progress bar')
window.geometry('400x200')
icon = PhotoImage(file='images/icon.png')
window.iconphoto=(TRUE, icon)

percent= StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length = 300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taskLabel=Label(window, textvariable = text).pack()

button = Button(window, text='download', command=start).pack()

window.mainloop()