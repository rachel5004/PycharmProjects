from flask import Flask, render_template, request, redirect
from Scrapper import get_so_jobs
app = Flask(__name__)
db = {}
# naver.com/reddit
#  ↳ 도메인    ↳주소
@app.route("/")   #주소값 라우팅
# def index():
#    args = {'title':'index page','contents':'hello world'}
#    return render_template('index.html',**args)

def home():
    return render_template('home.html')

# @app.route("/<username>")
# def welcome(username):
#     return f"hi {username} how are you"

@app.route("/report")   # welcome과 다르게 인자값x
def report():
    # /report?word=<>
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_so_jobs(word)
            db[word]= jobs
    else: return redirect("/")
    return render_template('report.html',
                           searching_by = word,
                           resultNum = len(jobs),
                           jobs = jobs)