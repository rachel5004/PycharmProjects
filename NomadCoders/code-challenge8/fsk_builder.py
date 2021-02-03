from flask import Flask, request, redirect, render_template
app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("popular_page.html")

@app.route("/?order_by=new")
def newest():
    return render_template('new_page.html')

@app.route("/?order_by=popular")
def news():
    return render_template('popular_page.html')

@app.route("/<id>")
def id():
    pass

