"""Задание 3: простейший калькулятор."""

import tkinter as tk
from tkinter import ttk


def main() -> None:
    root = tk.Tk()
    root.title("Задание 3")
    root.geometry("420x180")

    first = tk.DoubleVar(value=10)
    second = tk.DoubleVar(value=5)
    operation = tk.StringVar(value="+")
    result = tk.StringVar(value="")

    ttk.Entry(root, textvariable=first, width=15).grid(row=0, column=0, padx=8, pady=16)
    ttk.Combobox(root, textvariable=operation, values=["+", "-", "*", "/"], width=5, state="readonly").grid(
        row=0, column=1, padx=8, pady=16
    )
    ttk.Entry(root, textvariable=second, width=15).grid(row=0, column=2, padx=8, pady=16)

    def calculate() -> None:
        a = first.get()
        b = second.get()
        op = operation.get()
        if op == "+":
            value = a + b
        elif op == "-":
            value = a - b
        elif op == "*":
            value = a * b
        elif b == 0:
            result.set("Деление на ноль")
            return
        else:
            value = a / b
        result.set(f"Результат: {value:g}")

    ttk.Button(root, text="=", command=calculate).grid(row=0, column=3, padx=8, pady=16)
    ttk.Label(root, textvariable=result).grid(row=1, column=0, columnspan=4, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
