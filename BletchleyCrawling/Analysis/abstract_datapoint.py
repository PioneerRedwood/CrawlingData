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
# 0, 1, 4, 5, 12, 18, 개, 폐점률

total_list = []
with open('..//PublicInfo_TotalData.csv', 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.reader(f)

    with open('datapoints.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)

        i = 0
        for row in reader:
            if i == 0:
                i += 1
                writer.writerow([row[0], row[1], '가맹사업 개월수', row[5], '평균매출액', '창업비용', '개점률', '폐점률'])
                continue

            # row[4]:가맹점수, [8]:신규개점, [9]:계약종료, [10]:계약해지
            # 개점률 = 신규 / 전체
            # 폐점률 = 종료 + 해지 / 전체
            temp_row = []
            datas = [row[5], row[8], row[9], row[10]]
            for data in datas:
                temp = ''
                if ',' in data:
                    for d in data.split(','):
                        temp += d
                else:
                    temp = data
                temp_row.append(int(temp))

            opening_rate = 0
            closing_rate = 0
            if temp_row[0] == 0:
                opening_rate = 0
            else:
                opening_rate = temp_row[1] / temp_row[0]

            if temp_row[0] == 0:
                closing_rate = 0
            else:
                closing_rate = temp_row[2] + temp_row[3] / temp_row[0]

            col_2 = 0
            if row[4].split(' '):
                arr = row[4].split(' ')
                col_2 += int(arr[0][:1]) * 12
                if '개' in arr[1][:2]:
                    col_2 += int(arr[1][:1])
                else:
                    col_2 += int(arr[1][:2])

            col_4 = ''
            if ',' in row[12]:
                arr = row[12].split(',')
                for i in range(len(arr)):
                    col_4 += arr[i]
            else:
                col_4 = 0

            col_5 = ''
            if '\n' in row[18]:
                arr = row[18].split('\n')[0]
                if ',' in arr:
                    temp = arr.split(',')
                    for i in range(len(temp)):
                        col_5 += temp[i]
            else:
                col_5 = 0

            writer.writerow([row[0], row[1], col_2, row[5], col_4, col_5,
                             round(opening_rate * 100, 2), round(closing_rate * 100, 2)])

print('complete')
