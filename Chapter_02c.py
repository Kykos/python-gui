from tkinter import *
window = Tk()
window.title('Radio Buttons')

window.geometry('300x300')

icon =PhotoImage(file='images\icon.png')
window.iconphoto(True, icon)
window.config(background='#e7c6c7')

saladImage = PhotoImage(file="images\salad.png")
steakImage = PhotoImage(file="images\steak.png")
dessertImage = PhotoImage(file="images\dessert.png")

foodImages=[saladImage, steakImage, dessertImage]
food = ['salad', 'steak', 'desert']
def order():
    if(x.get()==0):
        print('You ordered a salad!')
    elif(x.get()==1):
        print('You ordered a steak!')
    elif (x.get() == 2):
        print('You order dessert!')    
    else:
        print('huh?')

x= IntVar()

for index in range(len(food)):
    radioButton = Radiobutton(window,
                            font=("Helvetica", 18),
                            bg="#e7c6c7",
                            text  = food[index],
                            variable = x,
                            value=index,
                            pady = 10,
                            image = foodImages[index],
                            compound=LEFT,
                            indicatoron = 0, # Turn the radio button into clickable button
                            width = 175,      # width of the push buttons
                            command=order
                            )
    radioButton.pack()
window.mainloop()
