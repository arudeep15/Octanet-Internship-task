import tkinter as tk
from tkinter import messagebox

# Simple in-memory data structure for user accounts
accounts = {
    'user1': {'pin': '1234', 'balance': 1000},
    'user2': {'pin': '5678', 'balance': 500}
}

# Global variables for current user and balance
current_user = None
current_balance = 0

def authenticate():
    global current_user, current_balance
    username = username_entry.get()
    pin = pin_entry.get()
    
    if username in accounts and accounts[username]['pin'] == pin:
        current_user = username
        current_balance = accounts[username]['balance']
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        show_main_screen()
    else:
        messagebox.showerror("Login Failed", "Invalid username or PIN")


def show_main_screen():
    login_frame.pack_forget()
    main_frame.pack()

def view_balance():
    balance_label.config(text="Current Balance: $" + str(current_balance))

def deposit_money():
    global current_balance
    amount = deposit_entry.get()
    if amount.isdigit():
        current_balance += int(amount)
        accounts[current_user]['balance'] = current_balance
        messagebox.showinfo("Deposit Successful", "Deposited: $" + amount)
        deposit_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid amount")

def withdraw_money():
    global current_balance
    amount = withdraw_entry.get()
    if amount.isdigit():
        amount = int(amount)
        if amount <= current_balance:
            current_balance -= amount
            accounts[current_user]['balance'] = current_balance
            messagebox.showinfo("Withdrawal Successful", "Withdrew: $" + str(amount))
            withdraw_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Insufficient Funds", "Not enough balance")
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid amount")

def logout():
    main_frame.pack_forget()
    login_frame.pack()

# Setup main window
window = tk.Tk()
window.title("ATM Interface")
window.geometry("300x400")

# Login Frame
login_frame = tk.Frame(window)
login_frame.pack(pady=20)

tk.Label(login_frame, text="ATM Login", font=("Arial", 16)).pack(pady=10)
tk.Label(login_frame, text="Username:").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack(pady=5)
tk.Label(login_frame, text="PIN:").pack()
pin_entry = tk.Entry(login_frame, show="*")
pin_entry.pack(pady=5)
tk.Button(login_frame, text="Login", command=authenticate).pack(pady=10)

# Main Frame
main_frame = tk.Frame(window)

tk.Label(main_frame, text="ATM Main Screen", font=("Arial", 16)).pack(pady=10)
balance_label = tk.Label(main_frame, text="Current Balance: $0")
balance_label.pack(pady=10)

tk.Button(main_frame, text="View Balance", command=view_balance).pack(pady=5)

tk.Label(main_frame, text="Deposit Amount:").pack(pady=5)
deposit_entry = tk.Entry(main_frame)
deposit_entry.pack(pady=5)
tk.Button(main_frame, text="Deposit", command=deposit_money).pack(pady=5)

tk.Label(main_frame, text="Withdraw Amount:").pack(pady=5)
withdraw_entry = tk.Entry(main_frame)
withdraw_entry.pack(pady=5)
tk.Button(main_frame, text="Withdraw", command=withdraw_money).pack(pady=5)

tk.Button(main_frame, text="Logout", command=logout).pack(pady=20)

# Start the application
window.mainloop()
