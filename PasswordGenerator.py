import tkinter as tk
from tkinter import ttk
import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def on_generate_clicked():
    length = 0
    if var_six.get():
        length = 6
    elif var_ten.get():
        length = 10
    elif var_twelve.get():
        length = 12
    password = generate_password(length)
    entry_password.delete(0, tk.END)  # Remove any existing content in the entry
    entry_password.insert(0, password)  # Insert the generated password

# Main window
root = tk.Tk()
root.title("Password Generator")


frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))


entry_password = ttk.Entry(frame, width=40)
entry_password.grid(row=0, column=1, pady=5)


var_six = tk.BooleanVar()
var_ten = tk.BooleanVar()
var_twelve = tk.BooleanVar()

checkbox_six = ttk.Checkbutton(frame, text="6 characters password", variable=var_six)
checkbox_six.grid(row=1, column=1, sticky=tk.W, pady=2)

checkbox_ten = ttk.Checkbutton(frame, text="10 characters password", variable=var_ten)
checkbox_ten.grid(row=2, column=1, sticky=tk.W, pady=2)

checkbox_twelve = ttk.Checkbutton(frame, text="12 characters password", variable=var_twelve)
checkbox_twelve.grid(row=3, column=1, sticky=tk.W, pady=2)
# Button to generate the password
button_generate = ttk.Button(frame, text="Generate", command=on_generate_clicked)
button_generate.grid(row=4, column=1, pady=5)

# Start the Tkinter event loop
root.mainloop()
