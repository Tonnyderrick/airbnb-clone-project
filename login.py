import tkinter as tk
from tkinter import messagebox

# Sample User Credentials (Ideally, use a database)
VALID_CREDENTIALS = {
    "admin": "password123",  # Replace with hashed passwords in real apps
    "user1": "pass123"
}

def login():
    userid = entry_user.get()
    password = entry_pass.get()
    
    if userid in VALID_CREDENTIALS and VALID_CREDENTIALS[userid] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {userid}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# GUI Setup
root = tk.Tk()
root.title("Login System")

tk.Label(root, text="Username:").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password:").pack()
entry_pass = tk.Entry(root, show="*")  # Hide password input
entry_pass.pack()

tk.Button(root, text="Login", command=login).pack()

root.mainloop()
