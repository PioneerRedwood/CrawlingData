# csv 중복 제거
import csv
import os

oldList = []
newList = []

with open('2020_brand_03.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for line in reader:
        oldList.append(line)

with open('2020_가맹점현황정보.csv', 'w', encoding='utf-8-sig', newline='') as new_f:
    writer = csv.writer(new_f)
    for line in oldList:
        if line not in newList:
            newList.append(line)
            writer.writerow(line)

print(os.stat('2020_brand_03.csv').st_size)
print(os.stat('2020_가맹점현황정보.csv').st_size)

