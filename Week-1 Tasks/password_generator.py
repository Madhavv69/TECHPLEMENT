import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=8, include_uppercase=True, include_lowercase=True, include_digits=True, include_special=True):
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    character_pool = ""
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_digits:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("No character types selected. Please include at least one type of character.")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def generate():
    try:
        length = int(length_var.get())
        include_uppercase = uppercase_var.get()
        include_lowercase = lowercase_var.get()
        include_digits = digits_var.get()
        include_special = special_var.get()

        print(f"Generating password with length {length}, uppercase: {include_uppercase}, lowercase: {include_lowercase}, digits: {include_digits}, special: {include_special}")  # Debugging statement

        password = generate_password(
            length=length,
            include_uppercase=include_uppercase,
            include_lowercase=include_lowercase,
            include_digits=include_digits,
            include_special=include_special
        )

        print(f"Generated password: {password}")  # Debugging statement

        result_var.set(password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")  # Set the size of the main window

# Variables for the options
length_var = tk.StringVar(value="8")
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)
result_var = tk.StringVar()

# Create and place widgets with padding for better spacing
tk.Label(root, text="Password Length:").grid(row=0, column=0, sticky="e", padx=10, pady=10)
tk.Entry(root, textvariable=length_var).grid(row=0, column=1, padx=10, pady=10)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).grid(row=1, columnspan=2, sticky="w", padx=10, pady=5)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var).grid(row=2, columnspan=2, sticky="w", padx=10, pady=5)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=3, columnspan=2, sticky="w", padx=10, pady=5)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=4, columnspan=2, sticky="w", padx=10, pady=5)

tk.Button(root, text="Generate Password", command=generate).grid(row=5, columnspan=2, padx=10, pady=20)
tk.Entry(root, textvariable=result_var, state="readonly", width=50).grid(row=6, columnspan=2, sticky="we", padx=10, pady=10)

# Start the main loop
root.mainloop()
