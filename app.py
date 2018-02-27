import os
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hi.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
