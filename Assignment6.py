import tkinter as tk
from tkinter import font


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.expression = ""

        # Display field
        self.display = tk.Entry(
            root,
            font=("Arial", 20),
            borderwidth=2,
            relief="solid",
            justify="right"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10, sticky="nsew")

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ]

        # Create buttons
        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        # Clear button
        self.create_clear_button()

        # Configure grid
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

    def create_button(self, text, row, col):
        btn = tk.Button(
            self.root,
            text=text,
            font=("Arial", 18),
            command=lambda: self.on_button_click(text)
        )
        btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def create_clear_button(self):
        btn = tk.Button(
            self.root,
            text="C",
            font=("Arial", 18),
            command=self.clear,
            bg="#ff6b6b"
        )
        btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.expression = str(result)
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

