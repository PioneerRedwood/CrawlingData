"""
Multi class classification (다수 클래스를 분류 알고리즘)

    [중요 용어]
        datapoint:  프랜차이즈 정보
        feature:    프랜차이즈마다 존재하는 특성
    [프로세스]
        다수의 프랜차이즈 정보에서 정해진 테마(10개 이하)
"""
import csv
# 업종,브랜드,상호,가맹사업 개시일,가맹사업 년수,가맹점수,가맹본부 임직원수,가맹점수,신규개점,계약종료,계약해지,명의변경,"가맹점평균매출액","가맹점면적(3.3㎡)당평균매출액","가입비(가맹비)",교육비,보증금,"기타비용(인테리어비용포함)","합계(창업비용지수)","면적당(3.3㎡)비용","기준면적(㎡)",총 비용
# 0,    1, 	2,	3,	4,	   5,	  6, 		7,        8,		9,   10,       11,           12,		13,			14,	  15,      16,	17		18,			19,	20,	 21

# 업종, 브랜드, 가맹사업 년수, 가맹점수, 가맹점평균매출액, 창업비용, 개점률, 폐점률
from openpyxl.styles.builtins import total

total_list = []
with open('2020_dataset.csv', 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i == 0:
            i += 1
            continue
        total_list.append(row)

print('read complete')

with open('2020_dataset.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    i = 0
    for row in total_list:
        if i == 0:
            writer.writerow(row)
            i += 1
            continue

        col_5 = ''
        if row[5].split('\r')[0]:
            col_5 = int(row[5])

        writer.writerow([row[:5] + [col_5] + row[6:]])

# print(total_list[0])
print('complete')
