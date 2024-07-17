import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def evaluate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("400x500")
root.config(bg="#2d2d2d")  # Dark grey background

entry = tk.Entry(root, width=20, font=('Arial', 20), justify=tk.RIGHT, bd=10, bg="#e0f7fa")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=20)

# Custom button function to simulate 3D and pop-up style
def create_button(text, command):
    button = tk.Button(
        root, text=text, font=('Arial', 16), command=command,
        bg="#000000", fg="#ffffff", activebackground="#3d3d3d", activeforeground="#ffffff",
        relief='raised', bd=5, padx=10, pady=5
    )
    return button

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    create_button(text, lambda t=text: button_click(t) if t != '=' else evaluate()).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

create_button('C', clear_entry).grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
create_button('⌫', backspace).grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Main loop
root.mainloop()
