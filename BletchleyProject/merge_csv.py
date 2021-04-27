"""
# 1. csv 레코드 다 읽어서 list로 가져오기 (중복은 없애야 함)
# 2. csv 파일 세 개 다 읽기
# 순서는 브랜드개요 -> 가맹점 현황 정보 -> 가맹점 창업 비용
# 3. 레코드 하나씩 읽어서 하나의 csv 파일로 묶기
"""

import csv
import os

list_1 = []
list_2 = []
list_3 = []

with open('DeprecatedCSVs/2020_BrandSummary.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for line in reader:
        list_1.append(line)

with open('DeprecatedCSVs/2020_FranchiseStatusInfo.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for line in reader:
        list_2.append(line)

with open('DeprecatedCSVs/2020_FranchiseFoundationCost.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for line in reader:
        list_3.append(line)

print(len(list_1))
print(len(list_2))
print(len(list_3))

for row1 in list_1:
    for row2 in list_2:
        if row1[1] == row2[1]:
            for i in range(3, len(row2)):
                row1.append(row2[i])
            break

for row1 in list_1:
    for row3 in list_3:
        if row1[1] == row3[1]:
            for i in range(3, len(row3)):
                row1.append(row3[i])
            break

with open('DeprecatedCSVs/2020_PublicInfo_TotalData.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    for line in list_1:
        writer.writerow(line)

print(os.stat('DeprecatedCSVs/2020_PublicInfo_TotalData.csv').st_size)
