from tkinter import *
import math

expression = ""


def input_bar_function(number, equation):
    global expression
    expression = expression + str(number)
    equation.set(expression)


def clear(equation):
    global expression
    expression = ""
    equation.set("Enter the expression")


def evaluate(equation):
    global expression
    # trying to evaluate the expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = ""

    except:
        equation.set("ERROR")
        expression = ""


def gui():
    window = Tk()
    window.title("CALCULATOR")
    window.geometry("310x185")
    window.configure(background="light blue")
    equation = StringVar()
    input_bar = Entry(window, textvariable=equation)
    input_bar.place(height=100)
    input_bar.grid(columnspan=4, ipadx=100, ipady=5)
    input_bar.configure(background="yellow")
    equation.set("Enter the equation")
    # BUTTONS
    _1 = Button(window, text=1, fg="black", bg="light blue", bd=2,
                command=lambda: input_bar_function(1, equation), height=1, width=7)
    _1.grid(row=2, column=0)
    _2 = Button(window, text=2, fg="black", bg="light blue", bd=2,
                command=lambda: input_bar_function(2, equation), height=1, width=7)
    _2.grid(row=2, column=1)
    _3 = Button(window, text=3, fg="black", bg="light blue", bd=2,
                command=lambda: input_bar_function(3, equation), height=1, width=7)
    _3.grid(row=2, column=2)
    _4 = Button(window, text=4, fg="black", bg="light blue", bd=2,
                command=lambda: input_bar_function(4, equation), height=1, width=7)
    _4.grid(row=4, column=0)
    _5 = Button(window, text=5, fg="black", bg="light blue", bd=2,
                command=lambda: input_bar_function(5, equation), height=1, width=7)
    _5.grid(row=4, column=1)
    _6 = Button(window, text=6, fg="black", bg="light blue", bd=2,
                command=lambda: input_bar_function(6, equation), height=1, width=7)
    _6.grid(row=4, column=2)
    _7 = Button(window, text=7, fg="black", bg="light blue", bd=2,
                command=lambda: input_bar_function(7, equation), height=1, width=7)
    _7.grid(row=6, column=0)
    _8 = Button(window, text=8, fg="black", bg="light blue", bd=2,
                command=lambda: input_bar_function(8, equation), height=1, width=7)
    _8.grid(row=6, column=1)
    _9 = Button(window, text=9, fg="black", bg="light blue", bd=2,
                command=lambda: input_bar_function(9, equation), height=1, width=7)
    _9.grid(row=6, column=2)
    _0 = Button(window, text=0, fg="black", bg="light blue", bd=2,
                command=lambda: input_bar_function(0, equation), height=1, width=7)
    _0.grid(row=7, column=1)
    plus = Button(window, text='+', fg="black", bg="light blue", bd=2,
                  command=lambda: input_bar_function('+', equation), height=1, width=7)
    plus.grid(row=7, column=0)
    minus = Button(window, text='-', fg="black", bg="light blue", bd=2,
                   command=lambda: input_bar_function('-', equation), height=1, width=7)
    minus.grid(row=8, column=0)
    multi = Button(window, text='*', fg="black", bg="light blue", bd=2,
                   command=lambda: input_bar_function('*', equation), height=1, width=7)
    multi.grid(row=7, column=2)
    division = Button(window, text='/', fg="black", bg="light blue", bd=2,
                      command=lambda: input_bar_function('/', equation), height=1, width=7)
    division.grid(row=8, column=2)
    equal = Button(window, text='=', fg="black", bg="light blue", bd=2,
                   command=lambda: evaluate(equation), height=1, width=7)
    equal.grid(row=8, column=1)
    clear_b = Button(window, text='C', fg="black", bg="light blue", bd=2,
                     command=lambda: clear(equation), height=1, width=7)
    clear_b.grid(row=9, column=0)
    decimal = Button(window, text='.', fg="black", bg="light blue", bd=2,
                     command=lambda: input_bar_function('.', equation), height=1, width=7)
    decimal.grid(row=9, column=1)

    window.mainloop()


if __name__ == "__main__":
    gui()