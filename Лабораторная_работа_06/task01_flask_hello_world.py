"""Задание 1: Flask-приложение Hello World."""

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    return "Hello World от Flask!"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
