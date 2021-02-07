import csv
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, send_file

app = Flask("final")
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

so = "https://stackoverflow.com/jobs?r=true&q="
wwr = "https://weworkremotely.com/remote-jobs/search?term="
ok = "https://remoteok.io/"

db = {}


# methods
def save_to_file(word,jobs):
    file = open(word+".csv", mode="w", encoding="UTF-8")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return


def SO_scrapper(word):
    so_jobs = []
    response = requests.get(so + word)
    results = BeautifulSoup(response.text, 'html.parser').find_all("div", {"class": "-job"})
    for result in results:
        job = SO_getinfo(result)
        so_jobs.append(job)
    return so_jobs


def WWR_scrapper(word):
    wwr_jobs = []
    response = requests.get(f"{wwr}/search?term={word}")
    results = BeautifulSoup(response.text, 'html.parser').find_all("li", {"class": "feature"})
    for result in results:
        job = WWR_getinfo(result)
        wwr_jobs.append(job)
    return wwr_jobs


def OK_scrapper(word):
    ok_jobs = []
    response = requests.get(f"{ok}remote-dev+{word}-jobs", headers=headers)
    results = BeautifulSoup(response.text, 'html.parser').find_all("tr", {"class": "job"})
    for result in results:
        job = OK_getinfo(result)
        ok_jobs.append(job)
    return ok_jobs


def SO_getinfo(result):
    title = result.find("h2", {"class": "mb4"})
    title_anchor = title.find("a")["title"]
    title = title_anchor
    company = result.find("h3", {"class": "fc-black-700"}).find("span")
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
    link = ok + result.find("a", {"itemprop": "url"})["href"]

    return {"title": title, "company": company, "link": link}


# html pages

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def result():
    word = request.args.get("term")
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = SO_scrapper(word) + WWR_scrapper(word) + OK_scrapper(word)
            db[word] = jobs
    return render_template('read.html',
                           searching_by=word,
                           resultNum=len(jobs),
                           results=jobs)


@app.route("/export")
def export():
    try:
        word = request.args.get('term')
        if not word:
            raise Exception()
        word = word.lower()
        results = db.get(word)
        if not results:
            raise Exception()
        save_to_file(word,results)
        return send_file(word+'.csv')
    except:
        return redirect("/")


# run
app.run(host="127.0.0.1", debug=True)
