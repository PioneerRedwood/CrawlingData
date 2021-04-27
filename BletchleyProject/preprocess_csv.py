"""
csv 중복 제거
"""
import csv
import os


valid_brand_list = []
with open('DeprecatedCSVs/2020_PublicInfo_TotalData.csv', 'r', encoding='utf-8-sig') as f:
    brand_name_list = []
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i == 0:
            valid_brand_list.append(row)
            i += 1
            continue

        if [row[1], row[2]] not in brand_name_list:
            valid_brand_list.append(row)
            brand_name_list.append([row[1], row[2]])

print(len(valid_brand_list))

with open('PublicInfo_TotalData.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    for row in valid_brand_list:
        writer.writerow(row)

print('complete')
