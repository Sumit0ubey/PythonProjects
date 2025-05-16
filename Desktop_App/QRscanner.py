from tkinter import *
from tkinter import ttk, filedialog
from tkinter.messagebox import showinfo, showerror, showwarning
from PIL import Image, ImageTk
from qrcode import make
from re import match
from subprocess import check_call
from importlib.util import find_spec
from sys import executable

needed_library = ['PIL', 'qrcode']
for library in needed_library:
    if find_spec(library) is None:
        print(f'{library} not Found. \n installing.....')
        check_call([executable, '-m', 'pip', 'install', library])
    else:
        pass


def type_selected(event):
    qr = chosen_type.get()
    for widget in body.winfo_children():
        widget.destroy()

    if qr == "Phone No QR Maker":
        ttk.Label(body, text='Phone Number: ').grid(row=0, column=0, sticky=W, padx=5)
        phone_number_entry = ttk.Entry(body)
        phone_number_entry.grid(row=0, column=1, sticky=W, padx=5)
        Button(body, text="Generate QR", command=lambda: generate_qr(phone_number_entry.get()), bg='#333333', fg='white').grid(row=0, column=2, sticky=W)
    elif qr == "Email QR Maker":
        ttk.Label(body, text='Email: ').grid(row=0, column=0, sticky=W, padx=5)
        email_entry = ttk.Entry(body)
        email_entry.grid(row=0, column=1, sticky=W, padx=5)
        Button(body, text="Generate QR", command=lambda: generate_qr(email_entry.get()), bg='#333333', fg='white').grid(row=0, column=2, sticky=W)
    elif qr == "Image QR Maker":
        ttk.Label(body, text='Image URL: ').grid(row=0, column=0, sticky=W, padx=5)
        image_url_entry = ttk.Entry(body)
        image_url_entry.grid(row=0, column=1, sticky=W, padx=5)
        Button(body, text="Generate QR", command=lambda: generate_qr(image_url_entry.get()), bg='#333333', fg='white').grid(row=0, column=2, sticky=W)
    elif qr == "UPI QR Maker":
        ttk.Label(body, text='UPI ID: ').grid(row=0, column=0, sticky=W, padx=5)
        upi_id_entry = ttk.Entry(body)
        upi_id_entry.grid(row=0, column=1, sticky=W, padx=5)
        Button(body, text="Generate QR", command=lambda: generate_qr(upi_id_entry.get()), bg='#333333', fg='white').grid(row=0, column=2, sticky=W)
    elif qr == "URL QR Maker":
        ttk.Label(body, text='URL: ').grid(row=0, column=0, sticky=W, padx=5)
        url_entry = ttk.Entry(body)
        url_entry.grid(row=0, column=1, sticky=W, padx=5)
        Button(body, text="Generate QR", command=lambda: generate_qr(url_entry.get()), bg='#333333', fg='white').grid(row=0, column=2, sticky=W)
    else:
        ttk.Label(body, text='Invalid Option').pack()


def generate_qr(data):
    if not data:
        showerror("Error", "No data provided!")
        return

    qr_type = chosen_type.get()

    if qr_type == "Phone No QR Maker":
        pattern = r'^(0|91)?[6-9][0-9]{9}$'
        if not match(pattern, data):
            showwarning("Invalid", "Enter a valid phone number")
            return
    elif qr_type == "Email QR Maker":
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        if not match(pattern, data):
            showwarning("Invalid", "Enter a valid email address")
            return
    elif qr_type == "UPI QR Maker":
        pattern = r'^[A-Za-z0-9.-]+@[a-zA-Z0-9]{3,64}$'
        if not match(pattern, data):
            showwarning("Invalid", "Enter a valid UPI ID")
            return
        #  upi://pay?pa=URL_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE
        data = f'upi://pay?pa={data}&pn=Recipient%20Name'
    elif qr_type == "URL QR Maker":
        pattern = r'^(http|https):\/\/[^\s$.?#].[^\s]*$'
        if not match(pattern, data):
            showwarning("Invalid", "Enter a valid URL")
            return

    qr_code = make(data)

    qr_image = qr_code.get_image()
    qr_image = qr_image.resize((200, 200), Image.LANCZOS)
    qr_photo = ImageTk.PhotoImage(qr_image)

    for widget in body.winfo_children():
        widget.destroy()

    qr_label = Label(body, image=qr_photo, bg='#333333')
    qr_label.image = qr_photo
    qr_label.pack(pady=10)

    for widget in footer.winfo_children():
        widget.destroy()

    Button(footer, text='Save', command=lambda: save_qr(qr_code), bg='#333333', fg='white').pack(anchor=CENTER,
                                                                                                 expand=TRUE, ipadx=10,
                                                                                                 ipady=5)
    showinfo("Success", "QR Code generated successfully!")


def save_qr(qr_code):
    file_path = filedialog.asksaveasfilename(
        defaultextension='.png',
        filetypes=[('PNG files', '*.png'), ('All files', '*.*')],
        title="Save QR Code As"
    )
    if file_path:
        qr_code.save(file_path)
        showinfo("Saved", f"QR Code saved at {file_path}")


window = Tk()
window.title('QR Maker | Project 6')
window.geometry(f'{600}x{450}+'
                f'{int(window.winfo_screenwidth() / 2 - 600 / 2)}+'
                f'{int(window.winfo_screenheight() / 2 - 450 / 2)}')
window.configure(bg='#333333')
window.resizable(False, False)
style = ttk.Style(window)
style.configure(style)
style.configure(style='TLabel', background='#333333', foreground='white', font=['Bell MT', 14])

header = Frame(window, bg='#333333')

ttk.Label(window, text="QR Maker App", font=['Kristen ITC', 16]).pack(pady=10)
ttk.Label(header, text='Choose Type: ').grid(row=0, column=0, sticky=W)

chosen_type = StringVar()
types = ['Phone No QR Maker', 'Email QR Maker', 'Image QR Maker', 'UPI QR Maker', 'URL QR Maker', '']
qr_type = ttk.Combobox(header, textvariable=chosen_type, values=types, state='readonly', width=60)
qr_type.grid(row=0, column=1, columnspan=8, sticky=W)
qr_type.bind('<<ComboboxSelected>>', type_selected)

header.pack(side=TOP, anchor=NW, fill=X, padx=50, pady=10)

body = Frame(window, bg='#333333')
ttk.Label(body, text="None Is Selected").pack()
body.pack(expand=TRUE, fill=BOTH, padx=120, pady=20)

footer = Frame(window, bg='#333333')
footer.pack(side=BOTTOM, anchor=CENTER, fill=X, pady=10)

window.mainloop()
