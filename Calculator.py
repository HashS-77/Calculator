import tkinter as tk


class Calculator:
    def __init__(self):
        self.root = tk.Tk()

        self.entry = tk.Entry(self.root, width=30, borderwidth=5, font=("Arial", 20))
        self.entry.bind("<Return>", lambda event: self.calculate())
        self.entry.pack(padx=10, pady=10)

        button_frame = tk.Frame(self.root)
        btn1 = tk.Button(
            button_frame,
            text="1",
            width=5,
            height=2,
            borderwidth=1,
            font=("Arial", 20),
            command=lambda: self.entry.insert(tk.END, "1"),
        )
        btn2 = tk.Button(
            button_frame,
            text="2",
            width=5,
            height=2,
            borderwidth=1,
            font=("Arial", 20),
            command=lambda: self.entry.insert(tk.END, "2"),
        )
        btn3 = tk.Button(
            button_frame,
            text="3",
            width=5,
            height=2,
            borderwidth=1,
            font=("Arial", 20),
            command=lambda: self.entry.insert(tk.END, "3"),
        )
        btn4 = tk.Button(
            button_frame,
            text="4",
            width=5,
            height=2,
            borderwidth=1,
            font=("Arial", 20),
            command=lambda: self.entry.insert(tk.END, "4"),
        )
        btn5 = tk.Button(
            button_frame,
            text="5",
            width=5,
            height=2,
            borderwidth=1,
            font=("Arial", 20),
            command=lambda: self.entry.insert(tk.END, "5"),
        )
        btn6 = tk.Button(
            button_frame,
            text="6",
            width=5,
            height=2,
            borderwidth=1,
            font=("Arial", 20),
            command=lambda: self.entry.insert(tk.END, "6"),
        )
        btn7 = tk.Button(
            button_frame,
            text="7",
            width=5,
            height=2,
            borderwidth=1,
            font=("Arial", 20),
            command=lambda: self.entry.insert(tk.END, "7"),
        )
        btn8 = tk.Button(
            button_frame,
            text="8",
            width=5,
            height=2,
            borderwidth=1,
            font=("Arial", 20),
            command=lambda: self.entry.insert(tk.END, "8"),
        )
        btn9 = tk.Button(
            button_frame,
            text="9",
            width=5,
            height=2,
            borderwidth=1,
            font=("Arial", 20),
            command=lambda: self.entry.insert(tk.END, "9"),
        )
        btn0 = tk.Button(
            button_frame,
            text="0",
            width=5,
            height=2,
            borderwidth=1,
            font=("Arial", 20),
            command=lambda: self.entry.insert(tk.END, "0"),
        )
        btn_add = tk.Button(
            button_frame,
            text="+",
            width=5,
            height=2,
            borderwidth=1,
            font=("Arial", 20),
            command=lambda: self.entry.insert(tk.END, "+"),
        )
        btn_sub = tk.Button(
            button_frame,
            text="-",
            width=5,
            height=2,
            borderwidth=1,
            font=("Arial", 20),
            command=lambda: self.entry.insert(tk.END, "-"),
        )
        btn_mul = tk.Button(
            button_frame,
            text="*",
            width=5,
            height=2,
            borderwidth=1,
            font=("Arial", 20),
            command=lambda: self.entry.insert(tk.END, "*"),
        )
        btn_div = tk.Button(
            button_frame,
            text="/",
            width=5,
            height=2,
            borderwidth=1,
            font=("Arial", 20),
            command=lambda: self.entry.insert(tk.END, "/"),
        )
        btn_equal = tk.Button(
            button_frame,
            text="=",
            width=5,
            height=2,
            borderwidth=1,
            font=("Arial", 20),
            command=self.calculate,
        )
        btn_clear = tk.Button(
            button_frame,
            text="C",
            width=5,
            height=2,
            borderwidth=1,
            font=("Arial", 20),
            command=lambda: self.entry.delete(0, tk.END),
        )
        btn1.grid(row=0, column=0)
        btn2.grid(row=0, column=1)
        btn3.grid(row=0, column=2)
        btn4.grid(row=1, column=0)
        btn5.grid(row=1, column=1)
        btn6.grid(row=1, column=2)
        btn7.grid(row=2, column=0)
        btn8.grid(row=2, column=1)
        btn9.grid(row=2, column=2)
        btn0.grid(row=3, column=1)
        btn_add.grid(row=0, column=3)
        btn_sub.grid(row=1, column=3)
        btn_mul.grid(row=2, column=3)
        btn_div.grid(row=3, column=3)
        btn_equal.grid(row=3, column=2)
        btn_clear.grid(row=3, column=0)
        button_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.root.mainloop()

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except:  # noqa: E722
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")


Calculator()
