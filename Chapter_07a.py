# Progress Bar
from tkinter import *
from tkinter.ttk import *
import time
def start():
    timesections = 10
    x = 0
    bar['value']=0
    while(x < timesections):
        time.sleep(1)
        bar['value'] +=10   # increase by 10
        x += 1
        percent.set(str(int((x/timesections)*100))+'%')
        text.set(str(x)+'/'+str(timesections) + ' tasks completed')
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