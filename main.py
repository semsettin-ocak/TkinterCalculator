import tkinter as tk


class Screen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol('WM_DELETE_WINDOW', self.exit)

        self.title('Basic Calculator')
        self.resizable(width=False, height=False)
        self.geometry('380x400')
        self.FONT = ('Courier New', 14, 'normal')
        self.FONT2 = ('Courier New', 14, 'bold')
        self.config(bg='light blue', pady=15)

        self.label1 = tk.Label(text='Enter first number', font=self.FONT, bg='light blue')
        self.label1.pack()

        self.entry1 = tk.Entry(width=20, bg='light green')
        self.entry1.pack()

        self.label2 = tk.Label(text='Enter second number', font=self.FONT, bg='light blue')
        self.label2.pack()

        self.entry2 = tk.Entry(width=20, bg='light green')
        self.entry2.pack()

        self.var = tk.IntVar()

        self.radio1 = tk.Radiobutton(text="Addition", variable=self.var, value=1,
                                     font=self.FONT, bg='light blue')
        self.radio1.place(x=70, y=100)

        self.radio2 = tk.Radiobutton(text="Subtraction", variable=self.var, value=2,
                                     font=self.FONT, bg='light blue')
        self.radio2.place(x=70, y=130)

        self.radio3 = tk.Radiobutton(text='Multiplication', variable=self.var, value=3,
                                     font=self.FONT, bg='light blue')
        self.radio3.place(x=70, y=160)

        self.radio4 = tk.Radiobutton(text='Division', variable=self.var, value=4,
                                     font=self.FONT, bg='light blue')
        self.radio4.place(x=70, y=190)

        self.button = tk.Button(text='Calculate', bg='light green', command=self.button_func, padx=10, pady=6)
        self.button.place(x=125, y=225)

        self.button2 = tk.Button(text='Exit', bg='light green', command=self.exit, padx=10, pady=8)
        self.button2.place(x=120, y=330)

        self.result_label = tk.Label(text='Your result is: ', bg='light blue', font=self.FONT2)
        self.result_label.place(x=0, y=270)

    def button_func(self):
        if self.entry1.get() == '' or self.entry2.get() == '':
            self.result_label.config(text='Entries can not be empty!', fg='red')
        else:
            try:
                if self.var.get() == 1:
                    self.result_label.config(
                        text='Your result is:\n {}'.format(float(self.entry1.get()) + float(self.entry2.get())),
                        fg='red')
                elif self.var.get() == 2:
                    self.result_label.config(
                        text='Your result is:\n {}'.format(float(self.entry1.get()) - float(self.entry2.get())),
                        fg='red')
                elif self.var.get() == 3:
                    self.result_label.config(
                        text='Your result is:\n {}'.format(float(self.entry1.get()) * float(self.entry2.get())),
                        fg='red')
                elif self.var.get() == 4:
                    self.result_label.config(
                        text='Your result is:\n {}'.format(float(self.entry1.get()) / float(self.entry2.get())),
                        fg='red')
                else:
                    self.result_label.config(
                        text='Select the calculation type!', fg='red')
            except (ValueError, ZeroDivisionError):
                self.result_label.config(
                    text='Enter only valid numbers please!', fg='red')

    def exit(self):
        self.button2['bg'] = 'brown2'
        self.button2['text'] = 'Exiting..'
        self.button2['fg'] = 'white'
        self.button2['font'] = self.FONT2
        self.after(1111, self.destroy)


screen = Screen()
screen.mainloop()
