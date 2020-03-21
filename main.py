from tkinter import *
from VSF import VerticalScrolledFrame

root = Tk()

# Placing window on screen
w = root.winfo_screenwidth()
w = w//2
h = 20
root.geometry("600x820+{}+{}".format(w, h))
root.iconbitmap("icon.ico")
root.title('Самовчитель по tkinter')
root.resizable(False, False)
codeFont = ("Courier New", 12)

# Setting default image and font for each button
buttonImage = PhotoImage(file="images/buttonImage.gif")
butFont = ("Trebuchet MS", 12)

lab1 = Label(root, text="Tkinter. Програмування GUI на мові Python. Курс",
             font=("Franklin Gothic Medium", 14, 'bold'), anchor=W)
lab1.place(x=80, y=10)

# Create buttons on main window
button1 = Button(root, width=300, height=30, text=" Що таке tkinter?", compound='left', image=buttonImage,
                 anchor=W, font=butFont)
button1.place(x=150, y=50)

button2 = Button(root, width=300, height=30, text=" Button, Label, Entry", compound='left', image=buttonImage,
                 anchor=W, font=butFont)
button2.place(x=150, y=100)

button3 = Button(root, width=300, height=30, text=" метод pack()", compound='left', image=buttonImage,
                 anchor=W, font=butFont)
button3.place(x=150, y=150)

button4 = Button(root, width=300, height=30, text=" Text - велике текстове поле",
                 compound='left', image=buttonImage, anchor=W, font=butFont)
button4.place(x=150, y=200)

button5 = Button(root, width=300, height=30, text=" Radiobutton, Checkbutton", compound='left', image=buttonImage,
                 anchor=W, font=butFont)
button5.place(x=150, y=250)

button6 = Button(root, width=300, height=30, text=" віджет Listbox()", compound='left', image=buttonImage,
                 anchor=W, font=butFont)
button6.place(x=150, y=300)

button7 = Button(root, width=300, height=30, text=" метод bind()", compound='left', image=buttonImage,
                 anchor=W, font=butFont)
button7.place(x=150, y=350)

button8 = Button(root, width=300, height=30, text=" Події", compound='left', image=buttonImage, anchor=W
                 , font=butFont)
button8.place(x=150, y=400)

button9 = Button(root, width=300, height=30, text=" Canvas", compound='left', image=buttonImage, anchor=W,
                 font=butFont)
button9.place(x=150, y=450)

button10 = Button(root, width=300, height=30, text=" Canvas. Ідентифікатори та теги",
                  compound='left', image=buttonImage, anchor=W, font=butFont)
button10.place(x=150, y=500)

button11 = Button(root, width=300, height=30, text=" Вікна", compound='left', image=buttonImage, anchor=W,
                  font=butFont)
button11.place(x=150, y=550)

button12 = Button(root, width=300, height=30, text=" метод grid()", compound='left', image=buttonImage,
                  anchor=W, font=butFont)
button12.place(x=150, y=600)

button13 = Button(root, width=300, height=30, text=" Діалогові вікна", compound='left', image=buttonImage,
                  anchor=W, font=butFont)
button13.place(x=150, y=650)

button14 = Button(root, width=300, height=30, text=" Віджет Menu()", compound='left', image=buttonImage,
                  anchor=W, font=butFont)
button14.place(x=150, y=700)

button15 = Button(root, width=300, height=30, text=" метод place()", compound='left', image=buttonImage, anchor=W
                  , font=butFont)
button15.place(x=150, y=750)

root.mainloop()
