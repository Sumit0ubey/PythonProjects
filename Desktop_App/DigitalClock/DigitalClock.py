import random
from tkinter import *
from tkinter import ttk
import time


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Digital Clock | Project 2')
        self.geometry('250x80')
        self.iconbitmap('clock.ico')
        self.resizable(False, False)

        n = random.randint(0, 6)
        colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple', 'brown', 'pink']

        self.style = ttk.Style(self)
        self.style.configure('TLabel', background='black', foreground=colors[n])
        self['bg'] = 'black'

        self.label = ttk.Label(self, text=self.time_string(), font=('Digital-7', 40))
        self.label.pack(expand=True)

        self.label.after(1000, self.update)

    def time_string(self):
        return time.strftime('%H:%M:%S')

    def update(self):
        self.label.configure(text=self.time_string())
        self.label.after(1000, self.update)


if __name__ == "__main__":
    app = App()
    app.mainloop()
