from tkinter import *
from VSF import VerticalScrolledFrame
from PIL import ImageTk, Image

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
frame.pack(fill=BOTH, expand=True)


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
        bleLesson()

    Button(win, text=" > Наступна тема > ", command=nextLesson).pack(anchor=SE, pady=10, padx=10)
    win.pack(fill=BOTH, expand=True)


# Вікно кнопки "Button, Label, Entry"
def bleLesson():
    global w, h, codeFont
    window = Toplevel(root)
    window.geometry("600x700+{}+{}".format(w, h))
    window.resizable(False, False)
    window.title('Button, Label, Entry')
    window.iconbitmap('icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("texts/bleLesson/1.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    f = open("texts/bleLesson/2.txt", 'r', encoding="utf-8")
    text2 = f.read()
    f.close()
    f = open("texts/bleLesson/3.txt", 'r', encoding="utf-8")
    text3 = f.read()
    f.close()

    Label(win, text='Віджети Button, Label, Entry', font=('Trebuchet MS', 22, "bold"), anchor=N).pack(pady=20)
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, text='Button - кнопка', font=('Trebuchet MS', 22, "bold")).pack()
    Label(win, text=text2, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text2
    Label(win, height=18, text="""
from tkinter import *

root = Tk()
b1 = Button(text="Натисни на мене", width=15,
     height=3)

def change():
    b1['text'] = "Натиснуто"
    b1['bg'] = '#000000'
    b1['activebackground'] = '#555555'
    b1['fg'] = '#ffffff'
    b1['activeforeground'] = '#ffffff'

b1.config(command=change)

b1.pack()
root.mainloop()
        """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    Label(win, text=text3, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text3
    Label(win, text="До:", font=('Comic Sans MS', 14, 'bold'), fg="darkgrey", justify=CENTER).pack(pady=10)
    image1 = ImageTk.PhotoImage(file='images/button/1.gif')
    labelImage1 = Label(win, image=image1)
    labelImage1.image = image1
    labelImage1.pack()
    del image1
    del labelImage1
    Label(win, text="Після:", font=('Comic Sans MS', 14, 'bold'), fg="darkgrey", justify=CENTER).pack(pady=10)
    image2 = ImageTk.PhotoImage(file='images/button/2.gif')
    labelImage2 = Label(win, image=image2)
    labelImage2.image = image2
    labelImage2.pack()
    del image2
    del labelImage2
    Label(win, text="Кнопка затиснута:", font=('Comic Sans MS', 14, 'bold'), fg="darkgrey",
          justify=CENTER).pack(pady=10)
    image3 = ImageTk.PhotoImage(file='images/button/3.gif')
    labelImage3 = Label(win, image=image3)
    labelImage3.image = image3
    labelImage3.pack()
    del image3
    del labelImage3

    def example():
        app = Tk()
        app.title('Тестування кнопки')

        # Створення кнопки
        button = Button(app, width=40, height=10, text='Натисни на мене')

        # конфігурація для кнопки
        def change():
            button['text'] = 'Натиснуто'  # змінюємо текст на кнопці
            button['activebackground'] = '#555555'  # змінюємо колір кнопки при зажимі кнопки
            button['bg'] = '#000000'  # змінюємо колір кнопки при натисканні на неї
            button['fg'] = '#ffffff'  # змінюємо колір шрифту при зажимі кнопки
            button['activeforeground'] = '#ffffff'  # зміна кольору шрифту при зажимі кнопки

        button.config(command=change)  # запуск функції конфігурації change() при натисканні
        button.pack()
        app.mainloop()

    Button(win, width=300, height=30, text="Запустити цю програму", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example

    f = open('texts/bleLesson/4.txt', 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    f = open('texts/bleLesson/5.txt', 'r', encoding="utf-8")
    text2 = f.read()
    f.close()
    f = open('texts/bleLesson/6.txt', 'r', encoding="utf-8")
    text3 = f.read()
    f.close()
    f = open('texts/bleLesson/7.txt', 'r', encoding="utf-8")
    text4 = f.read()
    f.close()

    Label(win, text='Label - мітка', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    Label(win, height=12, text="""
from tkinter import *
root = Tk()
root.title('Мітки')
label1 = Label(text="Перша мітка", 
    font='Arial', bd=17, bg='Aqua')
label2 = Label(text="Друга мітка", 
    font=('Comic Sans MS',24, 'bold'),
        bd=21, bg='#FF3636')
label1.pack()
label2.pack()
root.mainloop()
    """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    Label(win, text=text2, font=('Trebuchet MS', 12), justify=LEFT).pack()
    Label(win, text="Результат:", font=('Comic Sans MS', 14, 'bold'), fg="darkgrey", justify=CENTER).pack(pady=10)
    image1 = ImageTk.PhotoImage(file='images/label/1.gif')
    labelImage1 = Label(win, image=image1)
    labelImage1.image = image1
    labelImage1.pack()
    del image1
    del labelImage1
    Label(win, text=text3, font=('Trebuchet MS', 12), justify=LEFT).pack()
    Label(win, height=15, text="""
root = Tk()
root.title('Мітки')

def take():
    button.destroy()
    label['text'] = 'Отримано!'

Label(text='Пункт видачі', 
        font=("Arial", 18)).pack()
button = Button(text='Отримати',
        command=take)
label = Label(width=10,height=1)
button.pack()
label.pack()
root.mainloop()
        """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    Label(win, text="Запуск програми:", font=('Comic Sans MS', 14, 'bold'), fg="darkgrey",
          justify=CENTER).pack(pady=10)
    image1 = ImageTk.PhotoImage(file='images/label/2.gif')
    labelImage1 = Label(win, image=image1)
    labelImage1.image = image1
    labelImage1.pack()
    del image1
    del labelImage1
    Label(win, text="Натиснули на кнопку:", font=('Comic Sans MS', 14, 'bold'), fg="darkgrey",
          justify=CENTER).pack(pady=10)
    image1 = ImageTk.PhotoImage(file='images/label/3.gif')
    labelImage1 = Label(win, image=image1)
    labelImage1.image = image1
    labelImage1.pack()
    del image1, labelImage1

    def example():
        app = Tk()
        app.title('Мітки')

        # Також мітки і кнопки можна використовувати без прив'язки їх до змінних, якщо до них не потрібно звертатись
        # В даному прикладі тільки 1 мітка з 2-ох прив'язана до змінної, так як вона взаємодіє з функцією take()
        # Інша в ході програми корегуватися не буде, тому до змінної можемо її не прив'язувати

        def take():  # функція-команда для кнопки
            button.destroy()  # видаляємо кнопку після натиску
            label['text'] = 'Отримано!'  # виводимо мітку після натиску кнопки

        Label(app, text='Пункт видачі',
              font=("Arial", 18)).pack()  # Так як ця мітка не прив'язана до змінної, розмістити її
        # потрібно одразу через вказання .pack() в кінці

        button = Button(app, text='Отримати',
                        command=take)  # "command=take" - звернення до функції take() при натисканні
        label = Label(app, width=10,
                      height=1)  # пуста мітка, розмірами 10х1, яка буде запонена при натисканні на кнопку

        button.pack()
        label.pack()

        app.mainloop()

    Button(win, width=300, height=30, text="Запустити цю програму", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example
    Label(win, text=text4, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1, text2, text3, text4

    f = open('texts/bleLesson/8.txt', 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    f = open('texts/bleLesson/9.txt', 'r', encoding="utf-8")
    text2 = f.read()
    f.close()
    f = open('texts/bleLesson/10.txt', 'r', encoding="utf-8")
    text3 = f.read()
    f.close()

    Label(win, text='Entry - однострокове текстове поле', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    Label(win, height=12, text="""
from tkinter import *
root = Tk()
root.title('Введення')
entry = Entry(width=50)

def insertion():
    entry.insert(0, 'Tkinter - GUI ') 

button = Button(text='Ввести', command=insertion)
entry.pack()
button.pack()
root.mainloop()
        """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    Label(win, text=text2, font=('Trebuchet MS', 12), justify=LEFT).pack()
    Label(win, text="Программа:", font=('Comic Sans MS', 14, 'bold'), fg="darkgrey",
          justify=CENTER).pack(pady=10)
    image1 = ImageTk.PhotoImage(file='images/entry/1.gif')
    labelImage1 = Label(win, image=image1)
    labelImage1.image = image1
    labelImage1.pack()
    del image1, labelImage1

    def example():
        app = Tk()
        app.title('Введення')
        entry = Entry(app, width=50)

        def insertion():
            entry.insert(0, 'Tkinter - GUI ')

        button = Button(app, text='Ввести', command=insertion)
        entry.pack()
        button.pack()
        app.mainloop()

    Button(win, width=300, height=30, text="Запустити цю програму", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example
    Label(win, text=text3, font=('Trebuchet MS', 12), justify=LEFT).pack()

    del text1, text2, text3

    f = open('texts/bleLesson/11.txt', 'r', encoding="utf-8")
    text1 = f.read()
    f.close()

    Label(win, text='Практичне завдання', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1

    def example():
        app = Tk()
        app.title('Практика')

        entry = Entry(app, width=20)

        # Команди введення для кожного кольору
        def redInsert():
            entry.delete(0, END)  # в методі .delete(), аргументи 0 та END - Початковий та кінцевий символ
            # з яких по який треба стерти
            entry.insert(0, "#ff0000")

        def orangeInsert():
            entry.delete(0, END)
            entry.insert(0, "#ff7d00")

        def yellowInsert():
            entry.delete(0, END)
            entry.insert(0, "#ffff00")

        def greenInsert():
            entry.delete(0, END)
            entry.insert(0, "#00ff00")

        def cyanInsert():
            entry.delete(0, END)
            entry.insert(0, "#007dff")

        def blueInsert():
            entry.delete(0, END)
            entry.insert(0, "#0000ff")

        def purpleInsert():
            entry.delete(0, END)
            entry.insert(0, "#7d00ff")

        redButton = Button(app, bg='#ff0000', width=20, command=redInsert)
        orangeButton = Button(app, bg='#ff7d00', width=20, command=orangeInsert)
        yellowButton = Button(app, bg='#ffff00', width=20, command=yellowInsert)
        greenButton = Button(app, bg='#00ff00', width=20, command=greenInsert)
        cyanButton = Button(app, bg='#007dff', width=20, command=cyanInsert)
        blueButton = Button(app, bg='#0000ff', width=20, command=blueInsert)
        purpleButton = Button(app, bg='#7d00ff', width=20, command=purpleInsert)
        entry.pack()
        redButton.pack()
        orangeButton.pack()
        yellowButton.pack()
        greenButton.pack()
        cyanButton.pack()
        blueButton.pack()
        purpleButton.pack()
        app.mainloop()

    Button(win, width=300, height=30, text="Запустити зразок", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example

    def nextLesson():
        window.destroy()
        packLesson()

    def preLesson():
        window.destroy()
        whatistkinter()

    frame = Frame(win)
    Button(frame, text=" < Попередня тема < ", command=preLesson).pack(side=LEFT, anchor=SW, pady=10, padx=10)
    Button(frame, text=" > Наступна тема > ", command=nextLesson).pack(side=LEFT, anchor=SE, pady=10, padx=10)
    frame.pack()
    del frame
    win.pack(fill=BOTH, expand=True)


def packLesson():
    global w, h, codeFont
    window = Toplevel(root)
    window.geometry("600x700+{}+{}".format(w, h))
    window.resizable(False, False)
    window.title('метод pack()')
    window.iconbitmap('icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("texts/packLesson/1.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()

    Label(win, text='Метод pack()', font=('Trebuchet MS', 22, "bold"), anchor=N).pack(pady=20)
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, height=6, text="""
...
l1 = Label(width=7, height=4, bg='yellow', text="1")
l2 = Label(width=7, height=4, bg='orange', text="2")
l3 = Label(width=7, height=4, bg='lightgreen', text="3")
l4 = Label(width=7, height=4, bg='lightblue', text="4")
...
            """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    frame = Frame(win)
    Label(frame, text='l1.pack()\nl2.pack()\nl3.pack()\nl4.pack()', font=('Trebuchet MS', 18)).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='images/pack/1.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    frame = Frame(win)
    Label(frame, text='l1.pack(side=BOTTOM)\nl2.pack(side=BOTTOM)\nl3.pack(side=BOTTOM)\nl4.pack(side=BOTTOM)',
          font=('Trebuchet MS', 18)).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='images/pack/2.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    frame = Frame(win)
    Label(frame, text='l1.pack(side=LEFT)\nl2.pack(side=LEFT)\nl3.pack(side=LEFT)\nl4.pack(side=LEFT)',
          font=('Trebuchet MS', 18)).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='images/pack/3.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    frame = Frame(win)
    Label(frame, text='l1.pack(side=RIGHT)\nl2.pack(side=RIGHT)\nl3.pack(side=RIGHT)\nl4.pack(side=RIGHT)',
          font=('Trebuchet MS', 18)).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='images/pack/4.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    frame = Frame(win)
    Label(frame, text='l1.pack(side=TOP)\nl2.pack(side=BOTTOM)\nl3.pack(side=RIGHT)\nl4.pack(side=LEFT)',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='images/pack/5.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    f = open("texts/packLesson/2.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, height=24, text="""
from tkinter import *

root = Tk()
root.title('pack()')
frame_top = Frame(root) 
frame_bottom = Frame(root) 

l1 = Label(frame_top, width=10, height=5, 
            bg="orange", text="1")
l2 = Label(frame_top, width=10, height=5, 
            bg="yellow", text="2")
l3 = Label(frame_bottom, width=10, height=5, 
            bg="lightblue", text="3")
l4 = Label(frame_bottom, width=10, height=5, 
            bg="lightgreen", text="4")

frame_top.pack()
frame_bottom.pack()
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack(side=LEFT)
l4.pack(side=LEFT)

root.mainloop()
                """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    frame = Frame(win)
    Label(frame, text='Результат: ',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='images/pack/6.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    f = open("texts/packLesson/3.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, height=24, text="""
from tkinter import *

root = Tk()
frame_top = LabelFrame(text='Верх')
frame_bottom = LabelFrame(text='Низ')

l1 = Label(frame_top, width=7, height=4, 
                bg='yellow', text="1")
l2 = Label(frame_top, width=7, height=4, 
                bg='orange', text="2")
l3 = Label(frame_bottom, width=7, height=4, 
                bg='lightgreen', text="3")
l4 = Label(frame_bottom, width=7, height=4, 
                bg='lightblue', text="4")

frame_top.pack()
frame_bottom.pack()
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack(side=LEFT)
l4.pack(side=LEFT)

root.mainloop()
                    """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    frame = Frame(win)
    Label(frame, text='Результат: ',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='images/pack/7.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    f = open("texts/packLesson/4.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    frame = Frame(win)
    Label(frame, text='frame.pack(padx=10, pady=10)\nlabel1.pack(side=LEFT)\nlabel2.pack(side=LEFT)',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='images/pack/8.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    frame = Frame(win)
    Label(frame, text='frame.pack(ipadx=10, ipady=10)\nlabel1.pack(side=LEFT)\nlabel2.pack(side=LEFT)',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='images/pack/9.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    f = open("texts/packLesson/5.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    frame = Frame(win)
    Label(frame, text='frame.pack(side=LEFT, \n         padx=10, pady=10)\nlabel1.pack()\nlabel2.pack()',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='images/pack/10.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    f = open("texts/packLesson/6.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, height=10, text="""
from tkinter import *

root = Tk()
root.geometry("500x300") 

label = Label(width=40, height=10, 
        bg="lightblue", text="Звичайна мітка")
label.pack()

root.mainloop()
                        """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    f = open("texts/packLesson/7.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    frame = Frame(win)
    Label(frame, text='Результат: ',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=TOP)
    image1 = ImageTk.PhotoImage(file='images/pack/11.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=TOP, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    f = open("texts/packLesson/8.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, height=3, text="""
...
label.pack(expand=1)
...
                            """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    frame = Frame(win)
    Label(frame, text='Результат: ',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=TOP)
    image1 = ImageTk.PhotoImage(file='images/pack/12.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=TOP, pady=10)
    frame.pack()
    del frame, image1, labelImage1
    f = open("texts/packLesson/9.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, height=3, text="""
...
label.pack(expand=1, fill=Y)
...
                                """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    frame = Frame(win)
    Label(frame, text='Результат: ',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=TOP)
    image1 = ImageTk.PhotoImage(file='images/pack/13.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=TOP, pady=10)
    frame.pack()
    del frame, image1, labelImage1
    f = open("texts/packLesson/10.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, height=3, text="""
...
label.pack(expand=1, anchor=SE)
...
                                    """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT,
          font=codeFont).pack()
    frame = Frame(win)
    Label(frame, text='Результат: ',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=TOP)
    image1 = ImageTk.PhotoImage(file='images/pack/14.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=TOP, pady=10)
    frame.pack()
    del frame, image1, labelImage1

    f = open('texts/packLesson/11.txt', 'r', encoding="utf-8")
    text1 = f.read()
    f.close()

    Label(win, text='Практичне завдання', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1

    def example():
        app = Tk()
        app.title('Практика')
        label = Label(app)
        entry = Entry(app, width=20)
        frame = Frame(app)

        # Команди введення для кожного кольору
        def redInsert():
            entry.delete(0, END)  # в методі .delete(), аргументи 0 та END - Початковий та кінцевий символ
            # з яких по який треба стерти
            entry.insert(0, "#ff0000")
            label['text'] = 'Червоний'

        def orangeInsert():
            entry.delete(0, END)
            entry.insert(0, "#ff7d00")
            label['text'] = 'Помаранчевий'

        def yellowInsert():
            entry.delete(0, END)
            entry.insert(0, "#ffff00")
            label['text'] = 'Жовтий'

        def greenInsert():
            entry.delete(0, END)
            entry.insert(0, "#00ff00")
            label['text'] = 'Зелений'

        def cyanInsert():
            entry.delete(0, END)
            entry.insert(0, "#007dff")
            label['text'] = 'Голубий'

        def blueInsert():
            entry.delete(0, END)
            entry.insert(0, "#0000ff")
            label['text'] = 'Синій'

        def purpleInsert():
            entry.delete(0, END)
            entry.insert(0, "#7d00ff")
            label['text'] = 'Фіолетовий'

        redButton = Button(frame, bg='#ff0000', width=5, command=redInsert)
        orangeButton = Button(frame, bg='#ff7d00', width=5, command=orangeInsert)
        yellowButton = Button(frame, bg='#ffff00', width=5, command=yellowInsert)
        greenButton = Button(frame, bg='#00ff00', width=5, command=greenInsert)
        cyanButton = Button(frame, bg='#007dff', width=5, command=cyanInsert)
        blueButton = Button(frame, bg='#0000ff', width=5, command=blueInsert)
        purpleButton = Button(frame, bg='#7d00ff', width=5, command=purpleInsert)
        label.pack(pady=10)
        entry.pack()
        frame.pack(pady=10, padx=10)
        redButton.pack(side=LEFT)
        orangeButton.pack(side=LEFT)
        yellowButton.pack(side=LEFT)
        greenButton.pack(side=LEFT)
        cyanButton.pack(side=LEFT)
        blueButton.pack(side=LEFT)
        purpleButton.pack(side=LEFT)
        app.mainloop()

    Button(win, width=300, height=30, text="Запустити зразок", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example
    def nextLesson():
        window.destroy()
        #textLesson()

    def preLesson():
        window.destroy()
        bleLesson()
    frame = Frame(win)
    Button(frame, text=" < Попередня тема < ", command=preLesson).pack(side=LEFT, anchor=SW, pady=10, padx=10)
    Button(frame, text=" > Наступна тема > ", command=nextLesson).pack(side=LEFT, anchor=SE, pady=10, padx=10)
    frame.pack()
    del frame
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
                 anchor=W, font=butFont, command=bleLesson)
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


root.mainloop()
