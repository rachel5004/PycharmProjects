import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/jobs?q=python"


def extract_so_pages():
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pagination[-2].get_text()
    return int(last_page)


def extract_so_jobs(last_page):
    jobs = []
    for p in range(last_page):
        print(f"Scrapping SO: page {p+1}...")
        result = requests.get(f"{url}&pg={p}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_jobinfo(result)
            jobs.append(job)
    return jobs


def extract_jobinfo(html):
    title = html.find("h2", {"class": "mb4"})
    title_anchor = title.find("a")["title"]
    title = title_anchor

    company, location = html.find("h3", {"class": "fc-black-700"}).find_all("span", recursive=False)

    company = company.get_text(strip=True).replace("\r\n", "")
    location = location.get_text(strip=True)
    job_id = html["data-result-id"]

    return {"title": title, "company": company, "location": location
        , "link": f"https://stackoverflow.com/jobs/{job_id}"}


def get_jobs():
    last_page = extract_so_pages()
    jobs = extract_so_jobs(last_page)
    return jobs

