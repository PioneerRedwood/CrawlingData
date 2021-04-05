from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
# from selenium.webdriver.support.select import Select
import time
import csv
import os

# origin_link = 'https://franchise.ftc.go.kr'
# link = 'https://franchise.ftc.go.kr/mnu/00013/program/userRqst/view.do?firMstSn=100480'

delay = 0.5
timeout = 3

browser = webdriver.Chrome('chromedriver.exe')

link_list = []

# 갱신 필요 - 꽤 상세 페이지 목록은 꽤 자주 바뀜 2021.04.05 월 최신화
with open('2020_정보공개서_상세.csv', 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.reader(f)
    idx = 0
    for line in reader:
        if idx == 0:
            print(line)
            idx += 1
        else:
            link_list.append(line[6])

header_list = []
table_list = []
with open('2020_정보공개서_상세열람_#1.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)

    flag = False
    for link in link_list[0:500]:
        browser.get(link)
        time.sleep(delay)
        try:
            # tables = WebDriverWait(browser, timeout).until(lambda x: x.find_elements_by_tag_name('table'))
            tables = browser.find_elements_by_tag_name('table')
            time.sleep(delay)

            # data header
            if not flag:
                ths = []
                table_idx = 0
                for table in tables:

                    # table#3, 6, 8, 10 skip
                    if table_idx == 3 or table_idx == 6 or table_idx == 8 or table_idx == 10:
                        table_idx += 1
                        continue

                    # table#16 가맹계약 기간
                    if table_idx == 15:
                        trs = table.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
                        for tr in trs:
                            if tr == trs[1]:
                                for th in tr.find_elements_by_tag_name('th'):
                                    if th.text != '':
                                        ths.append(th.text + ' 계약기간')
                        continue

                    # table#7 가맹점 변동 현황
                    # thead 있고 tbody 빈거 하나 tbody 하나 더
                    if table_idx == 7:
                        temp_list = []
                        for th in table.find_element_by_tag_name('thead').find_elements_by_tag_name('th'):
                            if th.text != '' and '연도' not in th.text:
                                temp_list.append(th.text)
                        tbody = table.find_elements_by_tag_name('tbody')[1]
                        trs = tbody.find_elements_by_tag_name('tr')
                        for tr in trs:
                            for temp in temp_list:
                                ths.append(tr.find_elements_by_tag_name('td')[0].text + '년 ' + temp)
                        table_idx += 1
                        continue

                    # from thead
                    theads = table.find_elements_by_tag_name('thead')
                    for thead in theads:
                        trs = thead.find_elements_by_tag_name('tr')
                        for tr in trs:
                            for th in tr.find_elements_by_tag_name('th'):
                                if th.text != '':
                                    ths.append(th.text)

                    # from tbody
                    tbody_ths = table.find_elements_by_tag_name('tbody')
                    for tbody in tbody_ths:
                        trs = tbody.find_elements_by_tag_name('tr')

                        # table#2(가맹본부 재무상황)
                        if table_idx == 2:
                            temp_list = []
                            for tr in trs:
                                if tr == trs[0]:
                                    for th in tr.find_elements_by_tag_name('th'):
                                        if th != tr.find_elements_by_tag_name('th')[0]:
                                            temp_list.append(th.text)
                                else:
                                    for temp in temp_list:
                                        ths.append(tr.find_elements_by_tag_name('td')[0].text + '년 ' + temp)
                        else:
                            for tr in trs:
                                for th in tr.find_elements_by_tag_name('th'):
                                    if th.text != '':
                                        ths.append(th.text)

                    table_idx += 1
                if len(ths) > 0 and ths not in header_list:
                    header_list.append(ths)
                    print(len(ths), ths)
                    writer.writerow(ths)
                    flag = True

            # data
            tds = []
            table_idx = 0
            for table in tables:
                if table_idx == 3 or table_idx == 6 or table_idx == 8 or table_idx == 10:
                    table_idx += 1
                    continue
                for tbody in table.find_elements_by_tag_name('tbody'):
                    for tr in tbody.find_elements_by_tag_name('tr'):
                        list_td = tr.find_elements_by_tag_name('td')
                        for td in list_td:
                            if table_idx == 2 or table_idx == 7:
                                if td == list_td[0]:
                                    continue
                                else:
                                    if td.text != '':
                                        tds.append(td.text)
                            else:
                                if td.text != '':
                                    tds.append(td.text)
                table_idx += 1

            if len(tds) > 0:
                print(len(tds), tds)
                writer.writerow(tds)
            table_list = []

        except NoSuchElementException:
            print('exception: There is no such element..')
        except TimeoutError:
            print('exception: timeout..')

    browser.quit()
print('complete')
