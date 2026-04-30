import tkinter as tk
from tkinter import ttk


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.config(bg="#1e1e1e")
        self.root.resizable(True, True)
        self.root.minsize(400, 500)

        # History storage
        self.history = []
        self.history_window = None

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
        self.entry.pack(padx=15, pady=15, fill="x", ipady=12)

        # Button frame
        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(padx=15, pady=15, fill="both", expand=True)

        # Button styling
        num_btn_style = {
            "font": ("Segoe UI", 16, "bold"),
            "bg": "#404040",
            "fg": "#ffffff",
            "activebackground": "#505050",
            "activeforeground": "#ffffff",
            "borderwidth": 0,
        }
        op_btn_style = {
            "font": ("Segoe UI", 16, "bold"),
            "bg": "#ff9500",
            "fg": "#ffffff",
            "activebackground": "#ffb143",
            "activeforeground": "#ffffff",
            "borderwidth": 0,
        }
        eq_btn_style = {
            "font": ("Segoe UI", 16, "bold"),
            "bg": "#34c759",
            "fg": "#ffffff",
            "activebackground": "#5dd981",
            "activeforeground": "#ffffff",
            "borderwidth": 0,
        }
        clr_btn_style = {
            "font": ("Segoe UI", 16, "bold"),
            "bg": "#ff3b30",
            "fg": "#ffffff",
            "activebackground": "#ff5c52",
            "activeforeground": "#ffffff",
            "borderwidth": 0,
        }
        paren_btn_style = {
            "font": ("Segoe UI", 16, "bold"),
            "bg": "#5b5bff",
            "fg": "#ffffff",
            "activebackground": "#7b7bff",
            "activeforeground": "#ffffff",
            "borderwidth": 0,
        }
        hist_btn_style = {
            "font": ("Segoe UI", 16, "bold"),
            "bg": "#9c27b0",
            "fg": "#ffffff",
            "activebackground": "#ab47bc",
            "activeforeground": "#ffffff",
            "borderwidth": 0,
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
            (
                tk.Button(
                    button_frame,
                    text="📜 History",
                    command=self.show_history,
                    **hist_btn_style,
                ),
                5,
                1,
            ),
        ]

        for btn, row, col in buttons:
            btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")

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

            # Store original expression for history
            original_expr = expression

            # Replace ^ with ** for exponentiation
            expression = expression.replace("^", "**")
            result = eval(expression)

            # Add to history
            self.history.append(f"{original_expr} = {result}")

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

    def show_history(self):
        """Display history in a separate window"""
        if self.history_window is None or not self.history_window.winfo_exists():
            self.history_window = tk.Toplevel(self.root)
            self.history_window.title("Calculation History")
            self.history_window.geometry("400x500")
            self.history_window.config(bg="#1e1e1e")

            # Title
            title = tk.Label(
                self.history_window,
                text="History",
                font=("Segoe UI", 18, "bold"),
                bg="#1e1e1e",
                fg="#ffffff",
            )
            title.pack(pady=10)

            # History listbox with scrollbar
            frame = tk.Frame(self.history_window, bg="#1e1e1e")
            frame.pack(fill="both", expand=True, padx=10, pady=10)

            scrollbar = tk.Scrollbar(frame)
            scrollbar.pack(side="right", fill="y")

            self.history_listbox = tk.Listbox(
                frame,
                font=("Segoe UI", 12),
                bg="#2d2d2d",
                fg="#ffffff",
                yscrollcommand=scrollbar.set,
                selectmode="single",
            )
            self.history_listbox.pack(side="left", fill="both", expand=True)
            scrollbar.config(command=self.history_listbox.yview)

            # Bind double-click to load expression
            self.history_listbox.bind("<Double-Button-1>", self.on_history_select)

            # Populate listbox with history in reverse order (newest first)
            for item in reversed(self.history):
                self.history_listbox.insert(0, item)

            # Button frame
            btn_frame = tk.Frame(self.history_window, bg="#1e1e1e")
            btn_frame.pack(fill="x", padx=10, pady=10)

            # Clear history button
            clear_btn = tk.Button(
                btn_frame,
                text="Clear All",
                font=("Segoe UI", 12, "bold"),
                bg="#ff3b30",
                fg="#ffffff",
                command=self.clear_history,
                relief="flat",
            )
            clear_btn.pack(side="left", padx=5)

            # Close button
            close_btn = tk.Button(
                btn_frame,
                text="Close",
                font=("Segoe UI", 12, "bold"),
                bg="#404040",
                fg="#ffffff",
                command=self.history_window.destroy,
                relief="flat",
            )
            close_btn.pack(side="right", padx=5)
        else:
            # Window exists, bring it to front
            self.history_window.lift()

    def on_history_select(self, event):
        """Load expression from history when double-clicked"""
        selection = self.history_listbox.curselection()
        if selection:
            item = self.history_listbox.get(selection[0])
            # Extract just the expression (before the "=")
            expression = item.split(" = ")[0]
            self.entry.delete(0, tk.END)
            self.entry.insert(0, expression)
            self.history_window.destroy()

    def clear_history(self):
        """Clear all history"""
        self.history = []
        self.history_listbox.delete(0, tk.END)


Calculator()
