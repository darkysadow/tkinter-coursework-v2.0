from tkinter import *
from VSF import VerticalScrolledFrame

root = Tk()

# Placing window on screen
w = root.winfo_screenwidth()
w = w//2
h = 20
root.geometry("600x700+{}+{}".format(w, h))
root.iconbitmap("icon.ico")
root.title('Самовчитель по tkinter')
root.resizable(False, False)
codeFont = ("Courier New", 12)
frame = VerticalScrolledFrame(root, borderwidth=2, relief=SUNKEN)
# frame.grid(column=0, row=0, sticky='nsew') # fixed size


def whatistkinter():
    global w, h, codeFont
    window = Toplevel(root)
    window.geometry("600x700+{}+{}".format(w, h))
    window.resizable(False, False)
    window.title('Що таке tkinter?')
    window.iconbitmap('icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("texts/tkinter/1.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    f = open("texts/tkinter/2.txt", 'r', encoding="utf-8")
    text2 = f.read()
    f.close()
    f = open("texts/tkinter/3.txt", 'r', encoding="utf-8")
    text3 = f.read()
    f.close()
    f = open("texts/tkinter/4.txt", 'r', encoding="utf-8")
    text4 = f.read()
    f.close()
    f = open("texts/tkinter/5.txt", 'r', encoding="utf-8")
    text5 = f.read()
    f.close()
    f = open("texts/tkinter/6.txt", 'r', encoding="utf-8")
    text6 = f.read()
    f.close()

    Label(win, text='Tkinter', font=('Trebuchet MS', 22, "bold"), anchor=N).pack()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    Label(win, height=2, text="root = Tk()", bg="black", bd=3,
          relief=GROOVE, fg="green", justify=CENTER, font=codeFont).pack()
    Label(win, text=text2, font=('Trebuchet MS', 12), justify=LEFT).pack()
    Label(win, height=3, text="""
    e = Entry(root, width=20)
    b = Button(root, text="Передати")
    l = Label(root, bg='black', fg='white', width=20)
    """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    Label(win, text=text3, font=('Trebuchet MS', 12), justify=LEFT).pack()
    Label(win, height=6, text="""
    def strToSortlist(event):
        s = e.get()
        s = s.split()
        s.sort()
        l['text'] = ' '.join(s)
    """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    Label(win, text=text4, font=('Trebuchet MS', 12), justify=LEFT).pack()
    Label(win, height=2, text="b.bind('<Button-1>', strToSortlist)", bg="black", bd=3, relief=GROOVE,
          fg="green", justify=LEFT, font=codeFont).pack()
    Label(win, text=text5, font=('Trebuchet MS', 12), justify=LEFT).pack()
    Label(win, height=5, text="""
    e.pack()
    b.pack()
    l.pack()
    """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    Label(win, text=text6, font=('Trebuchet MS', 12), justify=LEFT).pack()
    Label(win, height=2, text="root.mainloop()", bg="black", bd=3, relief=GROOVE,
          fg="green", justify=LEFT, font=codeFont).pack()

    def nextLesson():
        window.destroy()

    Button(win, text=" > Наступна тема > ", command=nextLesson).pack(anchor=SE, pady=10, padx=10)
    win.pack(fill=BOTH, expand=True)

# Setting default image and font for each button
buttonImage = PhotoImage(file="images/buttonImage.gif")
butFont = ("Trebuchet MS", 12)

lab1 = Label(frame, text="Tkinter. Програмування GUI на мові Python. Курс",
             font=("Franklin Gothic Medium", 14, 'bold'), anchor=W)
lab1.pack(padx=50)

# Create buttons on main window
button1 = Button(frame, width=300, height=30, text=" Що таке tkinter?", compound='left', image=buttonImage,
                 anchor=W, font=butFont, command=whatistkinter)
button1.pack(padx=140, pady=10)

button2 = Button(frame, width=300, height=30, text=" Button, Label, Entry", compound='left', image=buttonImage,
                 anchor=W, font=butFont)
button2.pack(padx=140)

button3 = Button(frame, width=300, height=30, text=" метод pack()", compound='left', image=buttonImage,
                 anchor=W, font=butFont)
button3.pack(padx=140, pady=10)

button4 = Button(frame, width=300, height=30, text=" Text - велике текстове поле",
                 compound='left', image=buttonImage, anchor=W, font=butFont)
button4.pack(padx=140)

button5 = Button(frame, width=300, height=30, text=" Radiobutton, Checkbutton", compound='left', image=buttonImage,
                 anchor=W, font=butFont)
button5.pack(padx=140, pady=10)

button6 = Button(frame, width=300, height=30, text=" віджет Listbox()", compound='left', image=buttonImage,
                 anchor=W, font=butFont)
button6.pack(padx=140)

button7 = Button(frame, width=300, height=30, text=" метод bind()", compound='left', image=buttonImage,
                 anchor=W, font=butFont)
button7.pack(padx=140, pady=10)

button8 = Button(frame, width=300, height=30, text=" Події", compound='left', image=buttonImage, anchor=W
                 , font=butFont)
button8.pack(padx=140)

button9 = Button(frame, width=300, height=30, text=" Canvas", compound='left', image=buttonImage, anchor=W,
                 font=butFont)
button9.pack(padx=140, pady=10)

button10 = Button(frame, width=300, height=30, text=" Canvas. Ідентифікатори та теги",
                  compound='left', image=buttonImage, anchor=W, font=butFont)
button10.pack(padx=140)

button11 = Button(frame, width=300, height=30, text=" Вікна", compound='left', image=buttonImage, anchor=W,
                  font=butFont)
button11.pack(padx=140, pady=10)

button12 = Button(frame, width=300, height=30, text=" метод grid()", compound='left', image=buttonImage,
                  anchor=W, font=butFont)
button12.pack(padx=140)

button13 = Button(frame, width=300, height=30, text=" Діалогові вікна", compound='left', image=buttonImage,
                  anchor=W, font=butFont)
button13.pack(padx=140, pady=10)

button14 = Button(frame, width=300, height=30, text=" Віджет Menu()", compound='left', image=buttonImage,
                  anchor=W, font=butFont)
button14.pack(padx=140)

button15 = Button(frame, width=300, height=30, text=" метод place()", compound='left', image=buttonImage, anchor=W
                  , font=butFont)
button15.pack(padx=140, pady=10)
frame.pack(fill=BOTH, expand=True)

root.mainloop()
