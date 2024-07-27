import os
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno, showinfo, showerror
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.font import Font


class App(Tk):
    def __init__(self):
        super().__init__()
        self.filename = None
        self.title('File Management System | Project 10')
        self.geometry(f'{600}x{400}+'
                      f'{int(self.winfo_screenwidth() / 2 - 600 / 2)}+'
                      f'{int(self.winfo_screenheight() / 2 - 400 / 2)}')
        self.configure(background='white')

        self.create_menu()
        self.text = Text(self, font=('Arial', 12))
        self.text.pack(fill=BOTH, expand=TRUE)
        self.size_change = ttk.Sizegrip(self)
        self.size_change.pack(side=BOTTOM, anchor=SE)

    def create_menu(self):
        def new_file():
            if self.text.get(1.0, END).strip():
                save_or_not = askyesno(title='Closing File', message='Do you want to save this file?')
                if save_or_not:
                    save_file()
            self.text.delete(1.0, END)
            self.filename = None

        def open_file():
            self.filename = askopenfilename(defaultextension='.txt',
                                            filetypes=[("Text file", '*.txt'), ("Python file", '*.py'),
                                                       ("All files", '*.*')])
            if self.filename:
                try:
                    with open(self.filename, 'r') as file:
                        content = file.read()
                    self.text.delete(1.0, END)
                    self.text.insert(1.0, content)
                    self.text.configure(state='normal')
                except Exception as e:
                    showerror(title='Error', message=f"An error occurred \n Error: {e}")

        def name_of_all_file():
            files = os.listdir()
            if not files:
                showinfo(title='No File', message='There is no file in the current directory!')
            else:
                self.text.delete(1.0, END)
                data = "Files in directory: \n"
                for file in files:
                    data += "\t - " + file + "\n"
                self.text.insert(1.0, data)
                self.text.configure(state='disabled')

        def save_file():
            if self.filename:
                try:
                    with open(self.filename, 'w') as file:
                        file.write(self.text.get(1.0, END))
                except Exception as e:
                    showerror(title='Error', message=f"An error occurred \n Error: {e}")
            else:
                save_file_as()

        def save_file_as():
            filename = asksaveasfilename(defaultextension='.txt',
                                         filetypes=[("Text file", '*.txt'), ("Python file", '*.py'),
                                                    ("All files", '*.*')])
            if filename:
                self.filename = filename
                try:
                    with open(self.filename, 'w') as file:
                        file.write(self.text.get(1.0, END))
                except Exception as e:
                    showerror(title='Error', message=f"An error occurred \n Error: {e}")

        def delete_file():
            filename = askopenfilename(defaultextension='.txt',
                                       filetypes=[("Text file", '*.txt'), ("Python file", '*.py'),
                                                  ("All files", '*.*')])
            if filename:
                try:
                    os.remove(filename)
                    showinfo(title='Deleted File', message=f'{filename} has been deleted successfully!')
                except FileNotFoundError:
                    showerror(title='Not Found', message='File not found')
                except Exception as e:
                    showerror(title='Error', message=f"An error occurred \n Error: {e}")

        def family_change(font_style):
            current_font = Font(font=self.text.cget("font"))
            current_font.config(family=font_style)
            self.text.configure(font=current_font)

        def size_change(font_size):
            current_font = Font(font=self.text.cget("font"))
            current_font.config(size=font_size)
            self.text.configure(font=current_font)

        def theme_change(color):
            if color == 'black':
                self.configure(bg='#333333')
                self.text.configure(background='#333333', foreground='white')
            elif color == 'sky':
                self.configure(bg='lightblue')
                self.text.configure(background='lightblue', foreground='black')
            else:
                self.configure(bg=color)
                self.text.configure(background=color, foreground='black')

        self.menu_bar = Menu(self)
        self.config(menu=self.menu_bar)

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='Home')
        self.file_menu.add_command(label='New', command=new_file)
        self.file_menu.add_command(label='Open', command=open_file)
        self.file_menu.add_command(label='Files', command=name_of_all_file)
        self.file_menu.add_command(label='Save', command=save_file)
        self.file_menu.add_command(label='Save as', command=save_file_as)
        self.file_menu.add_command(label='Delete', command=delete_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', command=self.quit)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)

        self.font_menu = Menu(self.menu_bar, tearoff=0)
        font_names = ['Arial', 'Comic Sans MS', 'HP Simplified Jpan', 'Informal Roman', 'Perpetua Titling MT']
        self.family_submenu = Menu(self.font_menu, tearoff=0)
        for font in font_names:
            self.family_submenu.add_command(label=font, command=lambda Font=font: family_change(Font))
        self.font_menu.add_cascade(label='Font Style', menu=self.family_submenu)

        font_sizes = [10, 14, 16, 20, 24]
        self.size_submenu = Menu(self.font_menu, tearoff=0)
        for size in font_sizes:
            self.size_submenu.add_command(label=str(size), command=lambda Size=size: size_change(Size))
        self.font_menu.add_cascade(label='Font Size', menu=self.size_submenu)

        self.menu_bar.add_cascade(label='Font', menu=self.font_menu)

        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label='About', command=lambda: showinfo(title='About',
                                                                           message="File Management App \n "
                                                                                   "Created by: Sumit Dubey"))

        self.setting_submenu = Menu(self.help_menu, tearoff=0)

        self.theme_submenu = Menu(self.setting_submenu, tearoff=0)
        self.theme_submenu.add_command(label='Dark', command=lambda: theme_change('black'))
        self.theme_submenu.add_command(label='Light', command=lambda: theme_change('white'))
        self.theme_submenu.add_command(label='Sky', command=lambda: theme_change('sky'))
        self.setting_submenu.add_cascade(label='Theme', menu=self.theme_submenu)

        self.setting_submenu.add_command(label='Rest')
        self.setting_submenu.add_command(label='Version', command=lambda: showinfo(title='Version', message='1.0910v'))
        self.help_menu.add_cascade(label='Setting', menu=self.setting_submenu)

        self.help_menu.add_command(label='Report', command=lambda: showinfo(title='Contact Administrator',
                                                                            message="No contact number... Too bad"))
        self.menu_bar.add_cascade(label='Help', menu=self.help_menu)


if __name__ == "__main__":
    app = App()
    app.mainloop()
