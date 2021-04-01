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

browser = webdriver.Chrome('chromedriver.exe')

with open('2020_상세페이지_링크리스트.csv', 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.reader(f)
    for line in reader:
        link_list.append(line[1])

for link in link_list:
    browser.get(link)
    time.sleep(delay)

    # 웹페이지 구조 분석
    # 여러 테이블, thead 태그가 있어도 안이 비어있는 경우도 있음
    # tr 안에 td 혹은 th가 들어있는 경우가 있음 어느 경우든 row 가져와야함
    # get tables
    #     get thead - append
    #     get tbody
    #       get tr - append
    try:

        tables = browser.find_elements_by_tag_name('table')
        for table in tables:
            ths = table.find_elements_by_xpath('.//th[@scope="col"]')
            for th in ths:
                print(th.text)

    except:
        print('error')

    # for value in range(1, 22):
    #     # 이동
    #     browser.get(link_str + str(value))
    #     time.sleep(delay)
    #
    #     tbody = browser.find_element_by_tag_name('table').find_element_by_tag_name('tbody')
    #
    #     try:
    #         trs = tbody.find_elements_by_tag_name('tr')
    #
    #         i = 0
    #         for tr in trs:
    #             name = tr.find_elements_by_tag_name('td')[2].text
    #             link = tr.find_elements_by_tag_name('td')[1]\
    #                 .find_elements_by_xpath('//a[@class="authCtrl"]')[i].get_attribute('onclick')
    #             i += 2
    #             table_list.append(name)
    #             table_list.append(origin_link + link[9:len(link)-3])
    #
    #             # writer.writerow(table_list)
    #             print(table_list)
    #             table_list = []
    #
    #     except:
    #         print('error')
