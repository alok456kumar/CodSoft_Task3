# Creating a password generator application using python
import random
import pyperclip
from tkinter import *
from tkinter.ttk import Combobox  # Import Combobox specifically from ttk

def low():
    entry.delete(0, END)
    length = var1.get()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password
    elif var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    else:
        print("Please choose an option")

def generate():
    password1 = low()
    entry.delete(0, END)
    entry.insert(0, password1)

def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)

root = Tk()
root.title(" Password Generator")
root.configure(bg="#f0f0f0")  # Set background color

# Create a frame to hold the widgets
frame = Frame(root, bg="#f0f0f0")  # Set background color for the frame
frame.pack(padx=10, pady=10)

# Set custom font style and size
custom_font = ("Arial", 12)

Random_password = Label(frame, text="Password:", font=custom_font, bg="#f0f0f0")  
Random_password.grid(row=0, column=0, padx=5, pady=5)
entry = Entry(frame, width=30, font=custom_font)  # Set custom font for the entry widget
entry.grid(row=0, column=1, padx=5, pady=5)

copy_button = Button(frame, text="Copy to Clipboard", command=copy1, font=custom_font)  
copy_button.grid(row=0, column=2, padx=5, pady=5)

generate_button = Button(frame, text="Generate Password", command=generate, font=custom_font, bg="#4CAF50", fg="white") 
generate_button.grid(row=1, column=0, columnspan=3, padx=5, pady=10)

# Radio Buttons for deciding the strength of password
var = IntVar()
radio_low = Radiobutton(frame, text="Low", variable=var, value=1, font=custom_font, bg="#f0f0f0")  
radio_low.grid(row=2, column=0, padx=5, pady=5)

radio_medium = Radiobutton(frame, text="Medium", variable=var, value=0, font=custom_font, bg="#f0f0f0")  
radio_medium.grid(row=2, column=1, padx=5, pady=5)

radio_strong = Radiobutton(frame, text="Strong", variable=var, value=3, font=custom_font, bg="#f0f0f0")  
radio_strong.grid(row=2, column=2, padx=5, pady=5)

# Combo Box for length of your password
var1 = IntVar()
combo = Combobox(frame, textvariable=var1, width=10, font=custom_font)  
combo['values'] = tuple(range(8, 33))
combo.current(0)
combo.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
