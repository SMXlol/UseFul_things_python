from tkinter import *


def calculate():
    try:
        result = sum([int(num) for num in numbers.get().split()])
        result_label.config(text=f"Результат: {result}")
    except:
        result_label.config(text="Ошибка")


root = Tk()
root.geometry("400x300")
root.title("Калькулятор")

frame = Frame(root)
frame.pack(expand=True)

numbers = Entry(frame, width=40)
numbers.grid(row=0, column=0, columnspan=3)

equal_button = Button(frame, text="=", command=calculate)
equal_button.grid(row=1, column=1)

result_label = Label(frame, text="Результат: ")
result_label.grid(row=2, column=0, columnspan=3)

root.mainloop()
