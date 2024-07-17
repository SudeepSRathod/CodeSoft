import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("800x600")  # Adjusted window size
        self.root.resizable(False, False)
        self.contacts = {}

        # Set background color and create a frame for the contact list
        self.root.configure(bg="#ffccbc")  # Light orange background color
        self.frame_list = tk.Frame(self.root, padx=10, pady=10, bg="#ffe0b2")  # Lighter orange background for the frame
        self.frame_list.pack(fill=tk.BOTH, expand=True)

        # Contact List Header
        self.header = tk.Label(self.frame_list, text="Contact List", font=("Arial", 24, "bold"), bg="#ffe0b2", fg="#bf360c")  # Simple and modern font
        self.header.pack(pady=10)

        # Contact List
        self.tree = ttk.Treeview(self.frame_list, columns=("Name", "Phone"), show="headings", height=18)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Scrollbars
        self.v_scroll = tk.Scrollbar(self.frame_list, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.v_scroll.set)
        self.v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.h_scroll = tk.Scrollbar(self.frame_list, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.h_scroll.set)
        self.h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        # Buttons
        self.button_frame = tk.Frame(self.root, padx=10, pady=10, bg="#ffe0b2")
        self.button_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=10)

        # Grid layout for buttons
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=1)

        # 3D effect with relief and padding
        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact, width=20, height=2, font=("Segoe UI", 12, "bold"), bg="#ff8a65", fg="white", relief=tk.RAISED, bd=3, highlightbackground="#ff8a65", highlightcolor="#ff8a65")
        self.add_button.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.update_button = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact, width=20, height=2, font=("Segoe UI", 12, "bold"), bg="#ff7043", fg="white", relief=tk.RAISED, bd=3, highlightbackground="#ff7043", highlightcolor="#ff7043")
        self.update_button.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact, width=20, height=2, font=("Segoe UI", 12, "bold"), bg="#f44336", fg="white", relief=tk.RAISED, bd=3, highlightbackground="#f44336", highlightcolor="#f44336")
        self.delete_button.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        self.search_button = tk.Button(self.button_frame, text="Search Contact", command=self.search_contact, width=20, height=2, font=("Segoe UI", 12, "bold"), bg="#ffab91", fg="white", relief=tk.RAISED, bd=3, highlightbackground="#ffab91", highlightcolor="#ffab91")
        self.search_button.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

        # Load initial contacts (if any)
        self.load_contacts()

    def load_contacts(self):
        self.tree.delete(*self.tree.get_children())
        for name, phone in self.contacts.items():
            self.tree.insert("", tk.END, values=(name, phone))

    def add_contact(self):
        name = simpledialog.askstring("Add Contact", "Enter contact name:", parent=self.root)
        if name:
            phone = simpledialog.askstring("Add Contact", "Enter contact phone number (10 digits):", parent=self.root)
            if phone and len(phone) == 10 and phone.isdigit():
                if name in self.contacts:
                    messagebox.showerror("Error", "Contact already exists!")
                else:
                    self.contacts[name] = phone
                    self.load_contacts()
            else:
                messagebox.showerror("Error", "Phone number must be 10 digits.")

    def update_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            old_name, old_phone = self.tree.item(selected_item)["values"]
            new_name = simpledialog.askstring("Update Contact", "Enter new contact name:", initialvalue=old_name, parent=self.root)
            if new_name:
                new_phone = simpledialog.askstring("Update Contact", "Enter new contact phone number (10 digits):", initialvalue=old_phone, parent=self.root)
                if new_phone and len(new_phone) == 10 and new_phone.isdigit():
                    del self.contacts[old_name]
                    self.contacts[new_name] = new_phone
                    self.load_contacts()
                else:
                    messagebox.showerror("Error", "Phone number must be 10 digits.")
        else:
            messagebox.showerror("Error", "Select a contact to update!")

    def delete_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            name, _ = self.tree.item(selected_item)["values"]
            del self.contacts[name]
            self.load_contacts()
        else:
            messagebox.showerror("Error", "Select a contact to delete!")

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter contact name or phone number:", parent=self.root)
        if search_term:
            found = False
            for item in self.tree.get_children():
                name, phone = self.tree.item(item)["values"]
                if search_term.lower() in name.lower() or search_term in str(phone):
                    self.tree.selection_set(item)
                    self.tree.see(item)
                    found = True
                    break
            if not found:
                messagebox.showinfo("Search Result", "No contact found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
