from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, showwarning
from tkinter.filedialog import askopenfilename
from PIL import Image
from reportlab.pdfgen import canvas
import os


class App(Tk):
    def __init__(self):
        self.font_title = ['Helvetica', 20, 'bold']
        self.font_label = ['Helvetica', 12]
        self.font_button = ['Helvetica', 12, 'bold']
        self.background_color = '#f2f2f2'

        super().__init__()
        self.title('Resume Builder | Project 11')

        Label(self, text=' Resume Builder ', font=['Comic Sans MS', 14, 'bold']).pack(pady=10)
        self.form = Frame(self)
        self.create_form()
        self.form.pack(side=LEFT, anchor=NW, expand=TRUE, fill=BOTH, padx=40, pady=15)

        self.resizable(False, False)

    def submit_form(self):
        name = self.name_entry.get().strip()
        number = self.number_entry.get().strip()
        email = self.email_entry.get().strip()
        qualification = self.qualification_entry.get().strip()
        skills = self.skills_entry.get("1.0", END).strip()

        if not name or not number or not email or not qualification or not skills:
            showwarning(title='Invalid', message='Please fill all the fields')
            return

        showinfo(title='Instructions', message='Follow this step: \n Step 1: Select Profile Photo \n Step 2: Resume '
                                               'will be built automatically')

        filename = askopenfilename(defaultextension='.png', filetypes=[("Image file", '*.jpg *.jpeg *.png')])
        if not filename:
            showerror(title='Invalid', message='Please select photo')
            return

        pdf_filename = 'Resume.pdf'
        try:
            self.generate_resume_pdf(pdf_filename, name, number, email, qualification, skills, filename)
            showinfo(title='Created Resume', message=f"Resume created Successfully. \n PDF saved as {pdf_filename}")
        except Exception as e:
            showerror(title='Error', message=f"Failed to create resume: {e}")

        self.form.after(1000, self.clear())

    def generate_resume_pdf(self, filename, name, number, email, qualification, skills, photo_filename):
        c = canvas.Canvas(filename)
        c.setFont(self.font_title[0], self.font_title[1])
        c.drawString(50, 750, f'Name: {name}')
        c.drawString(50, 720, f'Number: {number}')
        c.drawString(50, 690, f'Email: {email}')
        c.drawString(50, 660, f'Qualification: {qualification}')
        c.drawString(50, 630, f'Skills:')
        c.setFont(self.font_label[0], self.font_label[1] - 2)
        c.drawString(60, 610, skills)

        photo = Image.open(photo_filename)
        photo.thumbnail((200, 200))
        thumbnail_path = 'thumbnail.jpg'
        photo.save(thumbnail_path)

        c.drawImage(thumbnail_path, 400, 650, 100, 100)

        c.showPage()
        c.save()

        if os.path.exists(thumbnail_path):
            os.remove(thumbnail_path)

    def create_form(self):
        label_style = {'font': ['Calisto MT', 12]}
        label_list = ['Full Name: ', 'Phone Number: ', 'Email Address: ', 'Qualification: ', 'Skills: ']
        entry_list = []

        for row, label in enumerate(label_list):
            ttk.Label(self.form, text=label, **label_style).grid(row=row, column=0, sticky=W)
            if label == 'Skills: ':
                text_widget = Text(self.form, width=50, height=4)
                text_widget.grid(row=row, column=1, pady=5, sticky=W)
                self.skills_entry = text_widget
            else:
                entry_widget = ttk.Entry(self.form, width=60)
                entry_widget.grid(row=row, column=1, pady=5, sticky=W)
                entry_list.append(entry_widget)

        self.name_entry, self.number_entry, self.email_entry, self.qualification_entry = entry_list

        ttk.Button(self.form, text='Browse / Build Resume', command=self.submit_form).grid(row=len(label_list), column=1, pady=5)
        ttk.Button(self.form, text='Clear', command=self.clear).grid(row=len(label_list), column=0)

    def clear(self):
        self.name_entry.delete(0, END)
        self.number_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.qualification_entry.delete(0, END)
        self.skills_entry.delete(0, END)


if __name__ == "__main__":
    app = App()
    app.mainloop()
