from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('help')
#root.iconbitmap('/home/anxiety/Downloads/test.ico')
button_quit = Button(root, text='exit', command=root.quit)
button_quit.pack()



my_img = ImageTk.PhotoImage(Image.open("/home/anxiety/Documents/GitHub/bash/tkinter/8.jpg"))

my_label = Label(image=my_img)

my_label.pack()




root.mainloop()