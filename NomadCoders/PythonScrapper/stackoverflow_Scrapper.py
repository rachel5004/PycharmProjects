import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/jobs?q=python"


def extract_so_pages():
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div",{"class":"s-pagination"}).find_all("a")
    # pages = pagination.find_all("a",{"class":"s-pagination--item"})

    last_page = pagination[-2].get_text()
    return int(last_page)
    # spans = []
    # for page in pages[:-1]:
    #     spans.append(int(page.get_text()))
    # max_page = spans[-1]
    # return max_page


def extract_so_jobs(last_page):
    jobs = []
    for p in range(3):
        print(f"Scrapping page {p}...")
        result = requests.get(f"{url}&pg={p}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div",{"class":"-job"})
        for result in results:
            # print(result["data-result-id"])
            job = extract_jobinfo(result)
            jobs.append(job)
    return jobs

def extract_jobinfo(html):
    title = html.find("h2", {"class": "mb4"})
    title_anchor = title.find("a")["title"]
    title = title_anchor

    company, location = html.find("h3", {"class": "fc-black-700"}).find_all("span",recursive=False)

    company = company.get_text().strip().replace("\r\n","")
    location = location.get_text().strip()
    # if company.find("a") is not None:
    #     company = company.find("a").string.replace("\n","")
    # else:
    #     company = company.string.replace("\n","")

    # location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
    # job_id = html["data-jk"]
    #
    # return {"title":title, "company":company, "location":location
    #         ,"link":f"https://kr.indeed.com/viewjob?jk={job_id}"}
    return {"title":title, "company":company,"location":location}



def get_jobs():
    last_page = extract_so_pages()
    jobs = extract_so_jobs(last_page)
    return jobs

print(get_jobs())