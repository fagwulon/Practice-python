import tkinter as tk


class Calculator:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.setup_window()
        self.create_widgets()
        self.bind_keyboard()  # Bind keyboard inputs

    def setup_window(self):
        """Configure main window parameters and grid weights."""
        self.root.title("OOP Calculator")
        self.root.geometry("320x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#2d2d2d")

        for i in range(6):
            self.root.rowconfigure(i, weight=1)
        for j in range(4):
            self.root.columnconfigure(j, weight=1)

    def create_widgets(self):
        """Create and place the display screen and operation buttons."""
        self.entry = tk.Entry(
            self.root,
            font=("Arial", 20),
            bg="#1e1e1e",
            fg="#ffffff",
            bd=0,
            justify="right",
            insertbackground="white"
        )
        self.entry.grid(
            row=0, column=0, columnspan=4,
            ipadx=8, ipady=15, padx=10, pady=15, sticky="nsew"
        )

        buttons = [
            ('C', 1, 0), ('/', 1, 1), ('*', 1, 2), ('-', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('=', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('.', 4, 3),
            ('0', 5, 0)
        ]

        for text, row, col in buttons:
            self.create_button(text, row, col)

    def create_button(self, text: str, row: int, col: int):
        """Helper method to instantiate individual buttons."""
        if text == 'C':
            cmd = self.clear_screen
            bg_color = "#e74c3c"
        elif text == '=':
            cmd = self.calculate_result
            bg_color = "#2ecc71"
        else:
            cmd = lambda val=text: self.handle_click(val)
            bg_color = "#3a3a3a" if text.isdigit() or text == '.' else "#f39c12"

        colspan = 2 if text == '0' else 1

        btn = tk.Button(
            self.root,
            text=text,
            font=("Arial", 14, "bold"),
            bg=bg_color,
            fg="#ffffff",
            bd=0,
            activebackground="#555555",
            activeforeground="#ffffff",
            command=cmd
        )
        btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=3, pady=3)

    def bind_keyboard(self):
        """Bind keyboard presses to calculator functions."""
        # Catches all standard character presses (0-9, +, -, *, /, .)
        self.root.bind("<Key>", self.handle_key_press)

        # Action keys
        self.root.bind("<Return>", lambda event: self.calculate_result())
        self.root.bind("<KP_Enter>", lambda event: self.calculate_result())  # Numpad Enter
        self.root.bind("<BackSpace>", lambda event: self.handle_backspace())
        self.root.bind("<Escape>", lambda event: self.clear_screen())

    # --- Instance Methods for Logic ---

    def handle_click(self, value: str):
        """Append clicked button value to entry display."""
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current_text + str(value))

    def handle_key_press(self, event: tk.Event):
        """Process character key presses from the keyboard."""
        valid_chars = "0123456789.+-*/"
        if event.char in valid_chars and event.char != "":
            self.handle_click(event.char)

    def handle_backspace(self):
        """Delete the last character from the entry display."""
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current_text[:-1])

    def clear_screen(self):
        """Clear all contents from entry display."""
        self.entry.delete(0, tk.END)

    def calculate_result(self):
        """Evaluate math expression currently displayed."""
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()