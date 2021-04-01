from selenium import webdriver
import time
import csv

csv_file_name = '낚시 채널 조황정보24.csv'

# 컬럼명
column_list = ['번호','카테고리','날짜','내용']

item_idx = 0 # 한 페이지내 글 목록 수 인덱스

# 결과 저장 리스트
result_list=[]

# 반복문 flag
flag =True

# csv 파일로 저장
with open(csv_file_name, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(column_list)  # 컬럼 설정

    # chromedriver로 브라우저 실행(낚시채널 조황정보)
    browser = webdriver.Chrome('/Users/KCG/DESKTOP/chromedriver')
    browser.get('https://www.eftv.co.kr/?m1=community%25&m2=information%25&pc_mode=%25')
    # browser.get('https://www.eftv.co.kr/?m1=community%25&m2=information%25&pc_mode=%25&page=202')
    browser.implicitly_wait(5)

    while(flag):
        try:
            # 1~10개 항목 불러오기
            if (item_idx !=10):
                # 현재 url
                # browser = browser.get(browser.current_url)
                # browser.implicitly_wait(5)

                tbody = browser.find_element_by_class_name('list')
                # 페이지 테이블 한 행 지정
                tr = tbody.find_elements_by_tag_name('tr')[item_idx]

                # 제목 지정(날짜와 카테고리를 가져오기 위함)
                title_link = tr.find_element_by_tag_name('span')

                # 번호,카테고리, 날짜 지정
                num = tr.find_element_by_tag_name('td')
                num_text = num.text
                # category = title_link.text.split('(')
                category = tr.find_elements_by_tag_name('td')[1]
                category_text=category.text
                date = title_link.text.split(' F')

                # 번호, 카테고리, 날짜 저장
                result_list.append(num_text)
                result_list.append(category_text)
                result_list.append(date[0])

                # 링크 클릭
                title_link.click()
                time.sleep(5)

                # 내용 출력
                content = browser.find_element_by_tag_name('td').text
                result_list.append(content)
                # print('content: ',content)

                print("번호: ", result_list[0])
                print(result_list)
                print("")

                # csv파일에 등록
                w.writerow(result_list)
                result_list=[] # 초기화

                # 브라우저 뒤로 가기
                browser.back()
                time.sleep(2)

                item_idx += 1  # 한 페이지 내 인덱스

                # 번호가 1이면 반복문 종료
                if (num_text == '1'):
                    flag = False
                    browser.close()

            # 다음 페이지 넘어가기 위함
            else:
                item_idx = 0
                print('다음페이지')
                print('')
                browser.find_element_by_xpath('//*[@id="pager_buttons"]/ul/li[8]/div/img').click()
                # browser.find_element_by_xpath('// *[ @ id = "pager_buttons"] / ul / li[8]').click()
                time.sleep(2)

        except:
            # item_idx-=1
            # browser.forward()
            # time.sleep(2)
            continue
