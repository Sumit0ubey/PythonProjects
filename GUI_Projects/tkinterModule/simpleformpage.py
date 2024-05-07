import tkinter as tk

def configure_widget(widget, **kwargs):
    widget.config(**kwargs)

root = tk.Tk()
root.title("Widget Experimentation")

message = tk.Message(root, text="This is a Message widget.", width=200)
configure_widget(message, bg="yellow", font=("Arial", 14))

button = tk.Button(root, text="Click me")
configure_widget(button, bg="green", fg="white", font=("Helvetica", 12))

entry = tk.Entry(root)
configure_widget(entry, bg="lightblue", font=("Courier", 12))

checkbutton = tk.Checkbutton(root, text="Check me")
configure_widget(checkbutton, bg="orange", font=("Verdana", 12))

radiobutton = tk.Radiobutton(root, text="Select me")
configure_widget(radiobutton, bg="purple", fg="white", font=("Times", 12))

scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
configure_widget(scale, bg="pink", font=("Arial", 12))

message.pack(pady=5)
button.pack(pady=5)
entry.pack(pady=5)
checkbutton.pack(pady=5)
radiobutton.pack(pady=5)
scale.pack(pady=5)

root.mainloop()
