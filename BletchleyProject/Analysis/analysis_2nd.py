"""
2번째 분석
    한번 뽑아낸 3907개의 브랜드가 전국에 몇개씩 있는지 찾아보기로 한다
결과
    총 123,736개의 가게. analysis_2nd.csv
"""

import csv
import time
past = time.time()

total_list = []
store_name_list = []

with open('Total_City_Addresses.csv', 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        total_list.append(row)
        store_name_list.append(row[1])

print(len(store_name_list))

equal_list = []
with open('analysis_1th.csv', 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        equal_list.append(row[0])

print(len(equal_list))

with open('analysis_2nd.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)

    specifics = []
    i = 0
    for equal in equal_list:
        for row in total_list:
            if equal in row[1]:
                i += 1
                if i % 500 == 0:
                    print(i, row)
                specifics.append(row)
    specifics.sort()

    for spec in specifics:
        writer.writerow(spec)

print('경과 시간: ', time.time() - past, '초')
print(len(specifics))
