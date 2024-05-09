import tkinter as tk
def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2
def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)
def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)
def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)
def pr():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)
def deli():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)



window = tk.Tk()
window.title('СУПЕРКАЛЬКУЛЯТОР')
window.geometry("470x370")
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=4, height=2, command=add)
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text='-', width=4, height=2, command=sub)
button_sub.place(x=150, y=200)
button_pr = tk.Button(window, text='*', width=4, height=2, command=pr)
button_pr.place(x=200, y=200)
button_deli = tk.Button(window, text='/', width=4, height=2, command=deli)
button_deli.place(x=250, y=200)
number1_entry = tk.Entry(window, width=31)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=31)
number2_entry.place(x=100, y=125)
answer_entry = tk.Entry(window, width=31)
answer_entry.place(x=100, y=300)
number1 = tk.Label(window, text='Введите первое число: ')
number1.place(x=100, y=50)
number2 = tk.Label(window, text='Введите второе число: ')
number2.place(x=100, y=100)
answer = tk.Label(window, text='Результат: ')
answer.place(x=100, y=275)
window.mainloop()


