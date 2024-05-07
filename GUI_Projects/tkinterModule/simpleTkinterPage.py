import tkinter as tk

def configure_widget(widget):
    widget.config(bg="red", font=("Times", 18))

root = tk.Tk()
root.title("Widget Configuration Example")

label = tk.Label(root, text="Hello, World!")

configure_widget(label)

label.pack(padx=20, pady=20)

root.mainloop()
