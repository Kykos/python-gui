from tkinter import *

window = Tk()
window.title=('Labels')
window.geometry('700x800')

icon =PhotoImage(file='images\icon.png')
window.iconphoto(True, icon)
window.config(background='#e4bdbf')

photo = PhotoImage(file="images\PandV.png")

label = Label(window, 
              text = "Python and VS Code GUI.This book is set to teach you everything you want to know about the GUI Python and VS Code.", 
              font = ('Arial', 40, 'bold'),
              fg = '#a05a5d',            # forground color
              bg = '#e4bdbf',            # background color
              wraplength = 550, 
              relief = RAISED,             # 
              bd = 5,                      # border debth
              padx = 20,                   # adding spaces to the sides
              pady = 20, 
              image = photo,               # adding spaces to the top and buttom
              compound = "bottom",         # Without this statement the image will be placed on top of the text
              )
label.config(bg='#e4bdbf', fg="black")
label.pack()

b_photo = PhotoImage(file="images\Press-Here.png"),

count = 0
def countMe():
    global count
    count += 1
    print(count)
button = Button(window, 
                text='Count Me',
                command = countMe,
                font =("Helvetica", 30),
                relief = GROOVE,
                bd= 7,
                fg = "#001400",
                bg = "#cff5cf",
                activeforeground = "#cff5cf",
                activebackground = "#124212",

                image = b_photo,
                compound = 'bottom', 
                )
button.pack()

window.mainloop()