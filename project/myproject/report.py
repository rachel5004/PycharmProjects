# 서론
# 앞서 기획에서는 파이썬을 이용해 '에브리타임' 어플의 맛집 게시판을 보완해 웹형식으로 만들 계획이었지만 편의상 몇 부분 수정을 거쳐 크롤링을 이용한 학교 인근 맛집 지도로 변경했다.
# 에브리타임은 로그인 및 학교 인증 과정을 거치지 않고는 게시글을 열람할 수 없기 때문에 webdriver를 통한 로그인과정이 없으면 데이터 추출에 다소 어려움이 따랐다.
# 때문에 타겟 페이지를 에브리타임에서 맛집사이트로 변경해 크롤링 및 맵핑을 진행하기로 했다.
# 과정
# 구글에 '성신여대 맛집'을 검색, 상위에 노출된 사이트 중 임의로 하나를 선택
# beautifulsoup로 크롤링
# 추출된 데이터 정렬
# folium에 맵핑
# main
# target site='다이닝코드'
# key word='성신여대'
# range=10


import io
import sys
import folium
from PyQt5 import QtWidgets, QtWebEngineWidgets
import os
from wordcloud import WordCloud
import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import numpy as np
import pandas as pd
from folium.plugins import MarkerCluster

search = '성신여대'  # 검색 키워드

url = 'https://www.diningcode.com/list.php?query=' + search

html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")

name = soup.find_all("span", attrs={"class": "btxt"})  # 상호명
menu = soup.find_all("span", attrs={"class": "stxt"})  # 메뉴
location = soup.find_all("span", attrs={"class": "ctxt"})  # 위치

nameres = []
for line1, line2, line3 in zip(name, menu, location[1::2]):
    print(line1.get_text(), end=': ')
    print(line2.get_text())
    print('위치: ', line3.get_text())
    nameres.append(line1.get_text()[3:])

# loca =['37.5910124,127.0170043','37.5921226,127.01504','37.5913354,127.0133764','37.590755,127.0154852','37.5906042,127.0162113','37.5907238,126.9483591','37.5894357,127.0175803','37.5908077,127.0148182','37.5937945,127.016436']
# data = dict(zip(nameres,loca))


data = [
    {"store": "윤휘식당", "loc": [37.5910124, 127.0170043]}, {"store": "애정마라샹궈", "loc": [37.5921226, 127.01504]},
    {"store": "문화식당", "loc": [37.5913354, 127.0133764]}, {"store": "태조 감자국", "loc": [37.590755, 127.0154852]},
    {"store": "버거파크", "loc": [37.5906042, 127.0162113]}, {"store": "이자와", "loc": [37.5907238, 126.9483591]},
    {"store": "팔백집", "loc": [37.5894357, 127.0175803]}, {"store": "상미규카츠", "loc": [37.5908077, 127.0148182]},
    {"store": "제순식당", "loc": [37.5917719, 127.0161304]}, {"store": "김통", "loc": [37.5937945, 127.016436]}
]

map_osm = folium.Map(location=[37.5917052, 127.0161233], zoom_start=18)  # 지도
marker_cluster = MarkerCluster().add_to(map_osm)

for i in range(len(data)):
    folium.Marker(
        location=data[i]['loc'],
        popup=data[i]['store'],
        icon=folium.Icon(color='red', icon='ok'),
    ).add_to(marker_cluster)

map_osm.save('map.html')
