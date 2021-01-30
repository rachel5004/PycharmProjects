import sys

import requests
from bs4 import BeautifulSoup
# limit = 50
# url = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit={limit}&sort=&psf=advsrch&from=advancedsearch"
#
#
# def extract_indeed_pages():
#     result = requests.get(url)
#     soup = BeautifulSoup(result.text, "html.parser")
#
#     pagination = soup.select_one("ul.pagination-list")
#     pages = pagination.select('li > a > span')
#
#     spans = []
#     for page in pages[:-1]:
#         spans.append(int(page.get_text()))
#     max_page = spans[-1]
#     return max_page
#
#
# def extract_indeed_jobs(last_page):
#     jobs = []
#     for n in range(last_page):
#         result = requests.get(f"{url}start={n * limit}")
#         soup = BeautifulSoup(result.text, "html.parser")
#         print(result.status_code)
#     return jobs
#
# last_indeed_page = extract_indeed_pages()
# extract_indeed_jobs(last_indeed_page)

strlst = ["str"]
print(strlst[0].__str__())
