"""
정보공개서 갱신 시기가 서로 다른 두 2020년, 2019년 csv 파일을 DB에 저장하기 위해 하나의 csv로 만든다.

2020년 2019년 테이블로 저장할 필요한 데이터 추출
    필요한 데이터 특성
        11개: id, 상호, 대표자, 법인 설립 등기일, 사업자 등록일, 대표번호, 대표 팩스 번호, 주소, 사업자 유형, 법인 등록 번호, 사업자 등록 번호
        18개 + 6개(병합을 위한 프리픽스): 2020년-2017년 (자산, 부채, 자본, 매출액, 영업이익, 당기순이익)
        9개 + 3개(병합을 위한 프리픽스): 2020년-2017년 (개점, 폐점(계약종료 + 계약해지), 명의변경)
        3개: 최근 3년간 법 위반 사실(공정거래위원회의 시정조치, 민사소송 패소 및 민사상 화해, 형의 선고)
    총 50개
"""
import csv
import time

# 2019년 원본
# 필요한 인덱스
# 상호,영업표지,대표자,업종,법인설립등기일,사업자등록일,대표번호,대표팩스 번호,등록번호,최초등록일,최종등록일,주소,사업자유형,법인등록번호,사업자등록번호,
# 2019년 자산,2019년 부채,2019년 자본,2019년 매출액,2019년 영업이익,2019년 당기순이익,2018년 자산,2018년 부채,2018년 자본,2018년 매출액,2018년 영업이익,2018년 당기순이익,2017년 자산,2017년 부채,2017년 자본,2017년 매출액,2017년 영업이익,2017년 당기순이익,
# 브랜드 수,가맹사업 계열사 수,가맹사업 개시일,2019년 신규개점,2019년 계약종료,2019년 계약해지,2019년 명의변경,2018년 신규개점,2018년 계약종료,2018년 계약해지,2018년 명의변경,2017년 신규개점,2017년 계약종료,2017년 계약해지,2017년 명의변경,
# "가맹지역본부(지사,지역총판)수", 형태,예치 가맹금,공정거래위원회의 시정조치,민사소송 패소 및 민사상 화해,형의 선고,가입비(가맹비),교육비,보증금,기타비용,합계,단위면적(3.3㎡)당 인테리어 비용,기준점포면적(㎡),인테리어 비용,최초 계약기간,연장 계약기간


start_time = time.time()

total_list = []
with open('정보공개서//2019_Company.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)

    i = 0
    for row in reader:
        if i == 0:
            i += 1
            table_list = [row[0], row[2]] + row[4:8] + row[11:15] \
                         + ['2020년 자산', '2020년 부채', '2020년 자본', '2020년 매출액', '2020년 영업이익', '2020년 당기순이익'] \
                         + row[15:33] \
                         + ['2020년 개점', '2020년 폐지', '2020년 명의변경', '2019년 개점', '2019년 폐지', '2019년 명의변경'] \
                         + ['2018년 개점', '2018년 폐지', '2018년 명의변경', '2017년 개점', '2017년 폐지', '2017년 명의변경'] \
                         + row[51:54]
            total_list.append(table_list)
            # print(len(table_list), table_list)
            continue

        # 36(2019 신규) 37+38(폐지) 39(명의변경)
        partial_list = [row[36], int(row[37]) + int(row[38]), row[39],
                        row[40], int(row[41]) + int(row[42]), row[43],
                        row[44], int(row[45]) + int(row[46]), row[47]]

        table_list = [row[0], row[2]] + row[4:8] + row[11:15] \
                     + ['0', '0', '0', '0', '0', '0'] \
                     + row[15:33] \
                     + ['0', '0', '0'] \
                     + partial_list + row[51:54]
        total_list.append(table_list)


with open('정보공개서//2020_Company.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)

    i = 0
    for row in reader:
        if i == 0:
            i += 1
            continue

        # 36(2020년 신규) 37+38(폐지) 39(명의변경)
        partial_list = [row[36], int(row[37]) + int(row[38]), row[39],
                        row[40], int(row[41]) + int(row[42]), row[43],
                        row[44], int(row[45]) + int(row[46]), row[47]]

        table_list = [row[0], row[2]] + row[4:8] + row[11:15] \
                     + row[15:33] \
                     + ['0', '0', '0', '0', '0', '0'] \
                     + partial_list \
                     + ['0', '0', '0'] \
                     + row[51:54]
        total_list.append(table_list)


with open('FinalHQ.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)

    i = 0
    for row in total_list:
        if i == 0:
            i += 1
            continue
        writer.writerow([i] + row)
        i += 1

# 위에서 한 작업에서 앞에 인덱스를 넣어둠
# with open('FinalHQ.csv', 'r', encoding='utf-8-sig', newline='') as f:
#     reader = csv.reader(f)
#
#     i = 0
#     for row in reader:
#         if i == 0:
#             i += 1
#             continue
#         total_list.append([i] + row)
#         i += 1
#
# with open('FinalHQ_.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     writer = csv.writer(f)
#
#     for row in total_list:
#         writer.writerow(row)

print('complete', 'Elapsed: ', time.time() - start_time)
