import csv
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, send_file
from Scrapper import SO_getinfo,WWR_getinfo,OK_getinfo

app = Flask("final")

so = "https://stackoverflow.com/jobs?r=true&q="
wwr = "https://weworkremotely.com/remote-jobs/search?term="
ok =  "https://remoteok.io/remote-dev+"
db={}

# methods
def save_to_file(jobs):
    file = open("job.csv", mode="w", encoding="UTF-8")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return

def SO_scrapper(word):
    so_jobs=[]
    response = requests.get(so+word)
    results = BeautifulSoup(response.text,'html.parser').find_all("div",{"class":"-job"})
    for result in results:
        job = SO_getinfo(result)
        so_jobs.append(job)
    return so_jobs


def WWR_scrapper(word):
    wwr_jobs =[]
    response = requests.get(wwr+word)
    results = BeautifulSoup(response.text,'html.parser').find_all("li")
    for result in results:
        job = SO_getinfo(result)
        wwr_jobs.append(job)
    return wwr_jobs

def OK_scrapper(word):
    response = requests.get(f"{ok}{word}-jobs")
    soup = BeautifulSoup(response.text,'html.parser')




# html pages

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def result():
    word = request.args.get("term")
    jobs =[]
    print(word)
    return render_template('result.html',
                           searching_by = word,
                           resultNum = len(jobs),
                           jobs = jobs)

@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        results = db.get(word)
        if not results:
            raise Exception()
        save_to_file(results)
        return send_file('jobs.csv')
    except: return redirect("/")



# run
# app.run(host="127.0.0.1")