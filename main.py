from tkinter import *
from VSF import VerticalScrolledFrame
from PIL import ImageTk, Image
import random as r

root = Tk()

# Placing window on screen
w = root.winfo_screenwidth()
w = w//2
h = 20
root.geometry("600x700+{}+{}".format(w, h))
root.iconbitmap("C:/python-learn/tkinter-coursework-2/icon.ico")
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
    window.iconbitmap('C:/python-learn/tkinter-coursework-2/icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("C:/python-learn/tkinter-coursework-2/texts/tkinter/1.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    f = open("C:/python-learn/tkinter-coursework-2/texts/tkinter/2.txt", 'r', encoding="utf-8")
    text2 = f.read()
    f.close()
    f = open("C:/python-learn/tkinter-coursework-2/texts/tkinter/3.txt", 'r', encoding="utf-8")
    text3 = f.read()
    f.close()
    f = open("C:/python-learn/tkinter-coursework-2/texts/tkinter/4.txt", 'r', encoding="utf-8")
    text4 = f.read()
    f.close()
    f = open("C:/python-learn/tkinter-coursework-2/texts/tkinter/5.txt", 'r', encoding="utf-8")
    text5 = f.read()
    f.close()
    f = open("C:/python-learn/tkinter-coursework-2/texts/tkinter/6.txt", 'r', encoding="utf-8")
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
    window.iconbitmap('C:/python-learn/tkinter-coursework-2/icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("C:/python-learn/tkinter-coursework-2/texts/bleLesson/1.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    f = open("C:/python-learn/tkinter-coursework-2/texts/bleLesson/2.txt", 'r', encoding="utf-8")
    text2 = f.read()
    f.close()
    f = open("C:/python-learn/tkinter-coursework-2/texts/bleLesson/3.txt", 'r', encoding="utf-8")
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
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/button/1.gif')
    labelImage1 = Label(win, image=image1)
    labelImage1.image = image1
    labelImage1.pack()
    del image1
    del labelImage1
    Label(win, text="Після:", font=('Comic Sans MS', 14, 'bold'), fg="darkgrey", justify=CENTER).pack(pady=10)
    image2 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/button/2.gif')
    labelImage2 = Label(win, image=image2)
    labelImage2.image = image2
    labelImage2.pack()
    del image2
    del labelImage2
    Label(win, text="Кнопка затиснута:", font=('Comic Sans MS', 14, 'bold'), fg="darkgrey",
          justify=CENTER).pack(pady=10)
    image3 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/button/3.gif')
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

    f = open('C:/python-learn/tkinter-coursework-2/texts/bleLesson/4.txt', 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    f = open('C:/python-learn/tkinter-coursework-2/texts/bleLesson/5.txt', 'r', encoding="utf-8")
    text2 = f.read()
    f.close()
    f = open('C:/python-learn/tkinter-coursework-2/texts/bleLesson/6.txt', 'r', encoding="utf-8")
    text3 = f.read()
    f.close()
    f = open('C:/python-learn/tkinter-coursework-2/texts/bleLesson/7.txt', 'r', encoding="utf-8")
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
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/label/1.gif')
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
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/label/2.gif')
    labelImage1 = Label(win, image=image1)
    labelImage1.image = image1
    labelImage1.pack()
    del image1
    del labelImage1
    Label(win, text="Натиснули на кнопку:", font=('Comic Sans MS', 14, 'bold'), fg="darkgrey",
          justify=CENTER).pack(pady=10)
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/label/3.gif')
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

    f = open('C:/python-learn/tkinter-coursework-2/texts/bleLesson/8.txt', 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    f = open('C:/python-learn/tkinter-coursework-2/texts/bleLesson/9.txt', 'r', encoding="utf-8")
    text2 = f.read()
    f.close()
    f = open('C:/python-learn/tkinter-coursework-2/texts/bleLesson/10.txt', 'r', encoding="utf-8")
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
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/entry/1.gif')
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

    f = open('C:/python-learn/tkinter-coursework-2/texts/bleLesson/11.txt', 'r', encoding="utf-8")
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
    window.iconbitmap('C:/python-learn/tkinter-coursework-2/icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("C:/python-learn/tkinter-coursework-2/texts/packLesson/1.txt", 'r', encoding="utf-8")
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
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/pack/1.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    frame = Frame(win)
    Label(frame, text='l1.pack(side=BOTTOM)\nl2.pack(side=BOTTOM)\nl3.pack(side=BOTTOM)\nl4.pack(side=BOTTOM)',
          font=('Trebuchet MS', 18)).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/pack/2.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    frame = Frame(win)
    Label(frame, text='l1.pack(side=LEFT)\nl2.pack(side=LEFT)\nl3.pack(side=LEFT)\nl4.pack(side=LEFT)',
          font=('Trebuchet MS', 18)).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/pack/3.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    frame = Frame(win)
    Label(frame, text='l1.pack(side=RIGHT)\nl2.pack(side=RIGHT)\nl3.pack(side=RIGHT)\nl4.pack(side=RIGHT)',
          font=('Trebuchet MS', 18)).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/pack/4.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    frame = Frame(win)
    Label(frame, text='l1.pack(side=TOP)\nl2.pack(side=BOTTOM)\nl3.pack(side=RIGHT)\nl4.pack(side=LEFT)',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/pack/5.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    f = open("C:/python-learn/tkinter-coursework-2/texts/packLesson/2.txt", 'r', encoding="utf-8")
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
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/pack/6.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    f = open("C:/python-learn/tkinter-coursework-2/texts/packLesson/3.txt", 'r', encoding="utf-8")
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
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/pack/7.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    f = open("C:/python-learn/tkinter-coursework-2/texts/packLesson/4.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    frame = Frame(win)
    Label(frame, text='frame.pack(padx=10, pady=10)\nlabel1.pack(side=LEFT)\nlabel2.pack(side=LEFT)',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/pack/8.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    frame = Frame(win)
    Label(frame, text='frame.pack(ipadx=10, ipady=10)\nlabel1.pack(side=LEFT)\nlabel2.pack(side=LEFT)',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/pack/9.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    f = open("C:/python-learn/tkinter-coursework-2/texts/packLesson/5.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    frame = Frame(win)
    Label(frame, text='frame.pack(side=LEFT, \n         padx=10, pady=10)\nlabel1.pack()\nlabel2.pack()',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=LEFT)
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/pack/10.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=LEFT, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    f = open("C:/python-learn/tkinter-coursework-2/texts/packLesson/6.txt", 'r', encoding="utf-8")
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
    f = open("C:/python-learn/tkinter-coursework-2/texts/packLesson/7.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    frame = Frame(win)
    Label(frame, text='Результат: ',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=TOP)
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/pack/11.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=TOP, pady=10)
    frame.pack()
    del image1, labelImage1, frame
    f = open("C:/python-learn/tkinter-coursework-2/texts/packLesson/8.txt", 'r', encoding="utf-8")
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
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/pack/12.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=TOP, pady=10)
    frame.pack()
    del frame, image1, labelImage1
    f = open("C:/python-learn/tkinter-coursework-2/texts/packLesson/9.txt", 'r', encoding="utf-8")
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
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/pack/13.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=TOP, pady=10)
    frame.pack()
    del frame, image1, labelImage1
    f = open("C:/python-learn/tkinter-coursework-2/texts/packLesson/10.txt", 'r', encoding="utf-8")
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
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/pack/14.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=TOP, pady=10)
    frame.pack()
    del frame, image1, labelImage1

    f = open('C:/python-learn/tkinter-coursework-2/texts/packLesson/11.txt', 'r', encoding="utf-8")
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
        textLesson()

    def preLesson():
        window.destroy()
        bleLesson()
    frame = Frame(win)
    Button(frame, text=" < Попередня тема < ", command=preLesson).pack(side=LEFT, anchor=SW, pady=10, padx=10)
    Button(frame, text=" > Наступна тема > ", command=nextLesson).pack(side=LEFT, anchor=SE, pady=10, padx=10)
    frame.pack()
    del frame
    win.pack(fill=BOTH, expand=True)


def textLesson():
    global w, h, codeFont
    window = Toplevel(root)
    window.geometry("600x700+{}+{}".format(w, h))
    window.resizable(False, False)
    window.title('Віджет Text()')
    window.iconbitmap('C:/python-learn/tkinter-coursework-2/icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("C:/python-learn/tkinter-coursework-2/texts/textLesson/1.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()

    Label(win, text='Text - Багатострокові текстові поля', font=('Trebuchet MS', 22, "bold"), anchor=N).pack(pady=20)
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, height=9, text="""
from tkinter import *

root = Tk()
text = Text(width=20, height=50, wrap=WORD, 
                bg="green", fg="white")
text.pack()

root.mainloop()

                """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()

    def example():
        app = Tk()
        text = Text(app, width=20, height=5, wrap=WORD,
                    bg="green", fg="white")
        text.pack()
        app.mainloop()

    Button(win, width=300, height=30, text="Запустити зразок", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example
    f = open("C:/python-learn/tkinter-coursework-2/texts/textLesson/2.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, text='Text та Scrollbar', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/textLesson/3.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, height=12, text="""
from tkinter import *

root = Tk()
text = Text(width=20, height=10, wrap=WORD)
text.pack(side=LEFT)

scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)
root.mainloop()
                    """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    frame = Frame(win)
    Label(frame, text='Результат: ',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=TOP)
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/text/1.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=TOP, pady=10)
    frame.pack()
    del frame, image1, labelImage1
    f = open("C:/python-learn/tkinter-coursework-2/texts/textLesson/4.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, text='Методи Text', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/textLesson/5.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, height=42, text="""
from tkinter import *


def insertText():   
    s = "Hello World!"
    text.insert(1.0, s)


def getText():  
    s = text.get(1.0, END)
    label['text'] = s


def deleteText():  
    text.delete(1.0, END)
    label['text'] = ""


root = Tk()
root.title('Керування текстом')


frame = Frame()

text = Text(width=30, height=7)
text.pack()
label = Label(width=30, height=7, fg="grey")
frame.pack()

b_insert = Button(frame, width=8, height=3, 
            text="Вставити", command=insertText)
b_insert.pack(side=LEFT)
b_get = Button(frame, width=8, height=3, 
            text="Отримати", command=getText)
b_get.pack(side=LEFT)
b_delete = Button(frame, width=8, height=3, 
            text="Видалити", command=deleteText)
b_delete.pack(side=LEFT)

label.pack()
root.mainloop()
                        """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    def example():
        def insertText():  # Функція котра буде вводити стрічку Hello World!
            s = "Hello World!"
            text.insert(1.0, s)

        def getText():  # Функція котра буде отриувати текст користувача, та виводити його в мітку
            s = text.get(1.0, END)
            label['text'] = s

        def deleteText():  # Функція яка буде видаляти текст з поля та мітки
            text.delete(1.0, END)
            label['text'] = ""
        app = Tk()
        frame = Frame(app)  # Рамка, в яку будуть зібрані кнопки

        text = Text(app, width=30, height=7)
        text.pack()
        label = Label(app, width=30, height=7, fg="grey")
        frame.pack()

        # Далі описані кнопки, якими ми будемо керувати текстом в полі та мітці

        b_insert = Button(frame, width=8, height=3, text="Вставити", command=insertText)
        b_insert.pack(side=LEFT)
        b_get = Button(frame, width=8, height=3, text="Отримати", command=getText)
        b_get.pack(side=LEFT)
        b_delete = Button(frame, width=8, height=3, text="Видалити", command=deleteText)
        b_delete.pack(side=LEFT)

        label.pack()
        app.mainloop()

    Button(win, width=300, height=30, text="Запустити зразок", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example
    f = open("C:/python-learn/tkinter-coursework-2/texts/textLesson/6.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, text='Теги', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/textLesson/7.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, height=13, text="""
from tkinter import *

root = Tk()
text = Text(width=30, height=10)
text.insert(1.0, "Перша лінія\nДруга лінія")

text.tag_add("firstLine", 1.0, "1.end")

text.tag_config('firstLine', font=("Comic Sans MS", 
                    18, "bold"), justify=CENTER)
text.pack()
root.mainloop()
                        """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    frame = Frame(win)
    Label(frame, text='Без тегів: ',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=TOP)
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/text/2.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=TOP, pady=10)
    frame.pack()
    del frame, image1, labelImage1
    frame = Frame(win)
    Label(frame, text='З тегами: ',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=TOP)
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/text/3.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=TOP, pady=10)
    frame.pack()
    del frame, image1, labelImage1
    f = open("C:/python-learn/tkinter-coursework-2/texts/textLesson/7.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, text='Вставка віджетів в текстове поле', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/textLesson/8.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, height=16, text="""
from tkinter import *

def smile():   
    label = Label(fg="white", bg="black", text=":D")
    text.window_create(INSERT, window=label)   

root = Tk()

text = Text(width=20, height=7, wrap=WORD)
text.pack()
button = Button(text=":D", command=smile)
button.pack()

root.mainloop()
                            """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()

    def example():

        def smile():  # Функція-команда для кнопки, яка буде вставляти в поле смайлик
            label = Label(app, fg="white", bg="black", text=":D")
            text.window_create(INSERT, window=label)  # INSERT - місце в яке вставляємо смайл, тобто там де курсор

        app = Tk()

        text = Text(app, width=20, height=7, wrap=WORD)
        text.pack()

        button = Button(app, text=":D", command=smile)
        button.pack()
        app.mainloop()

    Button(win, width=300, height=30, text="Запустити зразок", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example
    f = open("C:/python-learn/tkinter-coursework-2/texts/textLesson/9.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, text='Практична робота', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/textLesson/10.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/text/4.gif')
    labelImage1 = Label(win, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=TOP, pady=10)
    del image1, labelImage1

    def nextLesson():
        window.destroy()
        racheLesson()

    def preLesson():
        window.destroy()
        packLesson()
    frame = Frame(win)
    Button(frame, text=" < Попередня тема < ", command=preLesson).pack(side=LEFT, anchor=SW, pady=10, padx=10)
    Button(frame, text=" > Наступна тема > ", command=nextLesson).pack(side=LEFT, anchor=SE, pady=10, padx=10)
    frame.pack()
    del frame
    win.pack(fill=BOTH, expand=True)


# Radiobutton, Checkbutton
def racheLesson():
    global w, h, codeFont
    window = Toplevel(root)
    window.geometry("600x700+{}+{}".format(w, h))
    window.resizable(False, False)
    window.title('Radiobutton, Checkbutton')
    window.iconbitmap('C:/python-learn/tkinter-coursework-2/icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("C:/python-learn/tkinter-coursework-2/texts/racheLesson/1.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()

    Label(win, text='Radiobutton, Checkbutton. \nЗмінні Tkinter', font=('Trebuchet MS', 22, "bold"),
          anchor=N).pack(pady=20)
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, text='Radiobutton - радіокнопка', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/racheLesson/2.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, height=16, text="""
from tkinter import *

root = Tk()

r1 = Radiobutton(text="First") 
r2 = Radiobutton(text="Second")

r1.pack(anchor=W) 
r2.pack(anchor=W)

root.mainloop()
                                """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    frame = Frame(win)
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/radiobutton/1.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage1.pack(side=TOP, pady=10)
    frame.pack()
    del frame, image1, labelImage1
    Label(win, text='Radiobutton - радіокнопка', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/racheLesson/3.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, height=9, text="""
...
r_var = BooleanVar()
r_var.set(0)

r1 = Radiobutton(text="First", variable=r_var, value=0)
r2 = Radiobutton(text="Second", variable=r_var, value=1)
...
                                    """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT,
          font=codeFont).pack()
    f = open("C:/python-learn/tkinter-coursework-2/texts/racheLesson/4.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, height=34, text="""
from tkinter import *


# Функція зміни кольору
def change():
    if r_var.get() == 0:
        label['bg'] = "lightblue"
    elif r_var.get() == 1:
        label['bg'] = "lightgreen"
    elif r_var.get() == 2:
        label['bg'] = "pink"


root = Tk()

r_var = IntVar()
r_var.set(0)

r1 = Radiobutton(text="Blue", variable=r_var, value=0)
r2 = Radiobutton(text="Green", variable=r_var, value=1)
r3 = Radiobutton(text="Pink", variable=r_var, value=2)


r1.pack(anchor=W)   
r2.pack(anchor=W)
r3.pack(anchor=W)

button = Button(text="Змінити", command=change)
button.pack(pady=10)

label = Label(width=20, height=10)
label.pack()

root.mainloop()
                            """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT,
          font=codeFont).pack()

    def example():

        # Функція зміни кольору
        def change():
            if r_var.get() == 0:
                label['bg'] = "lightblue"
            elif r_var.get() == 1:
                label['bg'] = "lightgreen"
            elif r_var.get() == 2:
                label['bg'] = "pink"

        app = Tk()

        r_var = IntVar(app)
        r_var.set(0)

        r1 = Radiobutton(app, text="Blue", variable=r_var, value=0)
        r2 = Radiobutton(app, text="Green", variable=r_var, value=1)
        r3 = Radiobutton(app, text="Pink", variable=r_var, value=2)

        r1.pack(anchor=W)  # "Прибиваємо" їх на південь, тобто вниз для нормального вигляду
        r2.pack(anchor=W)
        r3.pack(anchor=W)

        button = Button(app, text="Змінити", command=change)
        button.pack(pady=10)

        label = Label(app, width=20, height=10)
        label.pack()

        app.mainloop()

    Button(win, width=300, height=30, text="Запустити програму", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example
    f = open("C:/python-learn/tkinter-coursework-2/texts/racheLesson/5.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, text='Checkbutton - прапорець', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/racheLesson/6.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    Label(win, height=18, text="""
from tkinter import *

root = Tk()

cb_var1 = BooleanVar()
cb_var1.set(0)
cb1 = Checkbutton(text="First", variable=cb_var1, 
                    onvalue=1, offvalue=0)
cb_var2 = BooleanVar()
cb_var2.set(0)
cb2 = Checkbutton(text="Second", variable=cb_var2, 
                    onvalue=1, offvalue=0)

cb1.pack()
cb2.pack()

root.mainloop()
                                """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT,
          font=codeFont).pack()
    frame = Frame(win)
    image1 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/radiobutton/2.gif')
    image2 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/radiobutton/3.gif')
    image3 = ImageTk.PhotoImage(file='C:/python-learn/tkinter-coursework-2/images/radiobutton/4.gif')
    labelImage1 = Label(frame, image=image1)
    labelImage1.image = image1
    labelImage2 = Label(frame, image=image2)
    labelImage2.image = image2
    labelImage3 = Label(frame, image=image3)
    labelImage3.image = image3
    labelImage1.pack(side=LEFT, pady=10)
    labelImage2.pack(side=LEFT, pady=10, padx=20)
    labelImage3.pack(side=LEFT, pady=10)
    frame.pack()
    del frame, image1, labelImage1, image2, labelImage2, image3, labelImage3
    f = open("C:/python-learn/tkinter-coursework-2/texts/racheLesson/7.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1

    Label(win, text='Практична робота', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/racheLesson/8.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1

    def example():
        def change():
            if r_var.get() == 1:
                label['text'] = "+38 (093) 25-1423-99"
            elif r_var.get() == 2:
                label['text'] = "+38 (097) 14-1635-24"
            elif r_var.get() == 3:
                label['text'] = "+38 (068) 21-3546-45"

        app = Tk()

        frame = Frame(app)

        r_var = IntVar(app)
        r_var.set(0)

        rb1 = Radiobutton(frame, text="Василь", indicatoron=0, variable=r_var, value=1, command=change, width=10)
        rb2 = Radiobutton(frame, text="Петро", indicatoron=0, variable=r_var, value=2, command=change, width=10)
        rb3 = Radiobutton(frame, text="Іван", indicatoron=0, variable=r_var, value=3, command=change, width=10)

        label = Label(app, width=30, height=8)

        frame.pack(side=LEFT)
        rb1.pack()
        rb2.pack()
        rb3.pack()
        label.pack(side=LEFT)

        app.mainloop()

    Button(win, width=300, height=30, text="Запустити зразок", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example

    def nextLesson():
        window.destroy()
        listboxLesson()

    def preLesson():
        window.destroy()
        textLesson()

    frame = Frame(win)
    Button(frame, text=" < Попередня тема < ", command=preLesson).pack(side=LEFT, anchor=SW, pady=10, padx=10)
    Button(frame, text=" > Наступна тема > ", command=nextLesson).pack(side=LEFT, anchor=SE, pady=10, padx=10)
    frame.pack()
    del frame
    win.pack(fill=BOTH, expand=True)


def listboxLesson():
    global w, h, codeFont
    window = Toplevel(root)
    window.geometry("600x700+{}+{}".format(w, h))
    window.resizable(False, False)
    window.title('Listbox()')
    window.iconbitmap('C:/python-learn/tkinter-coursework-2/icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("C:/python-learn/tkinter-coursework-2/texts/listboxLesson/1.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()

    Label(win, text='Віджет Listbox()', font=('Trebuchet MS', 22, "bold"),
          anchor=N).pack(pady=20)
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=23, text="""
from tkinter import *

root = Tk()

# Створюємо віджет Listbox та надаємо йому розміри
lbox = Listbox(width=25, height=10)
lbox.pack(side=LEFT)

# Створюємо скроллер для Listbox
scroll = Scrollbar(command=lbox.yview)
scroll.pack(fill=Y, side=LEFT)

lbox.config(yscrollcommand=scroll.set)

# Заповнюємо Listbox елементами від 0 до 25
for i in range(0, 26):
    lbox.insert(END, i)  
    # END виступає індексом списку, в який 
    # ми вставляємо елемент
    # якщо поставимо 0, все буде навпаки

root.mainloop()
                                    """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT,
          font=codeFont).pack()
    frame = Frame(win)
    Label(frame, text='Результат програми: ',
          font=('Trebuchet MS', 18), justify=LEFT).pack(pady=10, side=TOP)
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/listbox/1.gif")
    labelImage = Label(frame, image=image)
    labelImage.image = image
    labelImage.pack()
    del image, labelImage
    frame.pack()
    del frame
    f = open("C:/python-learn/tkinter-coursework-2/texts/listboxLesson/2.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=54, text="""
from tkinter import *


def addElement():
    # Додаємо елемент з поля в кінець списку
    lbox.insert(END, entry.get())
    entry.delete(0, END)


# Видаляємо виділені елементи в списку
def deleteElement():
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        lbox.delete(i)


# берігаємо створений список у файл listprogram.txt
def saveList():
    f = open("listprogram.txt", "w", encoding="utf-8")
    # Записуємо кожен елемент списку у 
    # файл з нової строки
    f.writelines("\ n".join(lbox.get(0, END))) 
    f.close()

root = Tk()

# Створюємо віджет Listbox та надаємо йому розміри
lbox = Listbox(width=25, height=10, 
                selectmode=EXTENDED)
lbox.pack(side=LEFT)

# Створюємо скроллер для Listbox
scroll = Scrollbar(command=lbox.yview)
scroll.pack(fill=Y, side=LEFT)

lbox.config(yscrollcommand=scroll.set)

frame = Frame(width=20)
frame.pack(side=LEFT, padx=10)
entry = Entry(frame, width=20)
entry.pack(anchor=N)
addBut = Button(frame, text="Додати", 
                    command=addElement)
addBut.pack(fill=X)
delBut = Button(frame, text="Видалити", 
                    command=deleteElement)
delBut.pack(fill=X)
saveBut = Button(frame, text="Зберегти", 
                    command=saveList)
saveBut.pack(fill=X)

root.mainloop()
                                        """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT,
          font=codeFont).pack()
    frame = Frame(win)
    Label(frame, text='Записуємо в текстове поле нове значення, \nта натискаємо кнопку "Додати"',
          font=('Trebuchet MS', 15), justify=LEFT).pack(pady=10, side=TOP)
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/listbox/2.gif")
    labelImage = Label(frame, image=image)
    labelImage.image = image
    labelImage.pack()
    del image, labelImage
    Label(frame, text='Виділяємо елементи, які бажаємо видалити, \nта натискаємо кнопку "Видалити"',
          font=('Trebuchet MS', 15), justify=LEFT).pack(pady=10, side=TOP)
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/listbox/3.gif")
    labelImage = Label(frame, image=image)
    labelImage.image = image
    labelImage.pack()
    del image, labelImage
    Label(frame, text='Маємо список, який бажаємо зберегти у файл \nта натискаємо кнопку "Зберегти"',
          font=('Trebuchet MS', 15), justify=LEFT).pack(pady=10, side=TOP)
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/listbox/4.gif")
    labelImage = Label(frame, image=image)
    labelImage.image = image
    labelImage.pack()
    del image, labelImage
    Label(frame, text='Для перевірки, відкриємо текстовий документ\nу який ми зберегли список:',
          font=('Trebuchet MS', 15), justify=LEFT).pack(pady=10, side=TOP)
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/listbox/5.gif")
    labelImage = Label(frame, image=image)
    labelImage.image = image
    labelImage.pack()
    del image, labelImage
    frame.pack()
    del frame
    f = open("C:/python-learn/tkinter-coursework-2/texts/listboxLesson/3.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, text='Практична робота', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/listboxLesson/4.txt", 'r', encoding="utf-8")
    text1 = f.read()
    f.close()
    Label(win, text=text1, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text1
    frame = Frame(win)
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/listbox/Practice.gif")
    labelImage = Label(frame, image=image)
    labelImage.image = image
    labelImage.pack()
    del image, labelImage
    frame.pack()
    del frame

    def nextLesson():
        window.destroy()
        bindLesson()

    def preLesson():
        window.destroy()
        racheLesson()

    frame = Frame(win)
    Button(frame, text=" < Попередня тема < ", command=preLesson).pack(side=LEFT, anchor=SW, pady=10, padx=10)
    Button(frame, text=" > Наступна тема > ", command=nextLesson).pack(side=LEFT, anchor=SE, pady=10, padx=10)
    frame.pack(pady=20)
    del frame
    win.pack(fill=BOTH, expand=True)


def bindLesson():
    global w, h, codeFont
    window = Toplevel(root)
    window.geometry("600x700+{}+{}".format(w, h))
    window.resizable(False, False)
    window.title('bind()')
    window.iconbitmap('C:/python-learn/tkinter-coursework-2/icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("C:/python-learn/tkinter-coursework-2/texts/bindLesson/1.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()

    Label(win, text='метод bind()', font=('Trebuchet MS', 22, "bold"),
          anchor=N).pack(pady=20)
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=15, text="""
from tkinter import *
root = Tk()

def change(event):
    b['fg'] = "red"
    b['activeforeground'] = "red"

b = Button(text='RED', width=10, height=3)
b.bind('<Button-1>', change)
b.bind('<Return>', change)

b.pack()

root.mainloop()
                                        """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT,
          font=codeFont).pack()
    f = open("C:/python-learn/tkinter-coursework-2/texts/bindLesson/2.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=16, text="""
from tkinter import *
root = Tk()

class RedButton:
    def __init__(self):
        self.b = Button(text='RED',
                            width=10, height=3)
        self.b.bind('<Button-1>', self.change)
        self.b.pack()
    def change(self, event):
        self.b['fg'] = "red"
        self.b['activeforeground'] = "red"

RedButton()
root.mainloop()
                                            """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT,
          font=codeFont).pack()
    f = open("C:/python-learn/tkinter-coursework-2/texts/bindLesson/3.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=16, text="""
from tkinter import *
root = Tk()

def font1(event):
    l['font'] = "Verdana"
def font2(event):
    l['font'] = "Times"

l = Label(text="Hello World")

l.bind('<Button-1>', font1) # ЛКМ
l.bind('<Button-3>', font2) # ПКМ
l.pack()

root.mainloop()
                                                """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT,
          font=codeFont).pack()
    f = open("C:/python-learn/tkinter-coursework-2/texts/bindLesson/4.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=6, text="""
… 
def changeFont(event, font):
    l['font'] = font
… 
                                                    """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT,
          font=codeFont).pack()
    f = open("C:/python-learn/tkinter-coursework-2/texts/bindLesson/5.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=7, text="""
… 
l.bind('<Button-1>', lambda event,
            f="Verdana": changeFont(event, f))
l.bind('<Button-3>', lambda event,
            f="Times": changeFont(event, f))
… 
                                                        """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT,
          font=codeFont).pack()
    f = open("C:/python-learn/tkinter-coursework-2/texts/bindLesson/6.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=15, text="""
from tkinter import *
root = Tk()

def changeFont(font):
    l['font'] = font

l = Label(text="Hello World")
l.pack()
Button(command=lambda f="Verdana": 
                changeFont(f)).pack()
Button(command=lambda f="Times": 
                changeFont(f)).pack()

root.mainloop()
                                                            """, bg="black", bd=3, relief=GROOVE, fg="green",
          justify=LEFT,
          font=codeFont).pack()
    Label(win, text='Практична робота', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/bindLesson/7.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text

    def example():
        def enter_change(event):
            listbox.insert(0, entry.get())
            entry.delete(0, END)

        def double_change(event):
            select = list(listbox.curselection())  # Створюємо кортеж індексів listbox
            select.reverse()  # Реверсуємо його
            for i in select:
                entry.insert(END, listbox.get(i) + " ")

        app = Tk()

        entry = Entry(app, width=25)
        entry.bind('<Return>', enter_change)
        entry.pack(pady=10)
        listbox = Listbox(app, width=25, height=10, selectmode=EXTENDED)
        listbox.bind('<Double-Button-1>', double_change)
        listbox.pack()
        app.mainloop()

    Button(win, width=300, height=30, text="Запустити зразок", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example

    def nextLesson():
        window.destroy()
        eventLesson()

    def preLesson():
        window.destroy()
        listboxLesson()

    frame = Frame(win)
    Button(frame, text=" < Попередня тема < ", command=preLesson).pack(side=LEFT, anchor=SW, pady=10, padx=10)
    Button(frame, text=" > Наступна тема > ", command=nextLesson).pack(side=LEFT, anchor=SE, pady=10, padx=10)
    frame.pack(pady=20)
    del frame
    win.pack(fill=BOTH, expand=True)


def eventLesson():
    global w, h, codeFont
    window = Toplevel(root)
    window.geometry("600x700+{}+{}".format(w, h))
    window.resizable(False, False)
    window.title('Події tkinter')
    window.iconbitmap('C:/python-learn/tkinter-coursework-2/icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("C:/python-learn/tkinter-coursework-2/texts/eventLesson/1.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()

    Label(win, text='Події', font=('Trebuchet MS', 22, "bold"),
          anchor=N).pack(pady=20)
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    frame = Frame(win)
    Label(frame, text='Типи подій', font=('Trebuchet MS', 18, "bold"),
          anchor=N).pack(pady=20)
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/event/2.gif")
    labelImage = Label(frame, image=image)
    labelImage.image = image
    labelImage.pack()
    del image, labelImage
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/event/3.gif")
    labelImage = Label(frame, image=image)
    labelImage.image = image
    labelImage.pack()
    del image, labelImage
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/event/4.gif")
    labelImage = Label(frame, image=image)
    labelImage.image = image
    labelImage.pack()
    del image, labelImage
    frame.pack()
    Label(win, text='При виклику методу bind () подія передається через перший аргумент.',
          font=('Trebuchet MS', 12), justify=LEFT).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/event/1.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/eventLesson/2.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=27, text="""
from tkinter import *


def rightClick(event):
    root.title('ПКМ')


def leftClick(event):
    root.title('ЛКМ')


def mouseMove(event):
    x = event.x
    y = event.y
    s = "Mouse moving on {}:{}".format(x, y)
    root.title(s)


root = Tk()
root.geometry("320x150")

root.bind('<Button-1>', leftClick)
root.bind('<Button-3>', rightClick)
root.bind('<Motion>', mouseMove)

root.mainloop()
     """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()

    def example():
        def rightClick(event):
            app.title('ПКМ')

        def leftClick(event):
            app.title('ЛКМ')

        def mouseMove(event):
            x = event.x
            y = event.y
            s = "Mouse moving on {}:{}".format(x, y)
            app.title(s)

        app = Tk()
        app.geometry("320x150")

        app.bind('<Button-1>', leftClick)
        app.bind('<Button-3>', rightClick)
        app.bind('<Motion>', mouseMove)

        app.mainloop()

    Button(win, width=300, height=30, text="Запустити приклад", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example
    f = open("C:/python-learn/tkinter-coursework-2/texts/eventLesson/3.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=53, text="""
from tkinter import *


def selectAll(event):
    # без цього виділення не відбудеться
    root.after(10, select_all, event.widget)
    # метод .after() виконує функцію, яка вказана 
    # в другому аргументі, через проміжок часу 
    # вказаному в першому аргументі. В третьому 
    # значенні передаєтсья значеня атрибута 
    # widget об'єкта event, тобто поле entry. 
    # Саме воно буде передано в функцію 
    # select_all() як параметр widget

# Виділення тексту
def select_all(widget):
    # Діапазон виділення
    widget.selection_range(0, END)
    # курсор в кінець
    widget.icursor(END)


# Вставка тексту з поля в мітку
def copyPaste(event):
    t = entry.get()
    # Конфігуруємо мітку label
    label.configure(text=t)


def exitWindow(event):
    # "Знищуємо" вікно
    root.destroy()


root = Tk()

entry = Entry(width=25, font="Comic")
# Ctrl + A - вибираємо весь текст в полі
entry.bind('<Control-a>', selectAll)
# Enter - вставляємо виділений текст в мітку
entry.bind('<Return>', copyPaste)
entry.pack(pady=10)


label = Label(height=4, font=("Verdana", 20, 
            'bold'), bg="lightgreen", fg="grey")
label.pack(fill=X)

# Вихід з програми
root.bind('<Control-q>', exitWindow)

root.mainloop()
         """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()

    def example():
        def selectAll(event):
            app.after(10, select_all, event.widget)  # без цього виділення не відбудеться
            # метод .after() виконує функцію, яка вказана в другому аргументі, через проміжок часу
            # вказаному в першому аргументі. В третьому значенні передаєтсья значеня атрибута
            # widget об'єкта event, тобто поле entry. Саме воно буде передано в функцію select_all()
            # як параметр widget

        def select_all(widget):  # Виділення тексту
            widget.selection_range(0, END)  # Діапазон виділення
            widget.icursor(END)  # курсор в кінець

        def copyPaste(event):  # Вставка тексту з поля в мітку
            t = entry.get()
            label.configure(text=t)  # Конфігуруємо мітку label

        def exitWindow(event):
            app.destroy()  # "Знищуємо" вікно

        app = Tk()

        entry = Entry(app, width=25, font="Comic")
        entry.bind('<Control-a>', selectAll)  # Ctrl + A - вибираємо весь текст в полі
        entry.bind('<Return>', copyPaste)  # Enter - вставляємо виділений текст в мітку
        entry.pack(pady=10)

        label = Label(app, height=4, font=("Verdana", 20, 'bold'), bg="lightgreen", fg="grey")
        label.pack(fill=X)

        app.bind('<Control-q>', exitWindow)  # Вихід з програми

        app.mainloop()

    Button(win, width=300, height=30, text="Запустити приклад", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example
    f = open("C:/python-learn/tkinter-coursework-2/texts/eventLesson/4.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, text='Практична робота', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/eventLesson/5.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text

    def example():
        app = Tk()

        en1 = Entry(app, width=5)
        en2 = Entry(app, width=5)
        en1.pack(side=TOP)
        en2.pack(side=TOP)

        button = Button(app, text="Змінити")
        button.bind('<Button-1>', lambda event: text.configure(width=en1.get(), height=en2.get()))
        button.pack(pady=10)

        text = Text(app, width=15, height=8, bg="lightgrey")
        text.bind('<FocusIn>', lambda x: text.configure(bg='white'))  # Подія, яка відбудеться коли text у фокусі
        text.bind('<FocusOut>', lambda x: text.configure(bg="lightgrey"))  # Подія, коли text не у фокусі
        text.pack()

        app.bind('<Return>', lambda event: text.configure(width=en1.get(), height=en2.get()))
        app.bind('<Escape>', lambda x: app.destroy())

        app.mainloop()

    Button(win, width=300, height=30, text="Запустити зразок", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example

    def nextLesson():
        window.destroy()
        canvasLesson()

    def preLesson():
        window.destroy()
        bindLesson()

    frame = Frame(win)
    Button(frame, text=" < Попередня тема < ", command=preLesson).pack(side=LEFT, anchor=SW, pady=10, padx=10)
    Button(frame, text=" > Наступна тема > ", command=nextLesson).pack(side=LEFT, anchor=SE, pady=10, padx=10)
    frame.pack(pady=20)
    del frame
    win.pack(fill=BOTH, expand=True)


def canvasLesson():
    global w, h, codeFont
    window = Toplevel(root)
    window.geometry("600x700+{}+{}".format(w, h))
    window.resizable(False, False)
    window.title('Canvas')
    window.iconbitmap('C:/python-learn/tkinter-coursework-2/icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("C:/python-learn/tkinter-coursework-2/texts/canvasLesson/1.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()

    Label(win, text='Canvas', font=('Trebuchet MS', 22, "bold"),
          anchor=N).pack(pady=20)
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/canvas/1.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack()
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/canvasLesson/2.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=33, text="""
from tkinter import *

root = Tk()

canvas = Canvas(root, width=800, 
            height=600, bg='lightgreen')
canvas.pack()

# create_line() - створює лінію у канвасі
canvas.create_line(100, 50, 700, 50)

# приймає першими двома аргументами х1 та у1, 
# координата початок лінії наступні 2 аргументи
# це х2 та у2, координата в якій лінія закінчиться

canvas.create_line(397, 150, 397, 500, width=6, 
                fill="purple", dash=(2, 1), 
                arrow=FIRST, arrowshape='20 80 200', 
                activefill="silver")

# Аргумент fill у методі create_line() виступає 
# "заливкою" лінії кольором. Аргумент 
# dash(перший арг., другий арг.), робить лінію 
# преривчастою. Першим аргументом в dash() задається 
# довжина відрізка, другим довжина пробілу
# Аргумент arrow малює стрілку, приймає значення 
# FIRST (Початок лінії) та LAST (Кінець лінії)
# Аргумент arrowshape визначає розміри стрілки.
# Аргумент activefill - задає колір лінії при 
# наведенні курсора миші

root.mainloop()
             """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    image = Image.open("C:/python-learn/tkinter-coursework-2/images/canvas/3.gif")
    new_image = image.resize((540, 450))
    image = ImageTk.PhotoImage(new_image)
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage, new_image
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/canvas/2.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack()
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/canvasLesson/3.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=22, text="""
...
# Створимо чотирикутник за допомогою метода 
# create_rectangle() перші 2 аргументи х1, у1, 
# це точка початок рисування. (Верхній лівий 
# куток прямокутника). наступні 2 аргументи:
# х2, у2, це точка кінець рисування (Нижній 
# правий куток прямокутника)

canvas.create_rectangle(100, 50, 500, 150)

# Створимо такий самий за розмірами чотирикутник,
# тільки надамо йому додаткові аргументи
canvas.create_rectangle(100, 200, 500, 300, 
                fill="lightgreen", outline='green',
                width=4, activedash=(4, 2))
# outline - колір лінії-межі чотирикутника
# width - товщина лінії-межі чотирикутника
# activedash - те ж саме, що й dash(), але 
# використовується для межі, при наведенні курсору
# на чотирикутник
...
                 """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    frame = Frame(win)
    image = Image.open("C:/python-learn/tkinter-coursework-2/images/canvas/4.gif")
    new_image = image.resize((540, 450))
    image = ImageTk.PhotoImage(new_image)
    labelImage = Label(frame, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage, new_image
    Label(frame, text='Курсор на прямокутнику:', font=('Trebuchet MS', 16), justify=LEFT).pack()
    image = Image.open("C:/python-learn/tkinter-coursework-2/images/canvas/5.gif")
    new_image = image.resize((540, 450))
    image = ImageTk.PhotoImage(new_image)
    labelImage = Label(frame, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage, new_image
    frame.pack()
    Label(win, text="\nМетодом create_polygon () малюється довільний багатокутник \n"
                    + "шляхом завдання координат кожної його точки:\n",
          font=('Trebuchet MS', 12), justify=LEFT).pack()
    Label(win, height=22, text="""
...
# Створимо шестикутник
canvas.create_polygon((250, 100), (350, 100),
                      (400, 150), (350, 200),
                      (250, 200), (200, 150))
# Координати точок повинні бути задані за 
# часовою стрілкою!!!
# Для зручності кожну точку візьмемо в ()

# Створимо восьмикутник
canvas.create_polygon((250, 250), (350, 250),
                      (400, 300), (400, 350),
                      (350, 400), (250, 400),
                      (200, 350), (200, 300),
    fill="lightblue", outline="silver", width=5)

# Створимо трапецію
canvas.create_polygon((250, 450), (350, 450),
                      (400, 550), (200, 550),
        fill="orange", outline="yellow", width=5)
...
                     """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    Label(win, text='Результат виконання:', font=('Trebuchet MS', 16), justify=LEFT).pack(pady=10)
    image = Image.open("C:/python-learn/tkinter-coursework-2/images/canvas/6.gif")
    new_image = image.resize((540, 650))
    image = ImageTk.PhotoImage(new_image)
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage, new_image
    f = open("C:/python-learn/tkinter-coursework-2/texts/canvasLesson/4.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=26, text="""
...
canvas.create_oval(50, 50, 350, 350)

# Створимо сектор методом create_arc(), 
# він приймає аргументи координати прямокутника
# в якому розташовується еліпс, до якого цей 
# метод застосовується
# аргумент start означає градус початок сектору, 
# extent - градус, скільки сектор буде займати

canvas.create_arc(50, 50, 350, 350, start=90, 
                    extent=45, fill="lightblue")
canvas.create_arc(50, 50, 350, 350, start=10, 
                    extent=45, fill="lightgreen")
# Створимо дугу тим самим методом, але дамо 
# більше аргументів
# аргумент style може приймати значення: 
# ARC - дуга, CHORD - сегмент
canvas.create_arc(50, 50, 350, 350, start=55, 
                    extent=35, style=ARC, 
                    outline="orange", width=3)
canvas.create_arc(50, 50, 350, 350, start=200, 
                    extent=90, style=CHORD, 
                    fill="#E74C3C")
...
                         """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/canvas/7.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/canvas/9.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    Label(win, text="\nНа полотні можна розмістити текст. Робиться це за допомогою \nметоду create_text ():\n",
          font=('Trebuchet MS', 12), justify=LEFT).pack()
    Label(win, height=10, text="""
...
canvas.create_text(200, 200, text="Вставка тексту\n" +
        "на холст", font=("Comic Sans MS", 18, "bold"), 
        justify=LEFT)

canvas.create_text(300, 380, text="Правий куток знизу",
                font=("Verdana", 10, "italic"), 
                justify=RIGHT, fill="aqua")
...
                             """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/canvas/8.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/canvasLesson/5.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, text='Практична робота', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    Label(win, text="Створіть на холсті подібне зразку зображення:", font=('Trebuchet MS', 12), justify=LEFT).pack()

    def example():
        app = Tk()
        app.title("для трави виористовуй цикл")

        canvas = Canvas(app, width=360, height=300)
        canvas.create_oval(220, 10, 270, 60, fill="yellow", outline="orange", width=2)
        canvas.create_polygon((20, 110), (120, 60), (220, 110), (200, 110), (200, 260), (40, 260), (40, 110),
                              fill="lightblue", outline='blue')

        i = -20

        while i <= 380:
            canvas.create_arc(i, 230, (i + 100), 380, start=200, extent=-90, style=ARC, outline="green", width=3)
            i += 10

        canvas.pack()

        app.mainloop()

    Button(win, width=300, height=30, text="Запустити зразок", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example

    def nextLesson():
        window.destroy()
        idtagLesson()

    def preLesson():
        window.destroy()
        eventLesson()

    frame = Frame(win)
    Button(frame, text=" < Попередня тема < ", command=preLesson).pack(side=LEFT, anchor=SW, pady=10, padx=10)
    Button(frame, text=" > Наступна тема > ", command=nextLesson).pack(side=LEFT, anchor=SE, pady=10, padx=10)
    frame.pack(pady=20)
    del frame
    win.pack(fill=BOTH, expand=True)


def idtagLesson():
    global w, h, codeFont
    window = Toplevel(root)
    window.geometry("600x700+{}+{}".format(w, h))
    window.resizable(False, False)
    window.title('Canvas. Анімація. Ідентифікатори і теги')
    window.iconbitmap('C:/python-learn/tkinter-coursework-2/icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("C:/python-learn/tkinter-coursework-2/texts/idtagLesson/1.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()

    Label(win, text='Canvas. Ідентифікатори і теги. Анімація.', font=('Trebuchet MS', 22, "bold"),
          anchor=N).pack(pady=20)
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, text='Ідентифікатори', font=('Trebuchet MS', 18, "bold"),
          anchor=N).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/idtagLesson/2.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=20, text="""
from tkinter import *

root = Tk()

c = Canvas(root, width=500, height=500)
c.focus_set()
c.pack()

ball = c.create_oval(200, 200, 300, 300, 
    fill="#F43F23", outline="#AD2009", width=3)

# Main moves
c.bind('<Up>', lambda event: c.move(ball, 0, -5))
c.bind('<Down>', lambda event: c.move(ball, 0, 5))
c.bind('<Left>', lambda event: c.move(ball, -5, 0))
c.bind('<Right>', lambda event: c.move(ball, 5, 0))


root.mainloop()
                                 """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()

    def example():
        app = Tk()
        c = Canvas(app, width=500, height=500)
        c.focus_set()
        c.pack()

        ball = c.create_oval(200, 200, 300, 300,
                             fill="#F43F23", outline="#AD2009", width=3)

        # Main moves
        c.bind('<Up>', lambda event: c.move(ball, 0, -5))
        c.bind('<Down>', lambda event: c.move(ball, 0, 5))
        c.bind('<Left>', lambda event: c.move(ball, -5, 0))
        c.bind('<Right>', lambda event: c.move(ball, 5, 0))

        app.mainloop()

    Button(win, width=300, height=30, text="Запустити зразок", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example
    f = open("C:/python-learn/tkinter-coursework-2/texts/idtagLesson/3.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=30, text="""
from tkinter import *


def inFocus(event):
    c.itemconfig(rect, fill="#95E874")
    c.coords(rect, 8, 8, 392, 392)


def outFocus(event):
    c.itemconfig(rect, fill="#69A452")
    c.coords(rect, 10, 10, 390, 390)


root = Tk()

c = Canvas(root, width=400, height=400, 
                            bg="white")

rect = c.create_rectangle(10, 10, 390, 390, 
                            fill="#69A452")
c.bind('<FocusIn>', inFocus)
c.bind('<FocusOut>', outFocus)

c.pack()

b = Button(root, text="Some Button")
b.pack()

root.mainloop()
    """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()

    def example():

        def inFocus(event):
            c.itemconfig(rect, fill="#95E874")
            c.coords(rect, 8, 8, 392, 392)

        def outFocus(event):
            c.itemconfig(rect, fill="#69A452")
            c.coords(rect, 10, 10, 390, 390)

        app = Tk()

        c = Canvas(app, width=400, height=400,
                   bg="white")

        rect = c.create_rectangle(10, 10, 390, 390,
                                  fill="#69A452")
        c.bind('<FocusIn>', inFocus)
        c.bind('<FocusOut>', outFocus)

        c.pack()

        b = Button(app, text="Some Button")
        b.pack()

        app.mainloop()

    Button(win, width=300, height=30, text="Запустити зразок", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example
    Label(win, text="Тут при отриманні полотном фокуса (натиснути Tab) зміниться колір \nі розмір квадрата.",
          font=('Trebuchet MS', 12), justify=LEFT).pack()
    Label(win, text='Теги', font=('Trebuchet MS', 18, "bold"),
          anchor=N).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/idtagLesson/4.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=16, text="""
...
c = Canvas(root, width=400, height=400)

c.create_line(10, 40, 390, 40, width=4, 
    fill="red", dash=(1, 1), tag="group1")
c.create_oval(10, 90, 390, 360, 
    fill="lightgreen", tag="group1")

c.bind("<Button-1>", lambda event: 
    c.itemconfig('group1', fill='lightblue'))
c.bind("<Button-3>", lambda event: 
    c.itemconfig('group1', fill='lightgreen'))

c.pack()
...
        """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    f = open("C:/python-learn/tkinter-coursework-2/texts/idtagLesson/5.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=42, text="""
from tkinter import *

root = Tk()

canvas = Canvas(root, width=470, height=160)
oval = canvas.create_oval(30, 30, 130, 130, 
                        fill="lightgreen")
canvas.create_polygon((180, 130), (230, 30), 
                (280, 130), fill="lightblue", 
            outline="black", tag='triangle')
canvas.create_rectangle(320, 30, 420, 130, 
                fill="pink", tag='rectangle')


def onOval(event):
    canvas.delete(oval)
    canvas.create_text(80, 80, text='Круг', 
        font=('Comic Sans MS', 20, "bold"))


def onTriangle(event):
    canvas.delete('triangle')
    canvas.create_text(225, 80, text='Трикутник', 
            font=('Comic Sans MS', 20, "bold"))


def onRectangle(event):
    canvas.delete('rectangle')
    canvas.create_text(380, 80, text='Квадрат',
            font=('Comic Sans MS', 20, "bold"))


canvas.tag_bind(oval, '<Button-1>', onOval)
canvas.tag_bind('triangle', '<Button-1>', 
                                onTriangle)
canvas.tag_bind('rectangle', '<Button-1>',
                                onRectangle)

canvas.pack()

root.mainloop()
            """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()

    def example():
        app = Tk()

        canvas = Canvas(app, width=470, height=160)
        oval = canvas.create_oval(30, 30, 130, 130, fill="lightgreen")
        canvas.create_polygon((180, 130), (230, 30), (280, 130), fill="lightblue", outline="black", tag='triangle')
        canvas.create_rectangle(320, 30, 420, 130, fill="pink", tag='rectangle')

        def onOval(event):
            canvas.delete(oval)
            canvas.create_text(80, 80, text='Круг', font=('Comic Sans MS', 20, "bold"))

        def onTriangle(event):
            canvas.delete('triangle')
            canvas.create_text(225, 80, text='Трикутник', font=('Comic Sans MS', 20, "bold"))

        def onRectangle(event):
            canvas.delete('rectangle')
            canvas.create_text(380, 80, text='Квадрат', font=('Comic Sans MS', 20, "bold"))

        canvas.tag_bind(oval, '<Button-1>', onOval)
        canvas.tag_bind('triangle', '<Button-1>', onTriangle)
        canvas.tag_bind('rectangle', '<Button-1>', onRectangle)

        canvas.pack()

        app.mainloop()

    Button(win, width=300, height=30, text="Запустити цей код", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example
    f = open("C:/python-learn/tkinter-coursework-2/texts/idtagLesson/6.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    Label(win, text='Практична робота', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    Label(win, height=17, text="""
from tkinter import *

root = Tk()
c = Canvas(root, width=300, height=200, bg="white")
c.pack()

ball = c.create_oval(0, 100, 40, 140, fill='green')

def motion():
    c.move(ball, 1, 0)
    if c.coords(ball)[2] < 300:
        root.after(10, motion)

motion()

root.mainloop()
                """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    f = open("C:/python-learn/tkinter-coursework-2/texts/idtagLesson/7.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text

    def example():
        app = Tk()
        c = Canvas(app, width=300, height=200, bg="white")
        c.pack()

        ball = c.create_oval(100, 100, 120, 120, fill='green')

        def mouseClick(event):
            x = event.x
            y = event.y
            motion(x, y)

        def motion(x, y):
            if (c.coords(ball)[2] + c.coords(ball)[0]) / 2 < x:
                c.move(ball, 1, 0)
                root.after(10, motion, x, y)
            if (c.coords(ball)[3] + c.coords(ball)[1]) / 2 < y:
                c.move(ball, 0, 1)
                root.after(10, motion, x, y)
            if (c.coords(ball)[2] + c.coords(ball)[0]) / 2 > x:
                c.move(ball, -1, 0)
                root.after(10, motion, x, y)
            if (c.coords(ball)[3] + c.coords(ball)[1]) / 2 > y:
                c.move(ball, 0, -1)
                root.after(10, motion, x, y)

        c.bind('<Button-1>', mouseClick)

        app.mainloop()

    Button(win, width=300, height=30, text="Запустити зразок", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example

    def nextLesson():
        window.destroy()
        windowLesson()

    def preLesson():
        window.destroy()
        canvasLesson()

    frame = Frame(win)
    Button(frame, text=" < Попередня тема < ", command=preLesson).pack(side=LEFT, anchor=SW, pady=10, padx=10)
    Button(frame, text=" > Наступна тема > ", command=nextLesson).pack(side=LEFT, anchor=SE, pady=10, padx=10)
    frame.pack(pady=20)
    del frame
    win.pack(fill=BOTH, expand=True)


def windowLesson():
    global w, h, codeFont
    window = Toplevel(root)
    window.geometry("600x700+{}+{}".format(w, h))
    window.resizable(False, False)
    window.title('Вікна')
    window.iconbitmap('C:/python-learn/tkinter-coursework-2/icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("C:/python-learn/tkinter-coursework-2/texts/windowLesson/1.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()

    Label(win, text='Вікна', font=('Trebuchet MS', 22, "bold"),
          anchor=N).pack(pady=20)
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, text='Розміри та розташування вікна', font=('Trebuchet MS', 18, "bold"),
          anchor=N).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/windowLesson/2.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=8, text="""
from tkinter import *

root = Tk()

root.geometry('600x400+200+100')

root.mainloop()
                    """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    f = open("C:/python-learn/tkinter-coursework-2/texts/windowLesson/3.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=61, text="""
from tkinter import *

root = Tk()

# Присвоюємо змінній w ширину екрану 
# (в моєму випадку 1600)
w = root.winfo_screenwidth()

# Присвоюємо змінній h висоту екрану
# (в моєму випадку 900)
h = root.winfo_screenheight()

# Виконуємо цілочисельне ділення ширини екрану, 
# тобто, шукаємо половину ширини = 800
w = w//2

# Виконуємо цілочисельне ділення висоти екрану, 
# тобто, шукаємо половину висоти = 450
h = h//2

# Віднімаємо половину ширини вікна для того,
# щоб воно розмістилось рівно в центрі
w = w - 200

# w = 800 - 200, w = 600

# Віднімаємо половину висоти вікна для того,
# щоб воно розмістилось рівно в центрі
h = h - 200

# h = 450 - 200, h = 250

# Перші два значення в методі geometry(), які розділені 
# літералом х приймають значення ширини та висоти вікна
# "+" - означає додати відступ по ширині від верхнього 
# лівого краю екрану(перше значення після плюса - зліва
# друге - зверху)
# Якщо "+" змінити на "-" відступ буде виконуватись з 
# правого нижнього кутка екрану
# Перше значення після "-" буде відступати справа, 
# друге знизу
# Відступаємо від верху 600 пікселів по ширині та 250 
# по висоті методом .format()
# Та використовуємо змінні, які проводили обчислення,
# щоб не обчислювати вручну
root.geometry('400x400+{}+{}'.format(w, h))

Label(root, text="Ширина екрану: "
            +str(root.winfo_screenwidth())).pack()
Label(root, text="Висота екрану: "
            +str(root.winfo_screenheight())).pack()
Label(root, text="Половина ширини: "
            +str(root.winfo_screenwidth()//2)).pack()
Label(root, text="Половина висоти: "
            +str(root.winfo_screenheight()//2)).pack()
Label(root, text="Початок рисування вікна "
            +"по осі Х: "+str(w)+"px").pack()
Label(root, text="Початок рисування вікна "
            +"по осі Y: "+str(h)+"px").pack()
root.mainloop()
                        """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()

    def example():
        app = Tk()

        wid = app.winfo_screenwidth()  # Присвоюємо змінній w ширину екрану (в моєму випадку 1600)
        hei = app.winfo_screenheight()  # Присвоюємо змінній h висоту екрану (в моєму випадку 900)
        wid = wid // 2  # Виконуємо цілочисельне ділення ширини екрану, тобто, шукаємо половину ширини = 800
        hei = hei // 2  # Виконуємо цілочисельне ділення висоти екрану, тобто, шукаємо половину висоти = 450
        # Віднімаємо половину ширини вікна для того, щоб воно розмістилось рівно в центрі
        wid = wid - 200  # w = 800 - 200, w = 600
        # Віднімаємо половину висоти вікна для того, щоб воно розмістилось рівно в центрі
        hei = hei - 200  # h = 450 - 200, h = 250

        # Перші два значення в методі geometry(), які розділені літералом х приймають значення ширини та висоти вікна
        # "+" - означає додати відступ по ширині від верхнього лівого краю екрану(перше значення після плюса - зліва
        # друге - зверху)
        # Якщо "+" змінити на "-" відступ буде виконуватись з правого нижнього кутка екрану
        # Перше значення після "-" буде відступати справа, друге знизу
        # Відступаємо від верху 600 пікселів по ширині та 250 по висоті методом .format()
        # Та використовуємо змінні, які проводили обчислення, щоб не обчислювати вручну
        app.geometry('400x400+{}+{}'.format(wid, hei))
        Label(app, text="Ширина екрану: " + str(app.winfo_screenwidth())).pack()
        Label(app, text="Висота екрану: " + str(app.winfo_screenheight())).pack()
        Label(app, text="Половина ширини: " + str(app.winfo_screenwidth() // 2)).pack()
        Label(app, text="Половина висоти: " + str(app.winfo_screenheight() // 2)).pack()
        Label(app, text="Початок рисування вікна по осі Х: " + str(wid) + "px").pack()
        Label(app, text="Початок рисування вікна по осі Y: " + str(hei) + "px").pack()
        app.mainloop()

    Button(win, width=300, height=30, text="Запустити приклад", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example
    f = open("C:/python-learn/tkinter-coursework-2/texts/windowLesson/4.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=89, text="""
from tkinter import *

root = Tk()

Button(root, width=20, 
        text="Just button").pack()
Label(root, width=20, height=3, 
        text='Just label').pack()
Button(root, width=20, 
        text="Just button").pack()

# З самого початку програми в geometry() 
# ширина та висота мають значення 1. Така 
# особливість tkinter
# Щоб оновити значення після розміщення 
# елементів використовуємо метод 
# update_idletasks()

root.update_idletasks()

# Присвоюємо змінній s значення висоти 
# та ширини вікна

s = root.geometry()

# Щоб взяти лише висоту та ширину, без 
# відступів збоку та зверху(знизу) використовуємо 
# стандартний метод split() де агрументом виступає 
# літерал, який розділяє ці данні, в данному 
# випадку "+"

s = s.split("+")

# Створюємо список та присвоюємо до нульововго 
# індексу ширину вікна використовуючи split.
# До індексу [1] буде присвоєне наступне значення 
# з geometry. Запис в список припиниться,
# тоді, коли ми достигнемо розділювача "+", про 
# який ми записали вище, так як geometry() складається
# з geometry
# ("ШИРИНАхВИСОТА+ВІДСТУП СПРАВА+ВІДСТУП ЗВЕРХУ"), 
# список буде складатись з двох елементів.
# У s[0] буде записане число-ширина вікна, у s[1] 
# число-висота вікна

s = s[0].split('x')

# Присвоємо змінній window_width ширину вікна з 
# списку s[]

window_width = int(s[0])

# А window_height - висоту вікна
window_height = int(s[1])

# Отримуємо ширину екрану
w = root.winfo_screenwidth()

# Отримуємо висоту екрану
h = root.winfo_screenheight()

# Ділимо націло ширину екрану на 2, щоб 
# розташувати вікно рівно по центру
w = w//2

# Таку ж операцію проводимо з висотою
h = h//2 

# Тепер, нам потрібно вирахувати точку відступу збоку,
# щоб вікно було рівно по центру відносно ширини.
# Для цього від половини ширини екрану віднімаємо 
# половину ширини вікна, інакше вікно
# буде розміщене дальше на відстань рівну половині своєї
# ширини. По суті, воно розмістить свій лівий
# верхній край там, де мав би бути центр

w = w - window_width//2

# Також вираховуємо точку відступу зверху,
h = h - window_height//2

# Далі впроваджуємо ці відступи до методу geometry(), 
# розміри вікна не вказуємо, так як вони вказані
# програмно вище.

root.geometry('+{}+{}'.format(w, h))

root.mainloop()
                            """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()

    def example():
        app = Tk()

        Button(app, width=20, text="Just button").pack()
        Label(app, width=20, height=3, text='Just label').pack()
        Button(app, width=20, text="Just button").pack()

        app.update_idletasks()
        s = app.geometry()
        s = s.split("+")
        s = s[0].split('x')
        window_width = int(s[0])
        window_height = int(s[1])

        wid = app.winfo_screenwidth()
        hei = app.winfo_screenheight()
        wid = wid // 2
        hei = hei // 2
        wid = wid - window_width // 2
        hei = hei - window_height // 2

        app.geometry('+{}+{}'.format(wid, hei))

        app.mainloop()

    Button(win, width=300, height=30, text="Запустити приклад", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example
    f = open("C:/python-learn/tkinter-coursework-2/texts/windowLesson/5.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=5, text="""
...
root.resizable(False, False)
...
                                """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/window/1.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    Label(win, text='Заголовок вікна', font=('Trebuchet MS', 18, "bold"),
          anchor=N).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/windowLesson/6.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=5, text="""
    ...
    root.title("Головне вікно")
    ...
                                    """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT,
          font=codeFont).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/window/2.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/windowLesson/7.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=51, text="""
from tkinter import *

root = Tk()
root.resizable(False, False)
# Розміщуємо головне вікно по центру
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w - 125
h = h - 100
root.geometry("250x200+{}+{}".format(w, h))


# Вікно, яке викликається кнопкою but
def more():
    # Створюємо другорядне вікно
    a = Toplevel()

    # Розміщуємо його на одному рівні з головним 
    # вікном, але правіше, на 20px
    ww = root.winfo_screenwidth()
    wh = root.winfo_screenheight()
    ww = ww//2
    wh = wh//2
    s = root.geometry()
    s = s.split('+')
    s = s[0].split('x')
    width_a = int(s[0])
    height_a = int(s[1])
    ww = ww + width_a//2 + 20
    wh = wh - height_a//2
    a.geometry('250x200+{}+{}'.format(ww, wh))

    # Відключаємо кнопки, та титулку на "Брові" вікна
    a.overrideredirect(True)
    Label(a, text="Функція, яка створює додаткове вікно\ n,"
    +" що синтезується поверх \ n головного вікна ""програми",
          justify=CENTER).pack(expand=1)

    # Знищуємо дане вікно через 6 секунд
    a.after(6000, lambda: a.destroy()) 


lab1 = Label(width=20, height=5, 
    text="функція TopLevel()").pack()
but = Button(text="Детальніше", 
    command=more).pack(pady=5)


root.mainloop()
        """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()

    def example():
        app = Tk()
        app.resizable(False, False)
        wid = app.winfo_screenwidth()
        hei = app.winfo_screenheight()
        wid = wid // 2
        hei = hei // 2
        wid = wid - 125
        hei = hei - 100
        app.geometry("250x200+{}+{}".format(wid, hei))

        def more():
            a = Toplevel()

            ww = app.winfo_screenwidth()
            wh = app.winfo_screenheight()
            ww = ww // 2
            wh = wh // 2
            s = app.geometry()
            s = s.split('+')
            s = s[0].split('x')
            width_a = int(s[0])
            height_a = int(s[1])
            ww = ww + width_a // 2 + 20
            wh = wh - height_a // 2
            a.geometry('250x200+{}+{}'.format(ww, wh))

            a.overrideredirect(True)
            Label(a, text="Функція, яка створює додаткове вікно\n, що синтезується поверх \nголовного вікна ""програми",
                  justify=CENTER).pack(expand=1)
            a.after(6000, lambda: a.destroy())  # Знищуємо дане вікно через 6 секунд

        Label(app, width=20, height=5, text="функція TopLevel()").pack()
        Button(app, text="Детальніше", command=more).pack(pady=5)

        app.mainloop()

    Button(win, width=300, height=30, text="Запустити приклад", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example
    Label(win, text='Практична робота', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/windowLesson/8.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text

    def example():
        app = Tk()

        app.title("Прямокутник і Овал")

        wid = app.winfo_screenwidth()
        hei = app.winfo_screenheight()
        wid = wid // 2
        hei = hei // 2
        mw = wid - 200
        mh = hei - 225

        app.geometry('400x450+{}+{}'.format(mw, mh))

        def addItem():
            controlPanel = Toplevel(app)
            controlPanel.title('Фігура')
            cpw = mw + 410
            cph = mh
            controlPanel.geometry("180x180+{}+{}".format(cpw, cph))
            frame1 = Frame(controlPanel)
            frame2 = Frame(controlPanel)
            labx1 = Label(frame1, text="x1")
            entx1 = Entry(frame1, width=3)
            laby1 = Label(frame1, text="y1")
            enty1 = Entry(frame1, width=3)
            labx2 = Label(frame2, text="x2")
            entx2 = Entry(frame2, width=3)
            laby2 = Label(frame2, text="y1")
            enty2 = Entry(frame2, width=3)
            r_var = IntVar(controlPanel)
            r_var.set(0)

            r1 = Radiobutton(controlPanel, text="Прямокутник", variable=r_var, value=0)
            r2 = Radiobutton(controlPanel, text="Овал", variable=r_var, value=1)

            frame1.pack(padx=20, pady=10)
            frame2.pack(padx=20, pady=10)
            labx1.pack(side=LEFT)
            entx1.pack(side=LEFT)
            laby1.pack(side=LEFT)
            enty1.pack(side=LEFT)
            labx2.pack(side=LEFT)
            entx2.pack(side=LEFT)
            laby2.pack(side=LEFT)
            enty2.pack(side=LEFT)
            r1.pack()
            r2.pack()

            def draw():
                x1 = entx1.get()
                x2 = entx2.get()
                y1 = enty1.get()
                y2 = enty2.get()
                if r_var.get() == 0:
                    canvas.create_rectangle(x1, y1, x2, y2)
                elif r_var.get() == 1:
                    canvas.create_oval(x1, y1, x2, y2)
                controlPanel.destroy()

            button = Button(controlPanel, text="Нарисувати фігуру", command=draw)
            button.pack()

        canvas = Canvas(app, width=400, height=400)
        canvas.pack()
        Button(app, text="Додати фігуру", command=addItem).pack()

        app.mainloop()

    Button(win, width=300, height=30, text="Запустити зразок", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example

    def nextLesson():
        window.destroy()
        gridLesson()

    def preLesson():
        window.destroy()
        idtagLesson()

    frame = Frame(win)
    Button(frame, text=" < Попередня тема < ", command=preLesson).pack(side=LEFT, anchor=SW, pady=10, padx=10)
    Button(frame, text=" > Наступна тема > ", command=nextLesson).pack(side=LEFT, anchor=SE, pady=10, padx=10)
    frame.pack(pady=20)
    del frame
    win.pack(fill=BOTH, expand=True)


def gridLesson():
    global w, h, codeFont
    window = Toplevel(root)
    window.geometry("600x700+{}+{}".format(w, h))
    window.resizable(False, False)
    window.title('метод grid()')
    window.iconbitmap('C:/python-learn/tkinter-coursework-2/icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("C:/python-learn/tkinter-coursework-2/texts/gridLesson/1.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()

    Label(win, text='Метод grid()', font=('Trebuchet MS', 22, "bold"),
          anchor=N).pack(pady=20)
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/grid/1.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/gridLesson/2.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/grid/3.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/gridLesson/3.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/grid/5.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    Label(win, text="Тепер напишемо код: ", font=('Trebuchet MS', 12), justify=LEFT).pack(pady=10)
    Label(win, height=30, text="""
from tkinter import *

root = Tk()

# Перший рядок
Label(root, text="Ім'я").grid(row=0, 
                            column=0)
Entry(root, width=38).grid(row=0, column=1,
                            columnspan=3)

# Другий рядок
Label(root, text="Стовпців: ").grid(row=1,
                                column=0)
Spinbox(root, from_=1, to=50, 
            width=10).grid(row=1, column=1)
Label(root, text="Рядків: "
                    ).grid(row=1, column=2)
Spinbox(root, from_=1, to=50, 
            width=10).grid(row=1, column=3)

# Третій рядок
Button(root, text="Довідка").grid(row=2,
                                    column=0)
Button(root, text="Вставити").grid(row=2,
                                    column=2)
Button(root, text="Відміна").grid(row=2,
                                    column=3)

root.mainloop()
        """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    f = open("C:/python-learn/tkinter-coursework-2/texts/gridLesson/4.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/grid/2.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/gridLesson/5.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=32, text="""
from tkinter import *

root = Tk()

# Перший рядок
# Атрибут sticky "прибиває" елемент відносно 
# сторони компаса, до сторони комірки

Label(root, text="Ім'я:").grid(row=0, column=0, 
                padx=10, pady=10, sticky=W)
Entry(root, width=38).grid(row=0, column=1, 
                columnspan=3, padx=10, pady=10)

# Другий рядок
Label(root, text="Стовпців: ").grid(row=1, 
            column=0, padx=10, pady=10, sticky=W)
Spinbox(root, from_=1, to=50, width=10).grid(row=1,
            column=1, padx=10, pady=10)
Label(root, text="Рядків: ").grid(row=1, column=2,
            padx=10, pady=10)
Spinbox(root, from_=1, to=50, width=10).grid(row=1,
            column=3, padx=10, pady=10)

# Третій рядок
Button(root, text="Довідка").grid(row=2, column=0,
            padx=10, pady=10, sticky=W)
Button(root, text="Вставити").grid(row=2, column=2)
Button(root, text="Відміна").grid(row=2, column=3,
            padx=10, pady=10, sticky=E)

root.mainloop()
            """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/grid/3.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/gridLesson/6.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, text='Практична робота', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    Label(win, text="Перепрограмуйте друге вікно з практичної роботи минулої теми, \n"
                    +"з використанням .grid() замість .pack()", font=('Trebuchet MS', 12), justify=LEFT).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/grid/4.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage

    def nextLesson():
        window.destroy()
        messageBoxLesson()

    def preLesson():
        window.destroy()
        windowLesson()

    frame = Frame(win)
    Button(frame, text=" < Попередня тема < ", command=preLesson).pack(side=LEFT, anchor=SW, pady=10, padx=10)
    Button(frame, text=" > Наступна тема > ", command=nextLesson).pack(side=LEFT, anchor=SE, pady=10, padx=10)
    frame.pack(pady=20)
    del frame
    win.pack(fill=BOTH, expand=True)


def messageBoxLesson():
    global w, h, codeFont
    window = Toplevel(root)
    window.geometry("600x700+{}+{}".format(w, h))
    window.resizable(False, False)
    window.title('Вікна діалогу')
    window.iconbitmap('C:/python-learn/tkinter-coursework-2/icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("C:/python-learn/tkinter-coursework-2/texts/messageBoxLesson/1.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()

    Label(win, text='Діалогові вікна', font=('Trebuchet MS', 22, "bold"),
          anchor=N).pack(pady=20)
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, text='Модуль messagebox - стандартні діалогові вікна', font=('Trebuchet MS', 18, "bold")).pack(pady=10)
    Label(win, text="Вікно вибору 'так' або 'ні' - askyesno()", font=('Trebuchet MS', 12), justify=LEFT).pack(pady=10)
    Label(win, height=25, text="""
from tkinter import *
from tkinter import messagebox as mb

root = Tk()


def check():
    answer = mb.askyesno(title="Дайте відповідь", 
                    message="Перенести данні?")
    if answer == True:
        s = entry.get()
        entry.delete(0, END)
        label.configure(text=s)


entry = Entry(root)
entry.pack()
button = Button(root, text="Передати",
                        command=check)
button.pack()
label = Label()
label.pack()

root.mainloop()
                """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/messageBox/1.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/messageBox/2.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/messageBox/3.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/messageBoxLesson/2.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, text='mb.showerror("Помилка", "Введіть число!")', font=('Trebuchet MS', 12), justify=LEFT).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/messageBox/4.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    Label(win, text='mb.showinfo("Помилка", "Введіть число!")', font=('Trebuchet MS', 12), justify=LEFT).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/messageBox/5.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    Label(win, text='mb.showwarning("Помилка", "Введіть число!")', font=('Trebuchet MS', 12), justify=LEFT).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/messageBox/6.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    Label(win, text='Модуль filedialog - діалогові вікна відкриття \nта збереження файлів',
          font=('Trebuchet MS', 18, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/messageBoxLesson/3.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=33, text="""
from tkinter import *
from tkinter import filedialog as fd

root = Tk()


def openFile():
    file_name = fd.askopenfilename()
    f = open(file_name, encoding="utf-8")
    s = f.read()
    text.insert(1.0, s)
    f.close()

def saveFile():
    file_name = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
            ("HTML files", "*.html;*.htm"),
            ("All files", "*.*") ))
    f = open(file_name, 'w', encoding="utf-8")
    s = text.get(1.0, END)
    f.write(s)
    f.close()


text = Text(root, width=45, height=25)
text.grid(columnspan=2)
Button(root, text="Відкрити", command=openFile
                    ).grid(row=1, sticky=E)
Button(root, text="Зберегти", command=saveFile
                ).grid(row=1, column=1, sticky=W)

root.mainloop()
            """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/messageBox/7.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/messageBoxLesson/4.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, text='Практична робота', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/messageBoxLesson/5.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text

    def nextLesson():
        window.destroy()
        menuLesson()

    def preLesson():
        window.destroy()
        gridLesson()

    frame = Frame(win)
    Button(frame, text=" < Попередня тема < ", command=preLesson).pack(side=LEFT, anchor=SW, pady=10, padx=10)
    Button(frame, text=" > Наступна тема > ", command=nextLesson).pack(side=LEFT, anchor=SE, pady=10, padx=10)
    frame.pack(pady=20)
    del frame
    win.pack(fill=BOTH, expand=True)


def menuLesson():
    global w, h, codeFont
    window = Toplevel(root)
    window.geometry("600x700+{}+{}".format(w, h))
    window.resizable(False, False)
    window.title('Menu()')
    window.iconbitmap('C:/python-learn/tkinter-coursework-2/icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("C:/python-learn/tkinter-coursework-2/texts/menuLesson/1.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()

    Label(win, text='Віджет Menu()', font=('Trebuchet MS', 22, "bold"),
          anchor=N).pack(pady=20)
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=9, text="""
from tkinter import *

root = Tk()

mainmenu = Menu(root)
root.config(menu=mainmenu)

root.mainloop()
        """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    f = open("C:/python-learn/tkinter-coursework-2/texts/menuLesson/2.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=6, text="""
...
mainmenu.add_command(label="Файл")
mainmenu.add_command(label="Довідка")
...
            """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/menu/1.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/menuLesson/3.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=25, text="""
from tkinter import *

root = Tk()

mainmenu = Menu(root)

root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Новий")
filemenu.add_command(label="Відкрити...")
filemenu.add_command(label="Зберегти...")
filemenu.add_command(label="Вихід")

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Допомога")
helpmenu.add_command(label="Про програму")

mainmenu.add_cascade(label="Файл", 
                        menu=filemenu)
mainmenu.add_cascade(label="Довідка", 
                        menu=helpmenu)

root.mainloop()
                """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/menu/2.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/menuLesson/4.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=20, text="""
...
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Новий")
filemenu.add_command(label="Відкрити...")
filemenu.add_command(label="Зберегти...")
filemenu.add_command(label="Вихід")

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Про програму")

helpmenu1 = Menu(helpmenu, tearoff=0)
helpmenu1.add_command(label='Локальна довідка')
helpmenu1.add_command(label='Довідка на сайті')

helpmenu.add_cascade(label="Допомога", menu=helpmenu1)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Довідка", menu=helpmenu)
...
    """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/menu/3.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/menuLesson/5.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=14, text="""
...
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Новий")

filemenu.add_separator()

filemenu.add_command(label="Відкрити...")
filemenu.add_command(label="Зберегти...")

filemenu.add_separator()

filemenu.add_command(label="Вихід")    
...
    """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/menu/4.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/menuLesson/6.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=44, text="""
from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300, 
                                bg="white")


def drawOval():
    canvas.create_oval(x, y, x+50, y+50)


def drawRect():
    canvas.create_rectangle(x, y, x+50, y+50)


def drawTria():
    canvas.create_polygon((x, y), (x+25, y-50), 
        (x+50, y), fill='white', outline="black")


canvas.pack()

menu = Menu(root, tearoff=0)
menu.add_command(label="Круг", command=drawOval)
menu.add_command(label="Квадрат", command=drawRect)
menu.add_command(label="Трикутник", 
                            command=drawTria)

x = 0
y = 0


def popup(event):
    global x, y
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)


root.bind("<Button-3>", popup)

root.mainloop()
        """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/menu/5.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/menuLesson/7.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, text='Практична робота', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/menuLesson/8.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/menu/6.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage

    def nextLesson():
        window.destroy()
        placeLesson()

    def preLesson():
        window.destroy()
        messageBoxLesson()

    frame = Frame(win)
    Button(frame, text=" < Попередня тема < ", command=preLesson).pack(side=LEFT, anchor=SW, pady=10, padx=10)
    Button(frame, text=" > Наступна тема > ", command=nextLesson).pack(side=LEFT, anchor=SE, pady=10, padx=10)
    frame.pack(pady=20)
    del frame
    win.pack(fill=BOTH, expand=True)


image15 = Image.open('C:/python-learn/tkinter-coursework-2/image.gif')
new_image = image15.resize((50, 50))
image15 = ImageTk.PhotoImage(new_image)

def placeLesson():
    global w, h, codeFont
    window = Toplevel(root)
    window.geometry("600x700+{}+{}".format(w, h))
    window.resizable(False, False)
    window.title('place()')
    window.iconbitmap('C:/python-learn/tkinter-coursework-2/icon.ico')
    window.grab_set()
    window.focus_set()

    mainframe = VerticalScrolledFrame(window, borderwidth=2, relief=SUNKEN)
    win = mainframe

    f = open("C:/python-learn/tkinter-coursework-2/texts/placeLesson/1.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()

    Label(win, text='Метод place()', font=('Trebuchet MS', 22, "bold"),
          anchor=N).pack(pady=20)
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/place/1.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/placeLesson/2.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=13, text="""
from tkinter import *

root = Tk()
root.geometry('150x150')

# Задаємо постійні координати, в яких буде кнопка
Button(bg='red').place(x=75, y=20) 

# Задаємо координати відносно ширини та висоти вікна
Button(bg='green').place(relx=0.3, rely=0.5)

root.mainloop()
    """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/place/2.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    Label(win, text='Розтягуємо вікно, і бачимо, як другий віджет залежить від розмірів',
          font=('Trebuchet MS', 12), justify=LEFT).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/place/3.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/placeLesson/3.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=7, text="""
...
Label(bg="lightgreen").place(x=10, y=10, 
                    width=100, height=30)
Label(bg="lightblue").place(x=10, y=50, 
            relwidth=0.3, relheight=0.15)
...
        """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/place/4.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    Label(win, text='Розтягуємо вікно, і бачимо, як другий віджет залежить від розмірів',
          font=('Trebuchet MS', 12), justify=LEFT).pack()
    image = ImageTk.PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/place/5.gif")
    labelImage = Label(win, image=image)
    labelImage.image = image
    labelImage.pack(pady=10)
    del image, labelImage
    f = open("C:/python-learn/tkinter-coursework-2/texts/placeLesson/4.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, text='Практична робота', font=('Trebuchet MS', 22, "bold")).pack(pady=10)
    f = open("C:/python-learn/tkinter-coursework-2/texts/placeLesson/5.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text
    Label(win, height=14, text="""
...
image = Image.open("назва файлу")
# Змінюємо розміри зображення
new_image = image.resize((нова ширина зображення,
                        нова довжина зображення))
# Відкриваємо редаговане зображення через PhotoImage
image = ImageTk.PhotoImage(new_image)

# Розміщуємо зображення на мітці
labelImage = Label(root, image=image)
labelImage.image = image
labelImage.pack()
...
            """, bg="black", bd=3, relief=GROOVE, fg="green", justify=LEFT, font=codeFont).pack()
    f = open("C:/python-learn/tkinter-coursework-2/texts/placeLesson/6.txt", 'r', encoding="utf-8")
    text = f.read()
    f.close()
    Label(win, text=text, font=('Trebuchet MS', 12), justify=LEFT).pack()
    del text

    def example():
        global image15
        app = Toplevel()
        app.title("Приклад")
        app.grab_set()
        app.focus_set()
        app.geometry("500x500")

        def placeIn():
            s = app.geometry()
            s = s.split('+')
            s = s[0].split('x')
            width_w = int(s[0]) - 50
            height_h = int(s[1]) - 50
            x = r.randint(0, width_w)
            y = r.randint(0, height_h)
            but.place(x=int(x), y=int(y))

        but = Button(app, image=image15, command=placeIn)
        but.image = image15
        but.place(x=200, y=200)

        app.mainloop()

    Button(win, width=300, height=30, text="Запустити зразок", compound="left", image=buttonImage,
           font=butFont, command=example).pack(pady=20, padx=140)
    del example

    def preLesson():
        window.destroy()
        menuLesson()

    frame = Frame(win)
    Button(frame, text=" < Попередня тема < ", command=preLesson).pack(side=LEFT, anchor=SW, pady=10, padx=10)
    frame.pack(pady=20)
    del frame
    win.pack(fill=BOTH, expand=True)


# Setting default image and font for each button
buttonImage = PhotoImage(file="C:/python-learn/tkinter-coursework-2/images/buttonImage.gif")
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
                 anchor=W, font=butFont, command=packLesson)
button3.pack(padx=140, pady=10)

button4 = Button(frame, width=300, height=30, text=" Text - велике текстове поле",
                 compound='left', image=buttonImage, anchor=W, font=butFont, command=textLesson)
button4.pack(padx=140)

button5 = Button(frame, width=300, height=30, text=" Radiobutton, Checkbutton", compound='left', image=buttonImage,
                 anchor=W, font=butFont, command=racheLesson)
button5.pack(padx=140, pady=10)

button6 = Button(frame, width=300, height=30, text=" віджет Listbox()", compound='left', image=buttonImage,
                 anchor=W, font=butFont, command=listboxLesson)
button6.pack(padx=140)

button7 = Button(frame, width=300, height=30, text=" метод bind()", compound='left', image=buttonImage,
                 anchor=W, font=butFont, command=bindLesson)
button7.pack(padx=140, pady=10)

button8 = Button(frame, width=300, height=30, text=" Події", compound='left', image=buttonImage, anchor=W
                 , font=butFont, command=eventLesson)
button8.pack(padx=140)

button9 = Button(frame, width=300, height=30, text=" Canvas", compound='left', image=buttonImage, anchor=W,
                 font=butFont, command=canvasLesson)
button9.pack(padx=140, pady=10)

button10 = Button(frame, width=300, height=30, text=" Canvas. Ідентифікатори та теги",
                  compound='left', image=buttonImage, anchor=W, font=butFont, command=idtagLesson)
button10.pack(padx=140)

button11 = Button(frame, width=300, height=30, text=" Вікна", compound='left', image=buttonImage, anchor=W,
                  font=butFont, command=windowLesson)
button11.pack(padx=140, pady=10)

button12 = Button(frame, width=300, height=30, text=" метод grid()", compound='left', image=buttonImage,
                  anchor=W, font=butFont, command=gridLesson)
button12.pack(padx=140)

button13 = Button(frame, width=300, height=30, text=" Діалогові вікна", compound='left', image=buttonImage,
                  anchor=W, font=butFont, command=messageBoxLesson)
button13.pack(padx=140, pady=10)

button14 = Button(frame, width=300, height=30, text=" Віджет Menu()", compound='left', image=buttonImage,
                  anchor=W, font=butFont, command=menuLesson)
button14.pack(padx=140)

button15 = Button(frame, width=300, height=30, text=" метод place()", compound='left', image=buttonImage, anchor=W
                  , font=butFont, command=placeLesson)
button15.pack(padx=140, pady=10)


root.mainloop()
