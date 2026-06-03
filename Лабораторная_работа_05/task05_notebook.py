"""Задание 5: программа со вкладками Notebook."""

import tkinter as tk
from tkinter import ttk


def main() -> None:
    root = tk.Tk()
    root.title("Задание 5")
    root.geometry("440x260")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    for title, text in (
        ("Главная", "Первая вкладка"),
        ("Данные", "Вторая вкладка"),
        ("Настройки", "Третья вкладка"),
    ):
        frame = ttk.Frame(notebook, padding=20)
        notebook.add(frame, text=title)
        ttk.Label(frame, text=text).pack(pady=30)

    root.mainloop()


if __name__ == "__main__":
    main()
