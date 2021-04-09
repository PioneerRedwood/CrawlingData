# 빅데이터 수업 과제 #1_2

import urllib.request
import urllib.parse
import pandas as pd
import json
import csv
import sys

# encoding key: 082IXMgEK76EbJN0NWoc9ot0TlEve7XfjwBNrsFMZoEdwgYBVExzKsbb6FGVXw9lWYlwqdtMKV%2BvOLwegs150w%3D%3D

url = "http://apis.data.go.kr/B553077/api/open/sdsc/storeListInDong"
# param
# divId: 시도는 ctprvnCd / 시군구는 signguCd / 행정동은 adongCd
# key: 시도는 시도코드값, 시군구는 시군구코드값, 행정동은 행정동코드값 사용
# indsLclsCd: 상권 업종 대분류 코드 (Q: 음식) - 고정
# indsMclsCd: 상권 업종 중분류 코드, *중분류 참고

# 아래는 테스트용
# params = \
#         '?divId=' + 'ctprvnCd' \
#         + '&key=' + str(11) \
#         + '&ServiceKey=' + '082IXMgEK76EbJN0NWoc9ot0TlEve7XfjwBNrsFMZoEdwgYBVExzKsbb6FGVXw9lWYlwqdtMKV%2BvOLwegs150w%3D%3D' \
#         + '&indsLclsCd=Q' \
#         + '&indsMclsCd=Q11' \
#         + '&numOfRows=1' \
#         + '&type=json'
#
# request = urllib.request.Request(url + params)
# request.method = 'GET'
# response = urllib.request.urlopen(request)
#
# result = response.getcode()
# if result == 200:
#     response_body = response.read().decode('utf-8')
#     items = json.loads(response_body)['body']['items']
#     for item in items:
#         print(item['indsMclsNm'])

"""
중분류 
    Q01:한식, 02:중식, 03:일식/수산물, 04:분식, 05:닭/오리요리, 06:양식, 07:패스트푸드, 08:제과제빵떡케익
    Q09:유흥주점, 10:별식/퓨전요리, 11:데이터 없음, 12:커피점/카페, 13:음식배달서비스, 14:기타음식점, 15:부페, 16이후 없음
"""
sector_dic = {'한식': 'Q01', '중식': 'Q02', '일식': 'Q03', '분식': 'Q04', '닭/오리요리': 'Q05', '양식': 'Q06', '패스트푸드': 'Q07',
              '제과제빵떡케익': 'Q08', '카페': 'Q12', '기타음식점': 'Q14'}

"""
시도 행정 코드 리스트
"""

city_dic = {'강원': '42', '경기': '41', '경남': '48', '경북': '47', '광주': '29', '대구': '27', '대전': '30', '부산': '26', '서울': '11',
            '세종': '36', '울산': '31', '인천': '28',
            '전남': '46', '전북': '45', '제주': '50', '충청': '44', '충북': '43'}
key = '41'

# define flow 도시 -> 업종 -> 페이지 수만큼
total = 0
total_list = []

with open('Gyeonggi.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)

    for sector in sector_dic:
        print(sector)

        # totalCount를 알아내기 위한 첫 페이지 크롤링
        count = 0
        params = \
            '?divId=' + 'ctprvnCd' \
            + '&ServiceKey=' + '082IXMgEK76EbJN0NWoc9ot0TlEve7XfjwBNrsFMZoEdwgYBVExzKsbb6FGVXw9lWYlwqdtMKV%2BvOLwegs150w%3D%3D' \
            + '&indsLclsCd=Q' \
            + '&numOfRows=100' \
            + '&type=json' \
            + '&key=' + key \
            + '&indsMclsCd=' + sector_dic[sector]

        request = urllib.request.Request(url + params)
        request.method = 'GET'
        response = urllib.request.urlopen(request)

        result = response.getcode()
        idx = 0
        if result == 200:
            response_body = response.read().decode('utf-8')

            items = json.loads(response_body)['body']['items']

            count = json.loads(response_body)['body']['totalCount']

            table_row = []
            for item in items:
                idx += 1
                table_row.append(item['indsMclsNm'])
                table_row.append(item['bizesNm'])
                table_row.append(item['ctprvnNm'])
                table_row.append(item['signguNm'])
                table_row.append(item['adongNm'])
                table_row.append(item['lon'])
                table_row.append(item['lat'])

                if idx % 100 == 0:
                    print('executing', '.' * int(idx / 500), idx, table_row)

                total_list.append(table_row)
                writer.writerow(table_row)
                table_row = []

        print(count)
        # 알아낸 카운트 수 - 1만큼 크롤링
        for i in range(2, int(count / 100) + 2):
            params = \
                '?divId=' + 'ctprvnCd' \
                + '&ServiceKey=' + '082IXMgEK76EbJN0NWoc9ot0TlEve7XfjwBNrsFMZoEdwgYBVExzKsbb6FGVXw9lWYlwqdtMKV%2BvOLwegs150w%3D%3D' \
                + '&indsLclsCd=Q' \
                + '&numOfRows=100' \
                + '&type=json' \
                + '&key=' + key \
                + '&indsMclsCd=' + sector_dic[sector] \
                + '&pageNo=' + str(i)

            request = urllib.request.Request(url + params)
            request.method = 'GET'
            response = urllib.request.urlopen(request)

            result = response.getcode()
            if result == 200:
                response_body = response.read().decode('utf-8')

                items = json.loads(response_body)['body']['items']

                table_row = []
                for item in items:
                    idx += 1
                    table_row.append(item['indsMclsNm'])
                    table_row.append(item['bizesNm'])
                    table_row.append(item['ctprvnNm'])
                    table_row.append(item['signguNm'])
                    table_row.append(item['adongNm'])
                    table_row.append(item['lon'])
                    table_row.append(item['lat'])

                    if idx % 500 == 0:
                        print('실행 중', '.' * int(idx / 500), idx, table_row[1])

                    total_list.append(table_row)
                    writer.writerow(table_row)
                    table_row = []

print(len(total_list))
print('completed', total)
