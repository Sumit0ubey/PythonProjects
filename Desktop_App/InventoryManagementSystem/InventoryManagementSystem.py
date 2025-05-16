import sqlite3 as sql
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Inventory Management System')
        self.configure(bg='#333333')
        self.geometry('680x440')
        self.resizable(False, False)

        self.login_frame = Frame(self, bg='#333333')
        self.create_login_frame()
        self.login_frame.pack()

        self.main_frame = Frame(self, bg='#333333')
        self.create_main_frame()

        self.mainloop()

    def create_login_frame(self):
        Label(self.login_frame, text="Login", bg='#333333', fg="#FFFFFF", font=("Book Antiqua", 30, "bold")).grid(row=0,
                                                                                                                  column=0,
                                                                                                                  columnspan=2,
                                                                                                                  sticky="news",
                                                                                                                  pady=40)
        Label(self.login_frame, text="Username: ", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).grid(row=1, column=0)
        Label(self.login_frame, text="Password: ", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).grid(row=2, column=0)

        self.username_entry = Entry(self.login_frame, font=("Arial", 16))
        self.password_entry = Entry(self.login_frame, show="*", font=("Arial", 16))
        self.username_entry.grid(row=1, column=1, pady=20)
        self.password_entry.grid(row=2, column=1, pady=20)

        Button(self.login_frame, text="Login", bg="black", fg="#FFFFFF", font=("Arial", 16), command=self.login).grid(
            row=3, column=0, columnspan=2, pady=30)

    def create_main_frame(self):
        ttk.Label(self.main_frame, text='Inventory Management System', font=['Comic Sans MS', 14], background='#333333',
                  foreground='white').grid(row=0, column=2, columnspan=2, sticky=N, pady=10)

        label_style = {'background': '#333333', 'foreground': 'white', 'font': ['Cambria', 10]}
        ttk.Label(self.main_frame, text='Product ID: ', **label_style).grid(row=1, column=0, sticky=W)
        ttk.Label(self.main_frame, text='Product Name: ', **label_style).grid(row=2, column=0, sticky=W)
        ttk.Label(self.main_frame, text='Product Quantity: ', **label_style).grid(row=3, column=0, sticky=W)
        ttk.Label(self.main_frame, text='Product Price: ', **label_style).grid(row=4, column=0, sticky=W)

        self.product_id = ttk.Entry(self.main_frame, width=60)
        self.product_name = ttk.Entry(self.main_frame, width=60)
        self.product_quantity = ttk.Entry(self.main_frame, width=60)
        self.product_price = ttk.Entry(self.main_frame, width=60)

        entries = [self.product_id, self.product_name, self.product_quantity, self.product_price]
        for row, entry in enumerate(entries, start=1):
            entry.grid(row=row, column=1, columnspan=7, pady=10)

        Button(self.main_frame, text="Add Product", command=self.add_product).grid(row=5, column=0)
        Button(self.main_frame, text="Edit Product", command=self.edit_product).grid(row=5, column=1)
        Button(self.main_frame, text="Delete Product", command=self.delete_product).grid(row=5, column=2)
        Button(self.main_frame, text="Low Stock Alert", command=self.low_stock_alert).grid(row=5, column=3)
        Button(self.main_frame, text="Sales Summary", command=self.sales_summary).grid(row=5, column=4)

        self.product_list = Listbox(self.main_frame, width=80, height=10)
        self.product_list.grid(row=6, column=0, columnspan=5, pady=10)

        self.load_products()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        database = sql.connect('Inventory_Storage.db')
        query = database.cursor()

        query.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = query.fetchone()

        if user:
            self.login_frame.pack_forget()
            self.main_frame.pack()
        else:
            showerror("Error", "Invalid username or password")
        database.close()

    def add_product(self):
        product_id = self.product_id.get()
        name = self.product_name.get()
        quantity = self.product_quantity.get()
        price = self.product_price.get()

        if not product_id or not name or not quantity.isdigit() or not price.replace('.', '', 1).isdigit():
            showerror("Error", "Invalid input")
            return

        database = sql.connect('Inventory_Storage.db')
        query = database.cursor()

        query.execute("INSERT INTO products (product_id, product_name, quantity, price) VALUES (?, ?, ?, ?)",
                  (product_id, name, int(quantity), float(price)))

        database.commit()
        database.close()

        self.load_products()

    def edit_product(self):
        selected = self.product_list.curselection()
        if not selected:
            showerror("Error", "No product selected")
            return

        product_id = self.product_list.get(selected[0]).split(' - ')[0]
        new_id = self.product_id.get()
        name = self.product_name.get()
        quantity = self.product_quantity.get()
        price = self.product_price.get()

        if not new_id or not name or not quantity.isdigit() or not price.replace('.', '', 1).isdigit():
            showerror("Error", "Invalid input")
            return

        database = sql.connect('Inventory_Storage.db')
        query = database.cursor()

        query.execute("UPDATE products SET product_id = ?, product_name = ?, quantity = ?, price = ? WHERE product_id = ?",
                  (new_id, name, int(quantity), float(price), product_id))

        database.commit()
        database.close()

        self.load_products()

    def delete_product(self):
        selected = self.product_list.curselection()
        if not selected:
            showerror("Error", "No product selected")
            return

        product_id = self.product_list.get(selected[0]).split(' - ')[0]

        database = sql.connect('Inventory_Storage.db')
        query = database.cursor()

        query.execute("DELETE FROM products WHERE product_id = ?", (product_id,))

        database.commit()
        database.close()

        self.load_products()

    def load_products(self):
        self.product_list.delete(0, END)

        database = sql.connect('Inventory_Storage.db')
        query = database.cursor()

        query.execute("SELECT * FROM products")
        products = query.fetchall()

        for product in products:
            self.product_list.insert(END, f"{product[0]} - {product[1]} (Qty: {product[2]}, Price: {product[3]})")

        database.close()

    def low_stock_alert(self):
        database = sql.connect('Inventory_Storage.db')
        query = database.cursor()

        query.execute("SELECT * FROM products WHERE quantity < 10")
        products = query.fetchall()

        alert_message = "Low Stock Products:\n"
        for product in products:
            alert_message += f"{product[1]} (Qty: {product[2]})\n"

        showinfo("Low Stock Alert", alert_message)

        database.close()

    def sales_summary(self):
        database = sql.connect('inventory_Storage.db')
        query = database.cursor()

        query.execute("SELECT * FROM products")
        datas = query.fetchall()

        inform = ''
        for data in datas:
            inform += str(data) + '\n'

        showinfo("Sales Summary", inform)


if __name__ == "__main__":
    inventoryManagementApp = App()
