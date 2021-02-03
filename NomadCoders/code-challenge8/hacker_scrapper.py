import requests
from bs4 import BeautifulSoup


def extract_posts(word):
    url = f"https://news.ycombinator.com/{word}"
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
                if word == "news":
                    post = popular_post_info(target)
                elif word == "newest":
                    post = new_post_info(target)
            except:
                pass
            posts.append(post)
    print(posts)


# <tr> athing > title & link
# <tr> > subsidery info(points, by, comments)
# <tr> spacer > 공백 분리자

def popular_post_info(target):
    title = target[0].find("a", {"class": "storylink"}).get_text()
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

    return {"title": title, "points": points, "by": by
        , "comments": comments}


def new_post_info(target):
    title = target[0].find("a", {"class": "storylink"}).get_text()
    link = target[0].find("a")['href']
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

    return {"title": title, "link": link, "points": points, "by": by
        , "comments": comments}


def get_posts(word):
    posts = extract_posts(word)
    return posts

print(get_posts('newest'))