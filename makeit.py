import tkinter as tk
from tkinter import messagebox


class ATMApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.balance = 50000.0  # Initial Balance

        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        """Configure main GUI window."""
        self.root.title("ATM System")
        self.root.geometry("350x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")

    def create_widgets(self):
        """Build visual components: title, balance label, entry box, and buttons."""
        # Title Header
        title = tk.Label(
            self.root,
            text="===== ATM =====",
            font=("Arial", 18, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        title.pack(pady=15)

        # Balance Display
        self.balance_label = tk.Label(
            self.root,
            text=f"Available Balance: ₦{self.balance:,.2f}",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="#2ecc71"
        )
        self.balance_label.pack(pady=10)

        # Input Entry Box
        self.amount_entry = tk.Entry(
            self.root,
            font=("Arial", 14),
            justify="center"
        )
        self.amount_entry.pack(pady=10, ipady=5)
        self.amount_entry.insert(0, "Enter Amount Here")

        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#2C378A")
        btn_frame.pack(pady=20)

        tk.Button(
            btn_frame, text="Deposit", font=("Arial", 11, "bold"),
            bg="#27ae60", fg="white", width=12, command=self.deposit
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            btn_frame, text="Withdraw", font=("Arial", 11, "bold"),
            bg="#e67e22", fg="white", width=12, command=self.withdraw
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            self.root, text="Exit ATM", font=("Arial", 11, "bold"),
            bg="#e74c3c", fg="white", width=26, command=self.root.quit
        ).pack(pady=10)

    # --- ATM Business Logic Methods ---

    def get_amount_input(self) -> float | None:
        """Helper to retrieve and validate numerical input from entry box."""
        try:
            return float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror(
                "Error", "Please enter a valid numeric amount.")
            return None

    def deposit(self):
        """Handle deposit action."""
        amount = self.get_amount_input()
        if amount is None:
            return

        if amount < 1000:
            messagebox.showwarning(
                "Deposit Failed", "Invalid Amount. Amount must be ₦1,000 or more.")
        else:
            self.balance += amount
            self.update_balance_display()
            messagebox.showinfo(
                "Success", f"Successfully deposited ₦{amount:,.2f}")

    def withdraw(self):
        """Handle withdrawal action."""
        amount = self.get_amount_input()
        if amount is None:
            return

        if amount <= 0:
            messagebox.showwarning("Withdrawal Failed", "Invalid Amount.")
        elif amount > self.balance:
            messagebox.showerror("Withdrawal Failed", "Insufficient funds!")
        else:
            self.balance -= amount
            self.update_balance_display()
            messagebox.showinfo(
                "Success", f"Successfully withdrew ₦{amount:,.2f}")

    def update_balance_display(self):
        """Update the on-screen balance label and clear entry input."""
        self.balance_label.config(
            text=f"Available Balance: ₦{self.balance:,.2f}")
        self.amount_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
