from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import csv
import os

origin_link = 'https://franchise.ftc.go.kr'

# 링크 주소(애초에 검색 내용(필터)이 담김)
link_str =\
    "https://franchise.ftc.go.kr/mnu/00013/program/userRqst/list.do?" \
    "searchCondition=&searchKeyword=&column=tNm&selUpjong=21&selIndus=&pageUnit=300&pageIndex="

# onclick='https://franchise.ftc.go.kr/mnu/00013/program/userRqst/view.do?firMstSn=78779'

link_list = []

delay = 0.5

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')

browser = webdriver.Chrome('chromedriver.exe', options=options)

with open('2020_상세페이지_링크리스트.csv', 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.reader(f)
    for line in reader:
        link_list.append(line[1])

table_list = []

for link in link_list:
    browser.get(link)
    time.sleep(delay)

    # 웹페이지 구조 분석
    # 여러 테이블, thead 태그가 있어도 안이 비어있는 경우도 있음
    # tr 안에 td 혹은 th가 들어있는 경우가 있음 어느 경우든 row 가져와야함
    # box_flop / table / tbody / tr / th 혹은 td
    # thead(요소 이름) 안에는 tr / th 방식으로 저장됨
    # get tables
    #     get thead - append
    #     get tbody
    #       get tr - append
    th_flag = False
    try:
        tables = browser.find_elements_by_tag_name('table')
        for table in tables:

            # get thead(th)
            if not th_flag:
                theads = table.find_elements_by_tag_name('thead')
                for thead in theads:
                    ths = []
                    for th in thead.find_elements_by_tag_name('th'):
                        if th != '':
                            ths.append(th.text)
                    print(ths)
                    table_list.append(ths)

            tds = []
            tbodies = table.find_elements_by_tag_name('tbody')
            #           get td
            for body in tbodies:
                for td in body.find_elements_by_tag_name('td'):
                    if td.text != '':
                        tds.append(td.text)
                print(tds)
            table_list.append(tds)

    except:
        print('error')

browser.quit()