"""
3번째 분석
    analysis_2nd.csv 를 분석해서 업종 별로 파일을 나눠 저장한다
"""

import csv
import time

past = time.time()
file_names = []
total_list = []
with open('analysis_2nd.csv', 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        total_list.append(row)
        temp = row[0]
        if '/' in temp:
            temp = temp.split('/')[0]

        if [temp, temp + '.csv'] not in file_names:
            pair = [temp, temp + '.csv']
            print(pair)
            file_names.append(pair)

print(len(file_names), len(total_list))

for file_name in file_names:
    with open(file_name[1], 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        print(file_name[0])
        i = 0
        for row in total_list:
            temp = row[0]
            if '/' in row[0]:
                temp = row[0].split('/')[0]
            if temp == file_name[0]:
                i += 1
                if i % 500 == 0:
                    print(i, row)
                writer.writerow(row)

print('경과시간:', time.time() - past, 'complete')