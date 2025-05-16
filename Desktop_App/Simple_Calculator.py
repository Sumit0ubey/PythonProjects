from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showwarning


def calculation(value):
    if value == '=':
        try:
            result = eval(data.get().replace('÷', '/').replace('x', '*'))
            data.set(result)
        except Exception as e:
            data.set("Error")
            showwarning(title='Error', message=e)
    elif value == 'C':
        data.set("")
    else:
        data.set(data.get() + value)


window = Tk()
window.title('Calculator | Project 4')
window.geometry(f'{350}x{280}+'
                f'{int(window.winfo_screenwidth() / 2 - 350 / 2)}+'
                f'{int(window.winfo_screenheight() / 2 - 280 / 2)}')
window.resizable(False, False)
window.configure(bg='#333333')

ttk.Label(window, text='~ Calculator ~', background='#333333', foreground='white', font=['Comic Sans MS', 16]).pack(pady=10)

Calculator_frame = Frame(window, bg='#333333')

style = ttk.Style(Calculator_frame)
style.configure('TButton', background='black', foreground='black')

data = StringVar()

entry = ttk.Entry(Calculator_frame, width=35, font=['Candara', 12], textvariable=data)
entry.grid(row=0, column=0, columnspan=4, pady=15)

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('x', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('÷', 4, 3)
]

for (text, row, col) in buttons:
    ttk.Button(Calculator_frame, text=text, command=lambda t=text: calculation(t)).grid(row=row, column=col, padx=3, pady=5)

Calculator_frame.pack(side=LEFT, expand=TRUE, fill=BOTH, padx=10, pady=10)

window.mainloop()
