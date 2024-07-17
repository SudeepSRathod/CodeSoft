import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password
def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            raise ValueError("Length should be a positive number.")
        if length > 13:
            messagebox.showwarning("Warning", "Password length should not exceed 13 characters.")
            return
        all_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_characters) for _ in range(length))
        password_display.config(text=password)
    except ValueError as ve:
        messagebox.showerror("Invalid input", str(ve))

# Setting up the main window
root = tk.Tk()
root.title("🔑 Secure Password Generator")
root.geometry("600x300")
root.resizable(False, False)
root.config(bg="#f5f5f5")

# Title label
title_label = tk.Label(root, text="🔑 Secure Password Generator", font=("Comic Sans MS", 24, "bold"), fg="#ff6347", bg="#f5f5f5")
title_label.pack(pady=20)

# Frame for user input
input_frame = tk.Frame(root, bg="#add8e6", bd=2, relief="groove")
input_frame.pack(pady=20, padx=20, fill="x")

# Label and entry for password length
length_label = tk.Label(input_frame, text="Password Length:", font=("Comic Sans MS", 16), fg="#000000", bg="#add8e6")
length_label.grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(input_frame, width=5, font=("Comic Sans MS", 16))
entry.grid(row=0, column=1, padx=10, pady=10)

# Button to generate password
generate_button = tk.Button(input_frame, text="Generate", font=("Comic Sans MS", 16), bg="#ff6347", fg="#ffffff", command=generate_password)
generate_button.grid(row=0, column=2, padx=10, pady=10)

# Label to display generated password
password_display = tk.Label(root, text="", font=("Comic Sans MS", 18, "bold"), fg="#32cd32", bg="#f5f5f5")
password_display.pack(pady=20)

# Run the application
root.mainloop()
