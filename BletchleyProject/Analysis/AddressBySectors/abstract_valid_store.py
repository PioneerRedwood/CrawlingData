"""
FinalBrand.csv에 속하지 않는 모든 가게(store)를 제거하고 유효한(valid) 것을 추출(abstract)한다.

"""

import csv
import time

start_time = time.time()

# brand_list = []
# with open('../../FinalBrand.csv', 'r', encoding='utf-8-sig', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         brand_list.append(row[2])

# ['기타음식점', '분식', '양식', '일식', '제과제빵떡케익', '중식', '커피점', '패스트푸드', '한식']
# sector = '한식'
# store_list = []
# with open(sector + '.csv', 'r', encoding='utf-8-sig', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         store_list.append(row)
#
# total_list = []
# i = 0
# for store in store_list:
#     for brand in brand_list:
#         if brand.__contains__(store[1]) or store.__contains__(brand):
#             i += 1
#             if i >= 1000:
#                 i = 0
#                 print([sector] + store[1:])
#             total_list.append([sector] + store[1:])
#
# with open('KoreanStoreAddress.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     writer = csv.writer(f)
#     for row in total_list:
#         writer.writerow(row)

total_list = []
comp_list = []
sectors = ['Korean', 'Chinese', 'Japanese', 'Occidental', 'Coffee', 'Etc', 'Fastfood', 'Snack', 'Chicken', 'Bread']
for sector in sectors:
    with open(sector + 'StoreAddress.csv', 'r', encoding='utf-8-sig', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1:] not in comp_list:
                comp_list.append(row[1:])
                total_list.append(row)
    print(sector, len(total_list))

print('read done')
total_list.sort(key=lambda x: [x[0], x[1]])

with open('FinalStoreAddress.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    for row in total_list:
        writer.writerow(row)

print('Elapsed: ', time.time() - start_time)
