import csv
import os

pages = []

with open('2020_PageDetail.csv', 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        pages.append(row)

headers = []
bodies = []

idx = 0
for page in pages:
    if idx % 2 == 0:
        headers.append(page)
    else:
        page_idx = 0
        temp = page
        for data in temp:
            if data == ' ':
                temp[page_idx] = '0'
            page_idx += 1
        bodies.append(temp)
    idx += 1

pages_2020 = []
pages_2019 = []

header_flag_2020 = False
header_flag_2019 = False

idx = 0
for header in headers:
    if '2020' in header[15]:
        if not header_flag_2020:
            pages_2020.append(header)
            header_flag_2020 = True
        pages_2020.append(bodies[idx])
        idx += 1
    elif '2019' in header[15]:
        if not header_flag_2019:
            pages_2019.append(header)
            header_flag_2019 = True
        pages_2019.append(bodies[idx])
        idx += 1

print('2020_ver_data: ', len(pages_2020), '2019_ver_data: ', len(pages_2019))

with open('정보공개서/2019_Company.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    for row in pages_2019:
        writer.writerow(row)

with open('정보공개서/2020_Company.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    for row in pages_2020:
        writer.writerow(row)

print(os.stat('정보공개서/2020_Company.csv').st_size)
print(os.stat('정보공개서/2019_Company.csv').st_size)

print('gracefully complete')
