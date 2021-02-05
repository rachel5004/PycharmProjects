import requests
from flask import Flask, render_template, request

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]


app = Flask("DayEleven")
@app.route("/")
def main_page():
    return render_template('home.html', subreddits = subreddits)




# /read?sub=on&

# @app.route("/")
# def result_page():
#     read = request.args.get("read")
#     if read == "popular":
#         posts = get_posts("news")
#         return render_template("popular_page.html",posts = posts)
#     elif read == "new":
#         posts = get_posts("newest")
#         return render_template("new_page.html", posts=posts)
#     else:
#         posts = get_posts("news")
#         return render_template("popular_page.html", posts=posts)
# @app.route("/")



app.run(host="127.0.0.1")