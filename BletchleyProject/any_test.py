"""
모든 테스트
"""

import csv
import time

total_list = []
with open('FinalHQ.csv', 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.reader(f)

    for row in reader:
        table_list = []
        for data in row:
            if ',' in data:
                table_list.append(data.replace(',', ''))
            elif ' - ' in data:
                table_list.append(data.replace(' ', ''))
            else:
                table_list.append(data)

        total_list.append(table_list)

with open('FinalHQ_.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)

    for row in total_list:
        # print(len(row))
        writer.writerow(row[:(len(row) - 1)])
