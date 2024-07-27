from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, showwarning

"""
Writing a function for validating the user inputs and checking the correctness of the data
"""


def Confirmation():
    if f_name.get() == "" or l_name.get() == "" or email.get() == "" or phone.get() == "" or degree.get() == "" or gender.get() == "" or stream.get() == "":
        showerror(title="Fill All", message="All the fields are required")
    else:
        from re import match
        email_valid = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}$'
        phone_valid = r'^(0|91)?[6-9][0-9]{9}$'
        if match(email_valid, email.get()) and match(phone_valid, phone.get()):
            showinfo(title="Confirmation",
                     message=f" You Filled: \n Name: {f_name.get()}  {l_name.get()} \n Stream : {stream.get()}, Degree: {degree.get()} \n Email: {email.get()} \n Phone No: {phone.get()}")
            Window.quit()
        else:
            showwarning(title="Invalid Entry", message="Email or Phone Number is not valid")


Window = Tk()
Window.title('Registration Form | Project 3')
Window.geometry('800x600')
Window.resizable(False, False)
Window.configure(bg='#333333')

ttk.Label(text='Student Registration', font=['Comic Sans MS', 30]).pack(pady=10)  # Creating a title for the form

"""
Declaring a variable to store the user inputs from various widgets 
"""

f_name = StringVar()
l_name = StringVar()
gender = StringVar()
stream = StringVar()
degree = StringVar()
email = StringVar()
phone = StringVar()

frame = Frame(Window, bg='#333333')

"""
Using Style method of ttk to style the multiple same widgets in one-Go
"""

style = ttk.Style(frame)
style.configure(style='TLabel', background='#333333', foreground='#ffffff', font=['Arial', 16])
style.configure(style='TRadiobutton', background='#333333', foreground='#ffffff', font=['Bookman Old Style', 14])
style.configure(style='TCheckbutton', background='#333333', foreground='#ffffff', font=['Bookman Old Style', 14])
style.configure(style='TCombobox', background='#ffffff')

"""
Creating and Placing the widgets in the frame using grid
"""

ttk.Label(frame, text='First Name : ').grid(row=0, column=0, sticky=W, padx=10, pady=10)
ttk.Entry(frame, textvariable=f_name, width=80, font=['Arial', 12]).grid(row=0, column=1, sticky=W, columnspan=12)

ttk.Label(frame, text='Surname : ').grid(row=1, column=0, sticky=W, padx=10, pady=10)
ttk.Entry(frame, textvariable=l_name, width=80, font=['Arial', 12]).grid(row=1, column=1, sticky=W, columnspan=12)

ttk.Label(frame, text='Gender : ').grid(row=2, column=0, padx=10, pady=10, sticky=W)
ttk.Radiobutton(frame, text='Male', value='M', variable=gender).grid(row=2, column=1, sticky=W)
ttk.Radiobutton(frame, text='Female', value='F', variable=gender).grid(row=2, column=2, sticky=W)

ttk.Label(frame, text='Stream : ').grid(row=3, column=0, padx=10, pady=10, sticky=W)
ttk.Checkbutton(frame, text='Sci', onvalue='Science', variable=stream).grid(row=3, column=1, sticky=W)
ttk.Checkbutton(frame, text='Art', onvalue='Art', variable=stream).grid(row=3, column=2, sticky=W)
ttk.Checkbutton(frame, text='Commerce', onvalue='Commerce', variable=stream).grid(row=3, column=3, sticky=W)

ttk.Label(frame, text='Degree : ').grid(row=4, column=0, sticky=W, padx=10, pady=10)
courses = ['B tech', 'BSC', 'CS', 'IT', 'BCOM', 'BMS', 'BAF', 'MSC IT/CS', 'M tech']
ttk.Combobox(frame, textvariable=degree, values=courses, state='readonly', width=60).grid(row=4, column=1, columnspan=8,
                                                                                          sticky=W)

ttk.Label(frame, text='Email : ').grid(row=5, column=0, sticky=W, padx=10, pady=10)
ttk.Entry(frame, textvariable=email, width=80, font=['Arial', 12]).grid(row=5, column=1, columnspan=12, sticky=W)

ttk.Label(frame, text='PhoneNo : ').grid(row=6, column=0, sticky=W, padx=10, pady=10)
ttk.Entry(frame, textvariable=phone, width=80, font=['Arial', 12]).grid(row=6, column=1, columnspan=12, sticky=W)

frame.pack(expand=TRUE, fill=BOTH, padx=80, pady=40)

#  Button to check whether the entered data is valid or not using function that is declared above
Button(text="Submit", command=Confirmation, background='black', foreground='#ffffff').pack(expand=TRUE, pady=20,
                                                                                           ipadx=20, ipady=10,
                                                                                           anchor=CENTER, side=BOTTOM)

Window.mainloop()
