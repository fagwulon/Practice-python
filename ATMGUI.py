import tkinter as tk
from tkinter import messagebox

# Global balance variable
balance = 50000.0


def update_balance_label():
    """Updates the text on screen to show the current balance."""
    balance_label.config(text=f"Available Balance: ₦{balance:,.2f}")


def check_balance():
    """Displays current balance in a popup window."""
    messagebox.showinfo("Balance", f"Available Balance: ₦{balance:,.2f}")


def deposit():
    """Handles deposit logic from the entry box."""
    global balance
    try:
        amount = float(amount_entry.get())
        if amount < 1000:
            messagebox.showwarning("Deposit Error", "Amount must be ₦1,000 or more.")
        else:
            balance += amount
            update_balance_label()
            messagebox.showinfo("Success", f"Successfully deposited ₦{amount:,.2f}")
            amount_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")


def withdraw():
    """Handles withdrawal logic from the entry box."""
    global balance
    try:
        amount = float(amount_entry.get())
        if amount <= 0:
            messagebox.showwarning("Withdrawal Error", "Invalid Amount.")
        elif amount > balance:
            messagebox.showerror("Withdrawal Error", "Insufficient funds!")
        else:
            balance -= amount
            update_balance_label()
            messagebox.showinfo("Success", f"Successfully withdrew ₦{amount:,.2f}")
            amount_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")


# --- GUI Setup ---

window = tk.Tk()
window.title("ATM Check")
window.geometry("350x380")
window.resizable(False, False)
window.configure(bg="#2c3e50")

# Title
title_label = tk.Label(
    window,
    text="===== ATM =====",
    font=("Arial", 18, "bold"),
    bg="#2c3e50",
    fg="#ecf0f1"
)
title_label.pack(pady=15)

# Balance Display
balance_label = tk.Label(
    window,
    text=f"Available Balance: ₦{balance:,.2f}",
    font=("Arial", 12),
    bg="#2c3e50",
    fg="#2ecc71"
)
balance_label.pack(pady=10)

# Entry for Amount Input
amount_entry = tk.Entry(window, font=("Arial", 14), justify="center")
amount_entry.pack(pady=10, ipady=5)

# Action Buttons
btn_frame = tk.Frame(window, bg="#2c3e50")
btn_frame.pack(pady=10)

check_btn = tk.Button(
    btn_frame, text="Check Balance", font=("Arial", 10, "bold"),
    bg="#3498db", fg="white", width=12, command=check_balance
)
check_btn.grid(row=0, column=0, padx=5, pady=5)

deposit_btn = tk.Button(
    btn_frame, text="Deposit", font=("Arial", 10, "bold"),
    bg="#27ae60", fg="white", width=12, command=deposit
)
deposit_btn.grid(row=0, column=1, padx=5, pady=5)

withdraw_btn = tk.Button(
    btn_frame, text="Withdraw", font=("Arial", 10, "bold"),
    bg="#e67e22", fg="white", width=12, command=withdraw
)
withdraw_btn.grid(row=1, column=0, columnspan=2, pady=5)

exit_btn = tk.Button(
    window, text="Exit ATM", font=("Arial", 10, "bold"),
    bg="#e74c3c", fg="white", width=26, command=window.quit
)
exit_btn.pack(pady=10)

# Run the window loop
window.mainloop()
