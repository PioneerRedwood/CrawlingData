"""
모든 테스트
"""

import csv
import time

start_time = time.time()
total_list = []

"""본부 구하기"""
# with open('FinalHQ.csv', 'r', encoding='utf-8-sig', newline='') as f:
#     reader = csv.reader(f)
#
#     for row in reader:
#         table_list = []
#         for data in row:
#             if ',' in data:
#                 table_list.append(data.replace(',', ''))
#             elif ' - ' in data:
#                 table_list.append(data.replace(' ', ''))
#             else:
#                 table_list.append(data)
#
#         total_list.append(table_list)
#
# with open('FinalHQ_.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     writer = csv.writer(f)
#
#     for row in total_list:
#         # print(len(row))
#         writer.writerow(row[:(len(row) - 1)])

"""가게 주소에 인덱스 부여"""
# with open('Analysis/Total_City_Addresses.csv', 'r', encoding='utf-8-sig', newline='') as f:
#     reader = csv.reader(f)
#     i = 0
#     for row in reader:
#         i += 1
#         total_list.append([i] + row)
# print('read done')
#
# with open('FinalAddress.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     writer = csv.writer(f)
#
#     for row in total_list:
#         writer.writerow(row)
# print('write done')

# with open('Analysis/population_2103.csv', 'r', encoding='utf-8-sig', newline='') as f:
#     reader = csv.reader(f)
#     i = 0
#     for row in reader:
#         if i == 0:
#             total_list.append(['si', 'gu', 'dong', 'population'])
#             i += 1
#             continue
#         arr = row[0].split(' ')
#         partial_list = [arr[0], arr[1], arr[2].split('(')[0].replace('제', ''), row[1]]
#         print(partial_list)
#         # total_list.append()

import pandas as pd
import numpy as np

# df = pd.read_csv('Analysis/population_2103_.csv')
# df[['행정구역', '인구수']].to_csv('Analysis/population_2103.csv')

# 행정구역, 인구수
with open('DeprecatedCSVs/population_2103_.csv', 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i == 0:
            total_list.append(['id', 'do', 'si(gu)', 'dong', 'population'])
            i += 1
            continue
        arr = row[0].split(' ')

        if len(arr) >= 3:
                dong = ''
                if len(arr) == 3:
                    if arr[2].split('(')[0]:
                        dong = arr[2].split('(')[0]
                        if '제' in dong:
                            dong = dong.replace('제', '')
                    sigu = arr[1]
                elif len(arr) == 4:
                    if arr[3].split('(')[0]:
                        dong = arr[3].split('(')[0]
                        if '제' in dong:
                            dong = dong.replace('제', '')
                    sigu = arr[1] + ' ' + arr[2]

                if dong != '':
                    partial_list = [i, arr[0], sigu, dong, row[1].replace(',', '')]
                    print(partial_list)
                    total_list.append(partial_list)
                    i += 1

        # 행정구역에 '제1동'으로 시작하는 행이 있어 '제'를 삭제해버린 행들
        # 하지만 유효한 데이터 마저 삭제하는 수 밖에 없었다.
        # if len(arr) == 3:
        #     if arr[2].split('(')[0]:
        #         dong = arr[2].split('(')[0]
        #         if '제' in dong:
        #             dong = dong.replace('제', '')
        #             print(dong)
        #
        # if len(arr) == 4:
        #     if arr[3].split('(')[0]:
        #         dong = arr[3].split('(')[0]
        #         if '제' in dong:
        #             dong = dong.replace('제', '')
        #             print(dong)



print('read done')

with open('FinalPopulation.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)

    for row in total_list:
        writer.writerow(row)
print('write done')

print('Elapsed: ', time.time() - start_time)
