import tkinter as tk

screen = tk.Tk()
screen.title('Basic Calculator')
screen.resizable(width=False, height=False)
screen.geometry('320x350')
FONT = ('Courier New', 14, 'normal')
screen.config(bg='light blue', pady=15)

label1 = tk.Label(text='Enter first number', font=FONT, bg='light blue')
label1.pack()

entry1 = tk.Entry(width=20, bg='light green')
entry1.pack()

label2 = tk.Label(text='Enter second number', font=FONT, bg='light blue')
label2.pack()

entry2 = tk.Entry(width=20, bg='light green')
entry2.pack()

var = tk.IntVar()

radio1 = tk.Radiobutton(text="Addition", variable=var, value=1, font=FONT, bg='light blue')
radio1.place(x=70, y=100)

radio2 = tk.Radiobutton(text="Subtraction", variable=var, value=2, font=FONT, bg='light blue')
radio2.place(x=70, y=130)

radio3 = tk.Radiobutton(text='Multiplication', variable=var, value=3, font=FONT, bg='light blue')
radio3.place(x=70, y=160)

radio4 = tk.Radiobutton(text='Division', variable=var, value=4, font=FONT, bg='light blue')
radio4.place(x=70, y=190)

button = tk.Button(text='Calculate', bg='light green')
button.place(x=125, y=230)

result_label = tk.Label(text='Your result is: ', bg='light blue', font=FONT)
result_label.place(x=80, y=260)

screen.mainloop()
