"""Задание 5: страница с Bootstrap."""

from flask import Flask, render_template
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
app = Flask(
    __name__,
    static_folder=str(BASE_DIR / "static"),
    template_folder=str(BASE_DIR / "templates"),
)


@app.route("/")
def bootstrap_page() -> str:
    return render_template("bootstrap_page.html")


if __name__ == "__main__":
    app.run(debug=True, port=5005)
