
import requests


def getURL():
    str = input().replace(" ","")
    urls = list(str.lower().replace("http://", "").split(","))
    for url in urls:
        if ".com" in url:
            if isLegit(("http://" + url)):
                print(f"http://{url} is up!")
            else:
                print(f"http://{url} is down!")
        else:
            print(f"{url} is not a valid URL")
    wantStartOver()


def wantStartOver():
    print("Do you want to start over? y/n")
    ans = input().lower()
    if ans == "n":
        print("K, bye!")
    elif ans == "y":
        getURL()
    else:
        print("That's not a valid answer")
        wantStartOver()


def isLegit(url):
    try:
        if requests.get(url).status_code:
            return True
    except requests.exceptions.ConnectionError:
        return False



####################
print("Please write a URL for URLs you want to check(seperated by comma)")

getURL()
