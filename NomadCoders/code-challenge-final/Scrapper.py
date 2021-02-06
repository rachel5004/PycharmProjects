import requests
from bs4 import BeautifulSoup

#########
wwr = "https://weworkremotely.com/remote-jobs/search?term="
def WWR_scrapper():
    wwr_jobs =[]
    response = requests.get(wwr+"python")
    results = BeautifulSoup(response.text,'html.parser').find("section",{"class":"jobs"}).find_all("li")

    for result in results:
        job = WWR_getinfo(result)
        wwr_jobs.append(job)
    print(wwr_jobs)
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
    try:
        title = result.find("span", {"class": "title"}).get_text()
        company = result.find("span", {"class": "company"}).get_text()
        link = "https://weworkremotely.com/remote-jobs" + result.find("a")["href"].replace("/company", "")
        return {"title": title, "company": company, "link": link}
    except:pass

def OK_getinfo():
    pass

WWR_scrapper()