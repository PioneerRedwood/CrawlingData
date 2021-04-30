"""
1번째 분석
    가져온 브랜드 정보(6026개)와 전국 업종별 가게 리스트를 분석하여
    유효한 데이터를 추출 및 분석석는 것이 목적

2021.04.11. Note.
    아무래도 이름을 비교해서 분석하는 것은 맞지 않는 것 같다.
    6026개 중에 3907개만 전국에 실제 매장으로 등록됐다는건 말이 안된다. 단단히 잘못 됐다.

결과.
    3907개의 브랜드만. analysis_1th.csv
"""

import csv
import time

brands = []
with open('../정보공개서/2020_Company.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i == 0:
            i += 1
            continue
        else:
            brands.append(row[1])

with open('../정보공개서/2019_Company.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i == 0:
            i += 1
            continue
        else:
            brands.append(row[1])

print('브랜드수', len(brands))

total_list = []
store_name_list = []

# file_path = 'BigDataClass\Cities\\'
# cities = ['Busan', 'Chungbuk', 'Chungcheong', 'Daegeon', 'Daegu', 'Gangwon', 'Gwangju', 'Gyeongbuk',
#           'Gyeonggi', 'Gyeongnam', 'Incheon', 'Jeonbuk', 'Jeonnam', 'Sejong', 'Seoul', 'Ulsan']
#
# for city in cities:
#     path = file_path + city + '.csv'
#     with open(path, 'r', encoding='utf-8-sig') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             total_list.append(row)
#             store_name_list.append(row[1])
# with open('Total_City_Addresses.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     writer = csv.writer(f)
#     for row in total_list:
#         writer.writerow(row)

with open('../DeprecatedCSVs/Total_City_Addresses.csv', 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        total_list.append(row)
        store_name_list.append(row[1])

print(len(store_name_list))

exists = []
i = 0

past = time.time()
for brand in brands:
    temp_list = [brand, ]
    for store in store_name_list:
        if brand in store:
            i += 1
            temp_list.append(store)
            exists.append(temp_list)
            break

print(len(exists))
print('경과 시간: ', time.time() - past, '초')

with open('analysis_1th.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    for exist in exists:
        writer.writerow(exist)

print('complete')
