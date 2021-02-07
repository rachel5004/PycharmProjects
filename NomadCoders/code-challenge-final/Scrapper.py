import requests
from bs4 import BeautifulSoup

#########
wwr=''
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
ok =  "https://remoteok.io/"
def OK_scrapper(word):
    ok_jobs = []
    response = requests.get(f"{ok}remote-dev+{word}-jobs",headers = headers)
    results = BeautifulSoup(response.text,'html.parser').find_all("tr",{"class":"job"})

    for result in results:
        job = OK_getinfo(result)
        ok_jobs.append(job)
    return ok_jobs
############

def SO_getinfo(result):
    title = result.find("h2", {"class": "mb4"})
    title_anchor = title.find("a")["title"]
    title = title_anchor
    company= result.find("h3", {"class": "fc-black-700"}).find("span")
    company = company.get_text(strip=True).replace("\r\n", "")
    job_id = result["data-result-id"]

    return {"title": title, "company": company, "link": f"https://stackoverflow.com/jobs/{job_id}"}

def WWR_getinfo(result):
    title = result.find("span", {"class": "title"}).get_text()
    company = result.find("span", {"class": "company"}).get_text()
    link = wwr + result.find("a")["href"].replace("/company", "")

    return {"title": title, "company": company, "link": link}


def OK_getinfo(result):
    title = result.find("h2", {"itemprop": "title"}).get_text()
    company = result.find("h3", {"itemprop": "name"}).get_text()
    link = ok+result.find("a", {"itemprop": "url"})["href"]

    return {"title": title, "company": company, "link": link}

