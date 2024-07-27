import random
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showwarning, showinfo
from PIL import ImageTk, Image
from time import strftime


class App(Tk):

    def __init__(self):
        super().__init__()

        self.title('Hotel Management System | Project 9')
        self.configure(bg='white')

        self.cafe_icon = ImageTk.PhotoImage(Image.open('cafe.jpg'))
        self.logo = Label(self, image=self.cafe_icon, bg="white")
        self.logo.place(x=0, y=0)

        self.create_widgets()
        self.resizable(False, False)

    def create_widgets(self):
        style = ttk.Style(self)
        style.configure('TButton', background='black', foreground='black')

        self.label = ttk.Label(self, text="  ~ Hotel Management System ~  ", font=('Comic Sans MS', 16, 'bold'), background='white',
                               foreground='#248aa2')
        self.label.pack(pady=10)

        self.time_label = ttk.Label(self, font=('Digital-7', 20), background=self.rgb_hex(35, 35, 35), foreground='white')
        self.time_label.pack(side=TOP, anchor=NE, pady=5, padx=10)

        labelframe_style = {'background': 'white', 'foreground': '#248aa2', 'font': ['High Tower Text', 12, 'bold'],
                            'borderwidth': 3, 'highlightbackground': 'black'}
        self.left_frame = LabelFrame(self, text='Menu', **labelframe_style)
        self.left_frame.pack(side=LEFT, anchor=NW, padx=10, pady=10)

        self.middle_frame = LabelFrame(self, text='Bill', **labelframe_style)
        self.middle_frame.pack(side=LEFT, anchor=N, padx=10, pady=10)

        self.calculator_frame = LabelFrame(self, text='Calculator', **labelframe_style)
        self.calculator_frame.pack(side=RIGHT, anchor=NE, padx=10, pady=40)

        self.show_time()
        self.show_product()
        self.show_bill()
        self.show_button()
        self.show_calculator()

    def rgb_hex(self, r, g, b):
        return f'#{r:02x}{g:02x}{b:02x}'

    def show_product(self):
        self.label_style = {'foreground': 'black', 'background': 'white', 'font': ('verdana', 10, 'bold')}
        entry_style = {'width': 8, 'borderwidth': 4, 'relief': 'sunken', 'bg': "#fbf9ef"}

        items = ['Green tea', 'Sushi', 'Udon', 'Tofu', 'Tempura', 'Ramen', 'Soba', 'Miso Soup']
        self.entries = []

        for row, item in enumerate(items):
            ttk.Label(self.left_frame, text=item, **self.label_style).grid(row=row, column=0, padx=5)
            entry = Entry(self.left_frame, **entry_style)
            entry.grid(row=row, column=1)
            self.entries.append(entry)

        def price():
            show = (" Name - Price \n Green tea: ¥100 \n Sushi: ¥250 \n Udon: ¥460 \n Tofu: ¥330 \n Tempura: ¥400 \n "
                    "Ramen: ¥190 \n Soba: ¥164 \n Miso Soup: ¥150")
            showinfo(title='Price', message=show)

        Button(self.left_frame, text='Show Price', command=price, background='white').grid(row=8, column=0, columnspan=2, pady=5)

    def show_bill(self):
        entry_style = {'width': 8, 'borderwidth': 4, 'relief': 'sunken', 'background': 'lightblue', 'state': 'readonly'}
        items = ['Order Id: ', 'Service charges', 'Item Cost', 'Tax', 'Sub tax', 'Total Cost']
        self.bill_entries = []

        for row, item in enumerate(items):
            ttk.Label(self.middle_frame, text=item, **self.label_style).grid(row=row, column=0, padx=5)
            entry = Entry(self.middle_frame, **entry_style)
            entry.grid(row=row, column=1, padx=5)
            self.bill_entries.append(entry)

        self.button_frame = Frame(self.middle_frame, background='white')
        self.button_frame.grid(row=6, column=0, columnspan=2, pady=10)

    def show_button(self):
        def calculate_bill():
            number = random.randint(100, 10000)
            item_prices = [100, 250, 460, 330, 400, 190, 164, 150]
            service_charge = 51
            item_quantities = []

            try:
                item_quantities = [int(entry.get()) if entry.get() else 0 for entry in self.entries]
            except ValueError:
                showwarning("Input Error", "Please enter valid quantities for the items.")
                return

            if any(qty < 0 for qty in item_quantities):
                showwarning("Input Error", "Quantities cannot be negative.")
                return

            if sum(item_quantities) != 0:
                item_cost = sum(qty * price for qty, price in zip(item_quantities, item_prices))
                tax_cost = (item_cost / 100) * 8
                sub_tax = random.randint(50, 60)
                total_cost = item_cost + tax_cost + sub_tax + service_charge
            else:
                item_cost, tax_cost, sub_tax, total_cost, service_charge = (0, 0, 0, 0, 0)

            x = 0
            for entry, value in zip(self.bill_entries, [number, service_charge, item_cost, tax_cost, sub_tax, total_cost]):
                entry.config(state='normal')
                entry.delete(0, END)
                if x == 0:
                    entry.insert(0, value)
                    x += 1
                else:
                    entry.insert(0, f"¥{value:.2f}")

        def clear_entries():
            for entry in self.entries:
                entry.delete(0, END)
            for entry in self.bill_entries:
                entry.config(state=NORMAL)
                entry.delete(0, END)
                entry.config(state='readonly')

        ttk.Button(self.button_frame, text='Total', command=calculate_bill).pack(side=LEFT, anchor=SW, padx=10, ipadx=5)
        ttk.Button(self.button_frame, text='Clear', command=clear_entries).pack(side=LEFT, anchor=SW, padx=10, ipadx=5)

    def show_time(self):
        def time_string():
            return strftime('%H:%M:%S')

        def update_time():
            self.time_label.config(text=time_string(), background='black', foreground='white')
            self.time_label.after(1000, update_time)

        update_time()

    def show_calculator(self):
        def Calculation(value):
            if value == '=':
                try:
                    result = eval(data.get().replace('÷', '/').replace('x', '*'))
                    data.set(result)
                except ZeroDivisionError:
                    data.set("Error")
                    showwarning("Math Error", "Cannot divide by zero.")
                except Exception as e:
                    data.set("Error")
                    showwarning("Calculation Error", str(e))
            elif value == 'C':
                data.set("")
            else:
                data.set(data.get() + value)

        data = StringVar()

        entry = ttk.Entry(self.calculator_frame, font=['Candara', 12], textvariable=data)
        entry.grid(row=0, column=0, columnspan=4, pady=5, padx=3)
        entry.focus()

        buttons = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('x', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('÷', 4, 3)
        ]

        for (text, row, col) in buttons:
            Button(self.calculator_frame, text=text, command=lambda t=text: Calculation(t), width=5).grid(row=row,
                                                                                                          column=col)


if __name__ == "__main__":
    HotelManagementSystems = App()
    HotelManagementSystems.mainloop()
