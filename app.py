import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Menu


window = Tk()

# а что ты хотел здесь найти ඞ

window.title("amogus.py v1.0 ru")
window.geometry('300x300')
text1 = Label(window, text="ඞ Amogus", font=("Segoe UI Light", 30))
text2 = Label(window, text="When the imposter is sus", font=("Segoe UI Light", 10))
text3 = Label(window, text="Программа еще в разработке и пока еще мало вещей. \nВерсия 1.0 на русском", font=("Segoe UI Light", 10))
text1.grid(column=0, row=0)
text2.grid(column=0, row=1)
text3.grid(column=0, row=6)


def clicked():

    messagebox.showinfo('Поздравляем!', 'Поздравляем, вы стали sussy bakoй')

def clicked2():

    messagebox.showinfo('sus', 'You are very sus')

def clicked3():

    messagebox.showinfo('ыгы', 'Нщг фку мукн ыгы')


def clicked4():
    poslat = messagebox.askyesno('Послать друга','Вы хотите потерять своего друга')
    poslat = messagebox.askyesno('Послать друга','Напишите вашему другу что https://natribu.org это официальный сайт амогуса')

def clicked1():

    nahui = messagebox.askokcancel('Амогус','АМОГУС ОСКОРБЛЯЕТ ТЕБЯ')
    nahui = messagebox.askokcancel('Амогус','ИДИ НАХУЙ СУКА БЛЯТЬ ДОЛБАЕБ ТУПОЙ ПИДОРАСИНА')
    nahui = messagebox.askokcancel('Амогус','Ой извините')


btn = Button(window,text='Стать sussy bakой', command=clicked)
bt2 = Button(window,text='Оскорбить амогуса', command=clicked1)
bt3 = Button(window,text='SUS', command=clicked2)
bt4 = Button(window,text='ЫГЫ', command=clicked3)
bt5 = Button(window,text='Послать друга', command=clicked4)
res = messagebox.askquestion('Перед запуском программы','Вы sussy baka?')


btn.grid(column=0, row=2)
bt2.grid(column=0, row=3)
bt3.grid(column=0, row=4)
bt4.grid(column=0, row=5)
bt5.grid(column=0, row=7)
window.mainloop()
