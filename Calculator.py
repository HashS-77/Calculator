"""Modern Calculator Application with History Tracking

Features:
- Basic arithmetic operations (+, -, *, /)
- Parentheses for order of operations
- Sign toggle (±) for positive/negative numbers
- Backspace and Clear functions
- Calculation history with load capability
- Dark theme with responsive UI
"""

import tkinter as tk


class Calculator:
    """Main Calculator class that creates and manages the GUI"""

    def __init__(self):
        """Initialize the calculator GUI and set up event bindings"""
        # Create main window
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.config(bg="#1e1e1e")  # Dark background
        self.root.resizable(True, True)  # Allow window resizing
        self.root.minsize(400, 500)  # Set minimum window size

        # Initialize history storage
        self.history = []  # List to store all calculations
        self.history_window = None  # Reference to history window (if open)

        # Create display entry field for showing input and results
        self.entry = tk.Entry(
            self.root,
            font=("Segoe UI", 32, "bold"),  # Large bold font
            bg="#2d2d2d",  # Dark gray background
            fg="#ffffff",  # White text
            borderwidth=0,  # No border
            justify="right",  # Right-align text
            insertbackground="#ffffff",  # White cursor
        )
        # Bind keyboard shortcuts
        self.entry.bind(
            "<Return>", lambda event: self.calculate()
        )  # Enter to calculate
        self.entry.bind(
            "<BackSpace>", lambda event: self.backspace()
        )  # Backspace to delete
        self.entry.bind("<Escape>", lambda event: self.clear())  # Escape to clear
        self.entry.pack(padx=15, pady=15, fill="x", ipady=12)

        # Create frame to hold all buttons
        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(padx=15, pady=15, fill="both", expand=True)

        # Define color schemes for different button types
        # Number button style (gray)
        num_btn_style = {
            "font": ("Segoe UI", 16, "bold"),
            "bg": "#404040",  # Dark gray
            "fg": "#ffffff",  # White text
            "activebackground": "#505050",  # Lighter gray when clicked
            "activeforeground": "#ffffff",
            "borderwidth": 0,  # Flat style
        }
        # Operator button style (orange) - for +, -, *, /
        op_btn_style = {
            "font": ("Segoe UI", 16, "bold"),
            "bg": "#ff9500",  # Orange
            "fg": "#ffffff",
            "activebackground": "#ffb143",  # Lighter orange
            "activeforeground": "#ffffff",
            "borderwidth": 0,
        }
        # Equals button style (green) - for calculation trigger
        eq_btn_style = {
            "font": ("Segoe UI", 16, "bold"),
            "bg": "#34c759",  # Green
            "fg": "#ffffff",
            "activebackground": "#5dd981",  # Lighter green
            "activeforeground": "#ffffff",
            "borderwidth": 0,
        }
        # Clear/Delete button style (red) - for C and ⌫ buttons
        clr_btn_style = {
            "font": ("Segoe UI", 16, "bold"),
            "bg": "#ff3b30",  # Red
            "fg": "#ffffff",
            "activebackground": "#ff5c52",  # Lighter red
            "activeforeground": "#ffffff",
            "borderwidth": 0,
        }
        # Parentheses button style (blue) - for (, ), ± buttons
        paren_btn_style = {
            "font": ("Segoe UI", 16, "bold"),
            "bg": "#5b5bff",  # Blue
            "fg": "#ffffff",
            "activebackground": "#7b7bff",  # Lighter blue
            "activeforeground": "#ffffff",
            "borderwidth": 0,
        }
        # History button style (purple)
        hist_btn_style = {
            "font": ("Segoe UI", 16, "bold"),
            "bg": "#9c27b0",  # Purple
            "fg": "#ffffff",
            "activebackground": "#ab47bc",  # Lighter purple
            "activeforeground": "#ffffff",
            "borderwidth": 0,
        }

        # Create list of all buttons with their positions and styles
        # Format: (Button widget, row, column)
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

        # Configure grid to be responsive - buttons expand to fill available space
        for i in range(6):  # 6 rows
            button_frame.grid_rowconfigure(i, weight=1)  # Equal weight = equal size
        for i in range(4):  # 4 columns
            button_frame.grid_columnconfigure(i, weight=1)

        # Start the GUI event loop
        self.root.mainloop()

    def backspace(self):
        """Delete the last character from the display"""
        current = self.entry.get()  # Get current text
        if current:  # Only delete if there's text
            self.entry.delete(len(current) - 1, tk.END)  # Delete last char

    def clear(self):
        """Clear all text from the display"""
        self.entry.delete(0, tk.END)  # Delete from start (0) to end (END)

    def toggle_sign(self):
        """Toggle the sign (positive/negative) of the entire expression"""
        current = self.entry.get()  # Get current display text
        if not current:
            return  # Do nothing if empty

        # Remove or add negative sign at the start
        if current.startswith("-"):
            # If starts with -, remove it
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current[1:])  # Insert without the minus
        else:
            # If positive, add minus
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "-" + current)  # Insert with minus prefix

    def calculate(self):
        """Evaluate the mathematical expression and show result"""
        try:
            expression = self.entry.get()  # Get user input
            if not expression:
                return  # Do nothing if empty

            # Store original for history (before modification)
            original_expr = expression

            # Convert ^ to ** for Python exponentiation syntax
            expression = expression.replace("^", "**")

            # Evaluate the expression using Python's eval()
            result = eval(expression)

            # Record this calculation in history
            self.history.append(f"{original_expr} = {result}")

            # Clear display and show result
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))

        # Handle specific errors gracefully
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
        """Open a new window to display calculation history"""
        # Check if history window already exists and is open
        if self.history_window is None or not self.history_window.winfo_exists():
            # Create new history window
            self.history_window = tk.Toplevel(self.root)
            self.history_window.title("Calculation History")
            self.history_window.geometry("400x500")
            self.history_window.config(bg="#1e1e1e")

            # Add title label at top
            title = tk.Label(
                self.history_window,
                text="History",
                font=("Segoe UI", 18, "bold"),
                bg="#1e1e1e",
                fg="#ffffff",
            )
            title.pack(pady=10)

            # Create container frame for listbox and scrollbar
            frame = tk.Frame(self.history_window, bg="#1e1e1e")
            frame.pack(fill="both", expand=True, padx=10, pady=10)

            # Add scrollbar for when history is long
            scrollbar = tk.Scrollbar(frame)
            scrollbar.pack(side="right", fill="y")

            # Create listbox to display history items
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

            # Allow double-click to load a calculation
            self.history_listbox.bind("<Double-Button-1>", self.on_history_select)

            # Fill listbox with history (newest entries first)
            for item in reversed(self.history):
                self.history_listbox.insert(0, item)

            # Create frame for buttons at bottom
            btn_frame = tk.Frame(self.history_window, bg="#1e1e1e")
            btn_frame.pack(fill="x", padx=10, pady=10)

            # Button to clear all history
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

            # Button to close the history window
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
            # If window already exists, just bring it to the foreground
            self.history_window.lift()

    def on_history_select(self, event):
        """Handle double-click on history item - load its expression"""
        selection = self.history_listbox.curselection()  # Get selected item
        if selection:
            item = self.history_listbox.get(selection[0])  # Get the full text
            # Split on " = " to get just the expression part
            expression = item.split(" = ")[0]  # Everything before the equals
            # Put expression back in main calculator display
            self.entry.delete(0, tk.END)
            self.entry.insert(0, expression)
            # Close the history window
            self.history_window.destroy()

    def clear_history(self):
        """Delete all stored calculation history"""
        self.history = []  # Empty the history list
        self.history_listbox.delete(0, tk.END)  # Clear the display listbox


Calculator()
