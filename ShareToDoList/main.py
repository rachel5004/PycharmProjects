import os
from flask import Flask, render_template, request, redirect, send_file


app = Flask("ToDO")

@app.route('/')
def mainpage():
    return render_template("login.html")

app.run(host="127.0.0.1")

