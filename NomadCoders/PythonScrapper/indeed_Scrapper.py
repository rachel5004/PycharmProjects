import requests
from bs4 import BeautifulSoup

limit = 50
url = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit={limit}&sort=&psf=advsrch&from=advancedsearch"


def extract_indeed_pages():
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.select_one("ul.pagination-list")
    pages = pagination.select('li > a > span')

    spans = []
    for page in pages[:-1]:
        spans.append(int(page.get_text()))
    max_page = spans[-1]
    return max_page


def extract_indeed_jobs(last_page):
    jobs = []
    for n in range(last_page):
        print(f"Scrapping Indeed: page {n+1}...")
        # {url}&start=게시물의 시작넘버 : 첫페이지=0 둘째페이지=50...
        result = requests.get(f"{url}&start={n * limit}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
        #print(results)
        for result in results:
            job = extract_jobinfo(result)
            jobs.append(job)
    return jobs


def extract_jobinfo(html):
    title = html.find("h2", {"class": "title"})
    title_anchor = title.find("a")["title"]
    title = title_anchor

    company = html.find("span", {"class": "company"})
    # 회사명이 a 태그 안에 존재하지 않는 케이스도 있음
    if company.find("a") is not None:
        company = company.find("a").string.replace("\n","")
    else:
        company = company.string.replace("\n","")

    # <div class="recJobLoc" data-rc-loc="location">
    location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]

    return {"title":title, "company":company, "location":location
            ,"link":f"https://kr.indeed.com/viewjob?jk={job_id}"}


def get_indeed_jobs():
    last_page = extract_indeed_pages()
    jobs = extract_indeed_jobs(last_page)
    return jobs
