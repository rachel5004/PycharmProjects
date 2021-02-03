from flask import Flask, request, render_template
from hacker_scrapper import get_posts,get_comments

app = Flask(__name__)

@app.route("/")
def main_page():
    order_by = request.args.get("order_by")
    if order_by == "popular":
        posts = get_posts("news")
        return render_template("popular_page.html",posts = posts)
    elif order_by == "new":
        posts = get_posts("newest")
        return render_template("new_page.html", posts=posts)
    else:
        posts = get_posts("news")
        return render_template("popular_page.html", posts=posts)

@app.route("/<id>")
def id_pg(id):
    posts = get_posts('news') + get_posts('newest')
    for tmppost in posts:
        if tmppost["id"] == id:
            selpost = tmppost
            commdetails = get_comments(selpost["commurl"])
            return render_template("id_page.html", post = selpost, comments = commdetails)

if __name__ == "__main__":
    app.run(host="127.0.0.1",debug=True)
