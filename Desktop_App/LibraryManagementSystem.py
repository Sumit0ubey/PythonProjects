import sqlite3 as sql
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, showwarning, askokcancel, WARNING
from datetime import datetime
from qrcode import make


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Library Management System')
        self.geometry('700x500')
        self.resizable(False, False)
        self.config(background='#333333')
        self.menu()
        self.create_widgets()
        self.mainloop()

    def menu(self):
        self.Menubar = Menu(self)
        self.config(menu=self.Menubar)

        self.home_menu = Menu(self.Menubar, tearoff=0)
        self.home_menu.add_command(label='Books', command=self.books_list)

        self.student_homesubmenu = Menu(self.home_menu, tearoff=0)
        self.student_homesubmenu.add_command(label='Login', command=self.login_widget)
        self.student_homesubmenu.add_command(label='Register', command=self.register_widget)
        self.home_menu.add_cascade(label='Student', menu=self.student_homesubmenu)

        self.staff_homesubmenu = Menu(self.home_menu, tearoff=0)
        self.staff_homesubmenu.add_command(label='Login', command=lambda: self.login_widget(1))

        self.home_menu.add_cascade(label='Staff', menu=self.staff_homesubmenu)

        self.home_menu.add_separator()
        self.home_menu.add_command(label='Exit', command=self.destroy)
        self.Menubar.add_cascade(label='Home', menu=self.home_menu)

    def __everytime__(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.menu()

    def create_widgets(self):
        def welcome():
            display_text.configure(text='Welcome to\n Our Library', font=['Kristen ITC', 40])

        self.start_frame = Frame(self, background='#333333')
        display_text = ttk.Label(self.start_frame, text='Library Management ', font=['Comic Sans MS', 45, 'bold'], background='#333333', foreground='white')
        display_text.pack(expand=True, fill=BOTH, pady=160, padx=30)
        self.start_frame.pack()
        self.start_frame.after(2000, welcome)

    def login_widget(self, is_admin=0):
        def login_validation():
            username = self.username_entry.get()
            password = self.password_entry.get()

            with sql.connect('library.db') as database:
                query = database.cursor()
                query.execute("SELECT name, admin, user_id FROM users WHERE username = ? AND password = ?",
                              (username, int(password)))
                self.NAME = query.fetchone()

            if self.NAME:
                if is_admin == 0 and self.NAME[1] == 0:
                    self.student_panel()
                elif self.NAME[1] == 1 and is_admin == 1:
                    self.staff_panel()
                else:
                    showwarning(title='Not Exist', message='There is no such Admin')
            else:
                showerror(title='Incorrect', message='Username or Password is invalid')

        self.__everytime__()

        self.login_frame = Frame(self, background='#333333')
        Label(self.login_frame, text="Login", font=("Book Antiqua", 30, "bold"), background='#333333', foreground='white').grid(row=0,
                                                                                      column=0,
                                                                                      columnspan=2,
                                                                                      sticky="news",
                                                                                      pady=40)
        Label(self.login_frame, text="Username: ", font=("Arial", 16), background='#333333', foreground='white').grid(row=1, column=0)
        Label(self.login_frame, text="Password: ", font=("Arial", 16), background='#333333', foreground='white').grid(row=2, column=0)

        self.username_entry = Entry(self.login_frame, font=("Arial", 16))
        self.password_entry = Entry(self.login_frame, show="*", font=("Arial", 16))
        self.username_entry.grid(row=1, column=1, pady=20)
        self.password_entry.grid(row=2, column=1, pady=20)
        self.username_entry.focus()

        Button(self.login_frame, text="Login", font=("Arial", 16), command=login_validation, background='#333333', foreground='white').grid(
            row=3, column=0, columnspan=2, pady=30)

        self.login_frame.pack()

    def register_widget(self, is_admin=0):
        def register_validation():
            name = self.name_entry.get()
            username = self.username_entry.get()
            password1 = self.password_entry.get()
            password2 = self.confirm_password.get()

            if password1 != password2:
                showwarning(title='Mismatch', message='Passwords do not match')
                return

            with sql.connect('library.db') as database:
                query = database.cursor()
                query.execute("INSERT INTO users (name, username, password, admin) VALUES (?, ?, ?, ?)",
                              (name, username, int(password1), is_admin))

            self.login_widget()

        self.__everytime__()

        self.register_frame = Frame(self, background='#333333')
        labels, row = ['Full Name: ', 'Set Username: ', 'Password: ', 'Confirm Password: '], 1
        for label in labels:
            Label(self.register_frame, text=label, font=("Arial", 16), foreground='white', background='#333333').grid(row=row, column=0)
            row += 1
        Label(self.register_frame, text="Register Form", font=("Book Antiqua", 30, "bold"), background='#333333', foreground='white').grid(row=0,
                                                                                                 column=0,
                                                                                                 columnspan=2,
                                                                                                 sticky="news",
                                                                                                 pady=40)

        self.name_entry = Entry(self.register_frame, font=("Arial", 16))
        self.username_entry = Entry(self.register_frame, font=("Arial", 16))
        self.password_entry = Entry(self.register_frame, show="*", font=("Arial", 16))
        self.confirm_password = Entry(self.register_frame, show="*", font=("Arial", 16))
        self.name_entry.grid(row=1, column=1, pady=10)
        self.username_entry.grid(row=2, column=1, pady=10)
        self.password_entry.grid(row=3, column=1, pady=10)
        self.confirm_password.grid(row=4, column=1, pady=10)

        Button(self.register_frame, text="Register", font=("Arial", 16), command=register_validation, background='black', foreground='white').grid(
            row=5, column=0, columnspan=2, pady=20)

        self.register_frame.pack()

    def get_books(self, is_studentPanel=False):
        with sql.connect('library.db') as database:
            query = database.cursor()
            query.execute("SELECT book_id, book_name FROM books")
            gots = query.fetchall()

            if is_studentPanel:
                for got in gots:
                    self.list_of_books.insert(END, got)
            else:
                self.data = "Books in library: \n"
                for got in gots:
                    self.data += f' \t- Book Name: {got[1]}\n'
                self.book_data.insert(1.0, self.data)

    def books_list(self):

        self.__everytime__()

        self.book_frame = Frame(self, background='#333333')
        self.book_data = Text(self.book_frame, background='#333333', foreground='white')
        self.book_data.pack(expand=True, fill=BOTH)
        self.book_frame.pack(expand=True, fill=BOTH)

        self.get_books()

    def student_panel(self):
        def search():
            find = str(self.search.get())
            if find != "":
                with sql.connect('library.db') as database:
                    query = database.cursor()
                    query.execute("SELECT book_id, book_name FROM books WHERE book_name = ?", (find,))
                    books = query.fetchall()
            else:
                with sql.connect('library.db') as database:
                    query = database.cursor()
                    query.execute("SELECT book_id, book_name FROM books;")
                    books = query.fetchall()

            self.list_of_books.delete(0, END)
            for book in books:
                self.list_of_books.insert(END, book)
    
        def issued_books():
            with sql.connect('library.db') as database:
                query = database.cursor()
                query.execute("SELECT id, book_name FROM student_book WHERE student_id = ?", (self.NAME[2],))
                books = query.fetchall()
            if books != []:
                self.book_that_home.delete(0, END)
                for book in books:
                    self.book_that_home.insert(END, f"{book[0]} - {book[1]}")
            else:
                self.book_that_home.delete(0, END)
        
        def issue_book():
            selected = self.list_of_books.curselection()
            if not selected:
                showinfo(title='Information', message='None books selected')
                return
            selected_book = self.list_of_books.get(selected[0])
            with sql.connect('library.db') as database:
                query = database.cursor()
                query.execute("INSERT INTO student_book (student_id, book_id, book_name, date) VALUES (?, ?, ?, ?)", (int(self.NAME[2]), int(selected_book[0]), selected_book[1], datetime.now().strftime("%Y-%m-%d")))

            issued_books()

        def return_book():
            selected = self.book_that_home.curselection()
            if not selected:
                showinfo(title='Information', message='No books selected')
                return
            selectedBook = self.book_that_home.get(selected[0])
            book_id = int(selectedBook.split()[0])

            with sql.connect('library.db') as database:
                query = database.cursor()
                query.execute("SELECT date FROM student_book WHERE id = ?", (book_id,))
                got = query.fetchone()
                if got and got[0]:
                    booked_date = datetime.strptime(got[0], "%Y-%m-%d")
                    differenceInDays = datetime.now() - booked_date
                    difference = differenceInDays.days
                    if difference >= 9:
                        amount = 50 * (difference - 9)
                        answer = askokcancel(title="Alert", message=f'You have to pay a fine of {amount} for late return', icon=WARNING)
                        if answer:
                            data = f'upi://pay?pa=sumit2003dubey@ibl&pn=Library fee&am={amount}&tn=Fine for late return'
                            qrCode = make(data)
                            qrCode.show()
                        else:
                            return
                    query.execute("DELETE FROM student_book WHERE id = ?", (book_id,))
                    database.commit()
                showinfo(title='Information', message='Book returned successfully')
            issued_books()

        self.__everytime__()
        ttk.Label(text=f"Student Name: {self.NAME[0]}", font=['Eras Medium ITC', 16], background='#333333', foreground='white').pack(pady=5)
        self.student_frame = Frame(self, background='#333333')

        self.student_leftFrame = Frame(self, background='#333333')
        ttk.Label(self.student_leftFrame, text='Books that you have -', background='#333333', foreground='white', font=['Leelawadee UI', 13]).grid(row=0, column=0, sticky=W, pady=8)
        self.book_that_home = Listbox(self.student_leftFrame, width=45, height=10, bg='#333333', font=['Gadugi', 10, 'bold'], foreground='white')
        self.book_that_home.grid(row=1, column=0, columnspan=4, sticky=W)

        self.take_book = Button(self.student_leftFrame, text='Issue Book', command=issue_book, background='#333333', foreground='white')
        self.give_book = Button(self.student_leftFrame, text='Return book', command=return_book, background='#333333', foreground='white')
        self.take_book.grid(row=2, column=0, sticky=W, pady=6)
        self.give_book.grid(row=2, column=1, sticky=W, pady=6)
        self.info = ttk.Label(self.student_leftFrame, text='Note: \n There will be Fine of 50 rs per day \n \t In case of late return', font=['Microsoft Sans Serif', 14], foreground='white', background='#333333')
        self.info.grid(row=3, column=0, sticky=W, pady=10, padx=10, columnspan=4)
        self.student_leftFrame.pack(side=LEFT, anchor=NW, pady=25, padx=30)

        self.student_rightFrame = Frame(self, background='#333333')
        self.search = ttk.Entry(self.student_rightFrame, width=20, font=['Arial', 10])
        self.search.grid(row=0, column=0, sticky=E, padx=5)
        self.search_button = Button(self.student_rightFrame, text='Search', command=search, foreground='white', background='#333333')
        self.search_button.grid(row=0, column=1, padx=2, sticky=E)
        ttk.Label(self.student_rightFrame, text='Books in Library -', background='#333333', foreground='white', font=['Leelawadee UI', 13]).grid(row=1, column=0, sticky=W, pady=8)
        self.list_of_books = Listbox(self.student_rightFrame, width=30, bg='#333333', font=['Verdana', 10, 'bold'], foreground='white')
        self.list_of_books.grid(row=2, column=0, columnspan=4, padx=10, pady=5)
        self.student_rightFrame.pack(side=RIGHT, anchor=NE, pady=10, padx=10)

        self.student_frame.pack(expand=True, fill=BOTH, pady=10, padx=10)

        self.get_books(is_studentPanel=True)
        issued_books()

    def staff_panel(self):
        def load_products():
            self.book_list.delete(0, END)

            with sql.connect('library.db') as database:
                query = database.cursor()
                query.execute("SELECT * FROM books")
                books = query.fetchall()

            for book in books:
                self.book_list.insert(END, f"{book[0]} - {book[1]} (author: {book[2]}, lang: {book[3]})")

        def add_book():
            book_id = self.book_id.get()
            name = self.book_name.get()
            author = self.book_author.get()
            language = self.book_language.get()

            if not book_id or not name or not author or not language:
                showwarning("Warning", "Please fill all fields")
                return

            with sql.connect('library.db') as database:
                query = database.cursor()
                query.execute("INSERT INTO books (book_id, book_name, author, language) VALUES (?, ?, ?, ?)",
                              (int(book_id), name, author, language))

            load_products()

        def edit_book():
            selected = self.book_list.curselection()
            if not selected:
                showerror("Error", "No Book selected")
                return

            book_id = self.book_list.get(selected[0]).split(' - ')[0]
            new_id = self.book_id.get()
            name = self.book_name.get()
            author = self.book_author.get()
            language = self.book_language.get()

            if not new_id or not name or not author or not language:
                showwarning("Warning", "Please fill all fields")
                return

            with sql.connect('library.db') as database:
                query = database.cursor()
                query.execute("UPDATE books SET book_id = ?, book_name = ?, author = ?, language = ? WHERE book_id = ?",
                              (int(new_id), name, author, language, int(book_id)))

            load_products()

        def delete_book():
            selected = self.book_list.curselection()
            if not selected:
                showerror("Error", "No Book selected")
                return

            book_id = self.book_list.get(selected[0]).split(' - ')[0]

            with sql.connect('library.db') as database:
                query = database.cursor()
                query.execute("DELETE FROM books WHERE book_id = ?", (int(book_id),))

            load_products()

        def show_book():
            with sql.connect('library.db') as database:
                query = database.cursor()
                query.execute("SELECT * FROM books")
                datas = query.fetchall()

            inform = ''
            for data in datas:
                inform += str(data) + '\n'

            showinfo("Book Data", inform)

        self.__everytime__()

        self.staff_frame = Frame(self, background='#333333')
        ttk.Label(self, text='Library Management System', font=['Comic Sans MS', 16], background='#333333', foreground='white').pack(pady=20)
        ttk.Label(self.staff_frame, text=f"User: {self.NAME[0]}", font=['System', 14], background='#333333', foreground='white').grid(row=0, column=2,
                                                                                            sticky='news')
        label_style = {'font': ['Cambria', 10], 'background':'#333333', 'foreground': 'white'}
        labels, row = ['Book ID: ', 'Book Name: ', 'Book Author: ', 'Book Language: '], 1
        for label in labels:
            ttk.Label(self.staff_frame, text=label, **label_style).grid(row=row, column=0, sticky=W)
            row += 1

        self.book_id = ttk.Entry(self.staff_frame, width=60)
        self.book_name = ttk.Entry(self.staff_frame, width=60)
        self.book_author = ttk.Entry(self.staff_frame, width=60)
        self.book_language = ttk.Entry(self.staff_frame, width=60)

        entries = [self.book_id, self.book_name, self.book_author, self.book_language]
        for row, entry in enumerate(entries, start=1):
            entry.grid(row=row, column=1, columnspan=7, pady=10)

        Button(self.staff_frame, text="Add Book", command=add_book, background='#333333', foreground='white').grid(row=5, column=0)
        Button(self.staff_frame, text="Edit Book detail", command=edit_book, background='#333333', foreground='white').grid(row=5, column=1)
        Button(self.staff_frame, text="Delete Book", command=delete_book, background='#333333', foreground='white').grid(row=5, column=2)
        Button(self.staff_frame, text="Show Books", command=show_book, background='#333333', foreground='white').grid(row=5, column=3)

        self.book_list = Listbox(self.staff_frame, width=80, height=10)
        self.book_list.grid(row=6, column=0, columnspan=5, pady=10, padx=20)

        load_products()
        self.staff_frame.pack(expand=TRUE, fill=BOTH, padx=95, pady=5)


if __name__ == "__main__":
    Library_Management_system = App()
