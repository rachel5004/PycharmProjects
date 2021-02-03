import requests
from bs4 import BeautifulSoup

site = "https://news.ycombinator.com/"

def extract_posts(word):
    url = site+word
    posts = []
    response = requests.get(url)
    target_list = BeautifulSoup(response.text, "html.parser").find("table", {"class": "itemlist"}).find_all("tr")
    targets = []
    for i in range(0, len(target_list), 3):
        target = [target_list[i], target_list[i + 1]]
        targets.append(target)
        # target = [title, subinfo]
    for target in targets:
        try:
            post = post_info(url,target)
        except:
            pass
        posts.append(post)
    return posts


# <tr> athing > title & link
# <tr> > subsidery info(points, by, comments)
# <tr> spacer > 공백 분리자

def post_info(url,target):
    id = target[0]["id"]
    title = target[0].find("a", {"class": "storylink"}).get_text()
    link = target[0].find("a",{"class":"storylink"})["href"]
    try:
        points = target[1].find("span", {"class": "score"}).get_text()
    except:
        points = '0 points'

    try:
        by = target[1].find("a", {"class": "hnuser"}).get_text()
    except:
        by = 'Anonymous'
    try:
        comments = target[1].find_all("a")[3].get_text()
    except:
        comments = '0 comments'

    try:
        comment_link = target[1].find_all("a")[3]
        commurl = site + comment_link["href"]
    except:
        commurl = "deleted"

    return {"id":id,"title": title, "link": link, "points": points, "by": by
        , "comments": comments,"commurl":commurl}

def get_comments(url):
    commdetails = []
    response = requests.get(url)
    comments = BeautifulSoup(response.text, "html.parser").find_all("td", {"class": "default"})
    for comment in comments:
        commdetail = get_commdetail(comment)
        commdetails.append(commdetail)
    return commdetails


def get_commdetail(comment):
    name = comment.find("a", {"class": "hnuser"}).get_text()
    content = comment.find("span", {"class": "commtext"}).get_text()
    return {'name':name,"content":content}

def get_posts(word):
    posts = extract_posts(word)
    return posts
