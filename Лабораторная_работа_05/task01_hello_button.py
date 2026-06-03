"""Задание 1: окно с кнопкой «Привет»."""

import tkinter as tk
from tkinter import messagebox, ttk


def main() -> None:
    root = tk.Tk()
    root.title("Задание 1")
    root.geometry("320x160")

    ttk.Label(root, text="Окно с кнопкой «Привет»").pack(pady=20)
    ttk.Button(root, text="Привет", command=lambda: messagebox.showinfo("Привет", "Здравствуйте!")).pack()

    root.mainloop()


if __name__ == "__main__":
    main()
