"""Задание 3: статическая страница + CSS."""

from flask import Flask, render_template
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
app = Flask(
    __name__,
    static_folder=str(BASE_DIR / "static"),
    template_folder=str(BASE_DIR / "templates"),
)


@app.route("/")
def static_page() -> str:
    return render_template("static_page.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
