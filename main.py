import random
from flask import Flask, render_template, request, make_response, redirect, url_for


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html")


if __name__ == '__main__':
    app.run(use_reloader=True)