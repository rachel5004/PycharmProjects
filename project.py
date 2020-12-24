from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
page = 10
conn = sqlite3.connect('test.db')
c = conn.cursor()
def select_all(con):
    return con.execute("select * from restaurant").fetchall()

def select(name, con):
    q = "select * from restaurant where name = '%s'" % name
    exc = con.execute(q)
    return exc.fetchone()
def check_exists(name, con):
    if len(select(name, con)) > 0:
        return True
    else:
        return False

def add_count(name, con):
    q = "select * from restaurant where name = '%s'" % name
    exc = con.execute(q).fetchone()
    count = exc[2] + 1
    num = exc[0]
    q = "update restaurant set count=%d where num=%d" % (count, num)
    con.execute(q)


driver = webdriver.Chrome('C:/Users/USER/Downloads/chromedriver/chromedriver.exe')
driver.implicitly_wait(3)

url = "https://everytime.kr/login"
driver.get(url)

driver.find_element_by_name('userid').send_keys('rachel5004')
driver.find_element_by_name('password').send_keys('jj123100!!')
driver.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()


def title_collector(first_line):
    result = first_line.split(">")[1]
    if result.__contains__("(수캠)"):
        result = result.replace("(수캠)", "")
    elif result.__contains__("수캠)"):
        result = result.replace("수캠)", "")
    elif result.__contains__("수캠 )"):
        result = result.replace("수캠 )", "")
    elif result.__contains__("수캠"):
        result = result.replace("수캠", "")
    elif result.__contains__("운캠"):
        return "-1"
    else:
        return "-1"

    if result.__contains__("("):
        result = result.split("(")[0]
    elif result.__contains__("편의점") or len(result) == 0:
        return "-1"

    return result


for x in range(page):
    page = "https://everytime.kr/256368/p/" + str(x + 1)
    driver.get(page)
    sleep(0.3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all("a", {"class": "article"})

    for i in range(20):
        data = articles[i].p
        line = str(data).split("<br/>")
        title = title_collector(line[0])
        if check_exists(title, c):
            add_count(title, c)

list = select_all(c)
