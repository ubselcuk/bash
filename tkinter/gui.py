from tkinter import *

root = Tk()


e = Entry(root, width = 20,borderwidth = 5)
e.pack()
e.insert(0, 'Enter name! ')


def cliccck():
    testlabel = Label(root, text = e.get())
    testlabel.pack()

#xbutton = Button(root, text = 'click me!',state=DISABLED)
#xbutton = Button(root, text = 'click me!', padx=50 ,pady = 30,command = cliccck,fg = 'blue')
#xbutton = Button(root, text = 'enter name',bg = '#fff')
xbutton = Button(root, text = 'enter name',command = cliccck)
xbutton.pack()


root.mainloop()



 






















## creating label widget
#myLabel1 = Label(root, text = 'Hello World!')
#myLabel2 = Label(root, text = 'Anime kızları!')
#
#
##showing it onto the screen
#myLabel1.grid(row = 0, column = 0)
#myLabel2.grid(row = 1, column = 5)
#