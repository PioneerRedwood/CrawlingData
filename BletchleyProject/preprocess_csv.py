"""
csv 중복 제거
"""
import csv
import os
import time

total_list = []
start = time.time()


def delete_char(value):
    result = ''

    if ',' in value:
        arr = value.split(',')
        for data in arr:
            result += data
        return result
    else:
        return value


# valid_brand_list = []
# with open('DeprecatedCSVs/2020_PublicInfo_TotalData.csv', 'r', encoding='utf-8-sig') as f:
#     brand_name_list = []
#     reader = csv.reader(f)
#     i = 0
#     for row in reader:
#         if i == 0:
#             valid_brand_list.append(row)
#             i += 1
#             continue
#
#         if [row[1], row[2]] not in brand_name_list:
#             valid_brand_list.append(row)
#             brand_name_list.append([row[1], row[2]])
#
# print(len(valid_brand_list))
#
# with open('PublicInfo_TotalData.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     writer = csv.writer(f)
#     for row in valid_brand_list:
#         writer.writerow(row)

# with open('PublicInfo_TotalData.csv', 'r', encoding='utf-8-sig', newline='') as f:
#     reader = csv.reader(f)
#     i = 0
#     for row in reader:
#         # for debugging
#         if i == 0:
#             i += 1
#             continue
#
#         col_4 = 0
#         if row[4].split(' '):
#             arr = row[4].split(' ')
#             col_4 += int(arr[0][:1]) * 12
#             if '개' in arr[1][:2]:
#                 col_4 += int(arr[1][:1])
#             else:
#                 col_4 += int(arr[1][:2])
#
#         col_18 = ''
#         if '\n' in row[18]:
#             col_18 = row[18].split('\n')[0]
#
#         table_list = row[:4] + [str(col_4)] + row[5:7] + row[8:12] + \
#                           [delete_char(row[12]), delete_char(row[13]), delete_char(row[14]), delete_char(row[15]),
#                            delete_char(row[16]), delete_char(row[17]), delete_char(col_18), delete_char(row[19]),
#                            delete_char(row[20]), delete_char(row[21])]
#         # print(len(table_list), table_list)
#         total_list.append(table_list)


# 인덱스 추가해야 함
# 임직원 수도 int로 변형시켜야 함
with open('FinalBrandDetailData_2.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        i += 1
        table_list = list([i]) + row[:6] + [row[6].split('명')[0]] + row[7:]
        # print(len(table_list), table_list)
        total_list.append(table_list)

with open('FinalBrand.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    for row in total_list:
        writer.writerow(row)

print(i, len(total_list))
print('complete', 'Elapsed: ', time.time() - start)
