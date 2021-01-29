import requests
from bs4 import BeautifulSoup as bs

dic = {}
url = requests.get("https://www.iban.com/currency-codes")
data = bs(url.text, "html.parser")
res = data.find_all("td")  # res[0],res[3] i=0,i[res.lenth-1],4
num=0
for i in range(0, len(res), 4):
    dic["#"+str(num)+". "+str(res[i]).replace("<td>", "").replace("</td>", "")]\
        = str(res[i + 2]).replace("<td>", "").replace("</td>","")
    num+=1

def main():
    print("Hello! Please choose a country by number:")
    for country in dic.keys():
        print(country)
    userChoice()


def userChoice():
    try:
        sel = int(input("#: "))
        if sel > len(dic):
            print("choose a number from the list.")
            userChoice()
        else:
            for k in dic.keys():
                if str(sel) in k:
                    key = k
                    break
            print("You choose", key[key.index(" ")+1:])
            print("The currency code is", dic[key])
    except:
            print("that wasn't a number.")
            userChoice()

main()