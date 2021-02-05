import requests
from bs4 import BeautifulSoup
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

@app.route("/read")
def result_page():
    results = []
    reads = request.args.to_dict("read")
    subs = reads.values()
    for read in reads.values():
        result = scrapper(read)
        results+=result
    return render_template('read.html', subs =subs, results = results)


def scrapper(read):
    posts=[]
    url = f'https://www.reddit.com/r/{read}/top/?t=month'
    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.text,'html.parser').find("div",{"class":"rpBJOHq2PR60pnwJlUyP0"})
    targets = soup.find_all("div",{"class":"_1oQyIsiPHYt6nx7VOmd1sz"})
    for target in targets:
        upvote = target.find("div", {"class": "_1rZYMD_4xY3gRcSS3p8ODO"}).get_text()
        link = target.find("a", {"class": "_3jOxDPIQ0KaOWpzvSQo-1s"})['href']
        title = target.find("h3").get_text()
        post = {"upvote":upvote,"title":title,"link":link,"sub":read}
        posts.append(post)
    return posts

app.run(host="127.0.0.1")