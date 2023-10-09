import math
from tkinter import *
                        # 1 - 2 = импортируем ткинтер для появления окна

root = Tk()
root.geometry('380x300')
root.title('Калькулятор')
root.config(background='Gray')

                        # 5 - 8 = задаем размер, название и цвет бэка у окна

exp = ''

result = StringVar()
pole_vvoda = Entry(textvariable=result)
pole_vvoda.grid(columnspan=4, ipadx=90)

                        # 14 - 16 = делаем result только для значений String. создаем поле ввода, которое отображает result. прикрепляем и указываем на сколько колонок располагается и задаем сколько будет занимать одна колонка по оси x

def press(num):
    global exp
    exp += str(num)
    result.set(exp)

#

def ravno_press():
    try:
        global exp
        total = str(eval(exp))
        result.set(total)
        exp = total
    except:
        result.set('ERROR :(')

def sqrt_exp():
    global exp
    total = str(math.sqrt(eval(exp)))
    result.set(total)
    exp = total

def sqr_exp():
    global exp
    total = str((eval(exp) * (eval(exp))))
    result.set(total)
    exp = total

def reset():
    global exp
    total = ''
    result.set(total)
    exp = total

                        # 20 - 52 = создаем функции, которые будут работать при нажатии на кнопку


button1 = Button(text = '1', height=3, width=10, command=lambda: press(1))
button1.grid(row=8, column=0)

button2 = Button(text = '2', height=3, width=10, command=lambda: press(2))
button2.grid(row=8, column=1)

button3 = Button(text = '3', height=3, width=10, command=lambda: press(3))
button3.grid(row=8, column=2)

button4 = Button(text = '4', height=3, width=10, command=lambda: press(4))
button4.grid(row=7, column=0)

button5 = Button(text = '5', height=3, width=10, command=lambda: press(5))
button5.grid(row=7, column=1)

button6 = Button(text = '6', height=3, width=10, command=lambda: press(6))
button6.grid(row=7, column=2)

button7 = Button(text = '7', height=3, width=10, command=lambda: press(7))
button7.grid(row=6, column=0)

button8 = Button(text = '8', height=3, width=10, command=lambda: press(8))
button8.grid(row=6, column=1)

button9 = Button(text = '9', height=3, width=10, command=lambda: press(9))
button9.grid(row=6, column=2)

button0 = Button(text = '0', height=3, width=10, command=lambda: press(0))
button0.grid(row=9, column=1)

plus = Button(text = '+', height=3, width=10, command=lambda: press('+'))
plus.grid(row=8,column=4)

minus = Button(text = '-', height=3, width=10, command=lambda: press('-'))
minus.grid(row=7,column=4)

ravno = Button(text = '=', height=3, width=10, command=ravno_press)
ravno.grid(row=9,column=4)

umn = Button(text = '*', height=3, width=10, command=lambda: press('*'))
umn.grid(row=6,column=4)

delit = Button(text = '/', height=3, width=10, command=lambda: press('/'))
delit.grid(row=5,column=4)

koren = Button(text = 'sqrt', height=3, width=10, command=sqrt_exp)
koren.grid(row=5,column=2)

sqr = Button(text = 'sqr', height=3, width=10, command=sqr_exp)
sqr.grid(row=5,column=1)

reset = Button(text = 'RESET', height=3, width=10, command=reset)
reset.grid(row=5,column=0)

zap = Button(text = ',', height=3, width=10, command=lambda: press('.'))
zap.grid(row=9,column=2)

                            # 57 - 112 = создаем кнопки, как они отображаются, высоту, ширину. задаем команду для каждой кнопки. задаем расположение кнопки(строка и столбец)

root.mainloop()

                            # 116 = запускаем бесконечный цикл

