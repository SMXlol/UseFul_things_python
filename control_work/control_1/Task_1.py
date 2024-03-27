import tkinter as tk


def up():
    label.config(text="верх")


def down():
    label.config(text="низ")


def right():
    label.config(text="право")


def left():
    label.config(text="лево")


root = tk.Tk()
root.geometry("400x400")
root.title("Нажмите кнопку")

frame = tk.Frame(root)
frame.pack(expand=True)

button_up = tk.Button(frame, text="Вверх", command=up)
button_up.pack(side=tk.TOP)

button_down = tk.Button(frame, text="Вниз", command=down)
button_down.pack(side=tk.BOTTOM)

button_right = tk.Button(frame, text="Вправо", command=right)
button_right.pack(side=tk.RIGHT)

button_left = tk.Button(frame, text="Влево", command=left)
button_left.pack(side=tk.LEFT)

label = tk.Label(root, text="")
label.pack()

root.mainloop()
