import tkinter as tk
from tkinter import ttk


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("500x700")
        self.root.config(bg="#1e1e1e")
        self.root.resizable(False, False)

        # Display entry
        self.entry = tk.Entry(
            self.root,
            font=("Segoe UI", 32, "bold"),
            bg="#2d2d2d",
            fg="#ffffff",
            borderwidth=0,
            justify="right",
            insertbackground="#ffffff",
        )
        self.entry.bind("<Return>", lambda event: self.calculate())
        self.entry.bind("<BackSpace>", lambda event: self.backspace())
        self.entry.bind("<Escape>", lambda event: self.clear())
        self.entry.pack(padx=15, pady=20, fill="both", ipady=15)

        # Button frame
        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(padx=15, pady=10, fill="both", expand=True)

        # Button styling
        num_btn_style = {
            "font": ("Segoe UI", 18, "bold"),
            "bg": "#404040",
            "fg": "#ffffff",
            "activebackground": "#505050",
            "activeforeground": "#ffffff",
            "borderwidth": 0,
            "height": 3,
            "width": 7,
        }
        op_btn_style = {
            "font": ("Segoe UI", 18, "bold"),
            "bg": "#ff9500",
            "fg": "#ffffff",
            "activebackground": "#ffb143",
            "activeforeground": "#ffffff",
            "borderwidth": 0,
            "height": 3,
            "width": 7,
        }
        eq_btn_style = {
            "font": ("Segoe UI", 18, "bold"),
            "bg": "#34c759",
            "fg": "#ffffff",
            "activebackground": "#5dd981",
            "activeforeground": "#ffffff",
            "borderwidth": 0,
            "height": 3,
            "width": 7,
        }
        clr_btn_style = {
            "font": ("Segoe UI", 18, "bold"),
            "bg": "#ff3b30",
            "fg": "#ffffff",
            "activebackground": "#ff5c52",
            "activeforeground": "#ffffff",
            "borderwidth": 0,
            "height": 3,
            "width": 7,
        }
        paren_btn_style = {
            "font": ("Segoe UI", 18, "bold"),
            "bg": "#5b5bff",
            "fg": "#ffffff",
            "activebackground": "#7b7bff",
            "activeforeground": "#ffffff",
            "borderwidth": 0,
            "height": 3,
            "width": 7,
        }

        # Create buttons with grid
        buttons = [
            (
                tk.Button(
                    button_frame,
                    text="(",
                    command=lambda: self.entry.insert(tk.END, "("),
                    **paren_btn_style,
                ),
                0,
                0,
            ),
            (
                tk.Button(
                    button_frame,
                    text=")",
                    command=lambda: self.entry.insert(tk.END, ")"),
                    **paren_btn_style,
                ),
                0,
                1,
            ),
            (
                tk.Button(
                    button_frame,
                    text="±",
                    command=self.toggle_sign,
                    **paren_btn_style,
                ),
                0,
                2,
            ),
            (
                tk.Button(
                    button_frame,
                    text="/",
                    command=lambda: self.entry.insert(tk.END, "/"),
                    **op_btn_style,
                ),
                0,
                3,
            ),
            (
                tk.Button(
                    button_frame,
                    text="7",
                    command=lambda: self.entry.insert(tk.END, "7"),
                    **num_btn_style,
                ),
                1,
                0,
            ),
            (
                tk.Button(
                    button_frame,
                    text="8",
                    command=lambda: self.entry.insert(tk.END, "8"),
                    **num_btn_style,
                ),
                1,
                1,
            ),
            (
                tk.Button(
                    button_frame,
                    text="9",
                    command=lambda: self.entry.insert(tk.END, "9"),
                    **num_btn_style,
                ),
                1,
                2,
            ),
            (
                tk.Button(
                    button_frame,
                    text="*",
                    command=lambda: self.entry.insert(tk.END, "*"),
                    **op_btn_style,
                ),
                1,
                3,
            ),
            (
                tk.Button(
                    button_frame,
                    text="4",
                    command=lambda: self.entry.insert(tk.END, "4"),
                    **num_btn_style,
                ),
                2,
                0,
            ),
            (
                tk.Button(
                    button_frame,
                    text="5",
                    command=lambda: self.entry.insert(tk.END, "5"),
                    **num_btn_style,
                ),
                2,
                1,
            ),
            (
                tk.Button(
                    button_frame,
                    text="6",
                    command=lambda: self.entry.insert(tk.END, "6"),
                    **num_btn_style,
                ),
                2,
                2,
            ),
            (
                tk.Button(
                    button_frame,
                    text="-",
                    command=lambda: self.entry.insert(tk.END, "-"),
                    **op_btn_style,
                ),
                2,
                3,
            ),
            (
                tk.Button(
                    button_frame,
                    text="1",
                    command=lambda: self.entry.insert(tk.END, "1"),
                    **num_btn_style,
                ),
                3,
                0,
            ),
            (
                tk.Button(
                    button_frame,
                    text="2",
                    command=lambda: self.entry.insert(tk.END, "2"),
                    **num_btn_style,
                ),
                3,
                1,
            ),
            (
                tk.Button(
                    button_frame,
                    text="3",
                    command=lambda: self.entry.insert(tk.END, "3"),
                    **num_btn_style,
                ),
                3,
                2,
            ),
            (
                tk.Button(
                    button_frame,
                    text="+",
                    command=lambda: self.entry.insert(tk.END, "+"),
                    **op_btn_style,
                ),
                3,
                3,
            ),
            (
                tk.Button(
                    button_frame,
                    text="0",
                    command=lambda: self.entry.insert(tk.END, "0"),
                    **num_btn_style,
                ),
                4,
                0,
            ),
            (
                tk.Button(
                    button_frame,
                    text=".",
                    command=lambda: self.entry.insert(tk.END, "."),
                    **num_btn_style,
                ),
                4,
                1,
            ),
            (
                tk.Button(
                    button_frame,
                    text="⌫",
                    command=self.backspace,
                    **clr_btn_style,
                ),
                4,
                2,
            ),
            (
                tk.Button(
                    button_frame, text="=", command=self.calculate, **eq_btn_style
                ),
                4,
                3,
            ),
            (
                tk.Button(
                    button_frame,
                    text="C",
                    command=self.clear,
                    **clr_btn_style,
                ),
                5,
                0,
            ),
        ]

        for btn, row, col in buttons:
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Configure grid weights for responsiveness
        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)

        self.root.mainloop()

    def backspace(self):
        """Delete last character safely"""
        current = self.entry.get()
        if current:
            self.entry.delete(len(current) - 1, tk.END)

    def clear(self):
        """Clear the display"""
        self.entry.delete(0, tk.END)

    def toggle_sign(self):
        """Toggle positive/negative for current number"""
        current = self.entry.get()
        if not current:
            return

        # Try to toggle the sign of the last number
        if current.startswith("-"):
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current[1:])
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "-" + current)

    def calculate(self):
        """Evaluate the expression"""
        try:
            expression = self.entry.get()
            if not expression:
                return

            # Replace ^ with ** for exponentiation
            expression = expression.replace("^", "**")
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except ZeroDivisionError:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Cannot divide by 0")
        except SyntaxError:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Syntax Error")
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")


Calculator()
