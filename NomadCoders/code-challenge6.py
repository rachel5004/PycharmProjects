import requests
from bs4 import BeautifulSoup as bs

dic = []
url = requests.get("https://www.iban.com/currency-codes")
data = bs(url.text, "html.parser")
res = data.find_all("td")  # res[0],res[3] i=0,i[res.lenth-1],4
# [{country:currency}]
for i in range(0, len(res), 4):
    country = {
        str(res[i]).replace("<td>", "").replace("</td>", ""): str(res[i + 2]).replace("<td>", "").replace("</td>", "")}
    dic.append(country)

def choice():
    sel = int(input("#: "))
    try:
        if sel > len(dic):
            print("choose a number from the list.")
            choice()
        else:
            print(list(dic[sel].keys())[0])
            return sel
    except:
        print("that wasn't a number.")
        choice()

def convert(country1, country2):
    print(f"How many {list(dic[country1].values())[0]} do you want to convert to {list(dic[country2].values())[0]}?")
    try:
        money = int(input())
        pass
        # convert src
    except:
        print("That's not a number.")
        convert(country1,country2)

def main():
    num = 0
    for i in dic:
        print("#", num, list(i.keys())[0])
        num += 1
    print("Where are oy from? Choose a country by number.")
    country1 = choice()
    print("Now choose another country.")
    country2 = choice()
    convert(country1,country2)


main()
