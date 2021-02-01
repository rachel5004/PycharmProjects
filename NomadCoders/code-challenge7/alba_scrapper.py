import requests
from bs4 import BeautifulSoup as bs
import csv

url = "http://www.alba.co.kr/"


def save_to_file(company,jobs):
    file = open(company+".csv", mode="w", encoding="UTF-8")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return


# 회사명,링크 ->dict list
def get_companies():
    response = requests.get(url)
    soup = bs(response.text, "html.parser")

    companies = []
    results = soup.find_all("li",{"class":"impact"})
    for result in results:
        company = result.find("span",{"class":"company"}).get_text()
        link = result.find_all("a").attrs['href']
        companies.append({"company":company,"link":link})
    return companies

# 회사별 공고
def extract_company(companies):
    # {"company":company,"link":link}
    for company in companies:
        response = requests.get(company["link"])
        soup = bs(response.text,"html.parser")
        name = company["company"]
        jobdata = get_jobdata(soup)
        save_to_file(company["company"],jobdata)


# job data
def get_jobdata(link):
    job = bs(requests.get(link).text,"html.parser")
    jobs = job.find_all("tr")
    for html in jobs:
        try:
            place = html.find("td",{"class":"local"}).get_text()
            title = html.find("td", {"class": "title"}).find("span",{"class":"company"}).get_text()
            time = html.find("span",{"class":"time"}).get_text()
            pay = html.find("td", {"class": "pay"}).get_text()
            date = html.find("td", {"class": "regDate"}).get_text()
        except: pass

    return {"place":place,"title": title, "time": time
         ,"pay": pay, "date": date}


