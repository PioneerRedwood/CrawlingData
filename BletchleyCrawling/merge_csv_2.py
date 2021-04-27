"""
테마로 지정할 만한 특성들을 뽑아내서 하나의 csv 파일로 병합해야 한다.
특성
가맹점수, 가맹사업 개월수, 최근 2년 매출 증가율, 매출액, 창업비용, 개점률, 폐점률
보류: 굿프랜차이즈(필터링만 하는 걸로), 광고비

안정성 > 가맹점 수 많음, 폐점률 낮음, 장수브랜드
굿프렌차이즈, KFA 등록 브랜드 >
본사지원 > 광고비 (보류)
신규 회사 브랜드 > 법인설립 등기일 3년이내
떠오르는 브랜드 > 매출 증가율 상위 10%
가성비 > 창업비용, 평균 매출액
"""

import pandas as pd
import numpy as np

avgs = pd.read_csv('avgs.csv')
dataset = pd.read_csv('Analysis/2020_dataset.csv')

# print(np.array(dataset)[:, :2])
# print(avgs['최근 2년간 매출 증가율'])
avgs = avgs.drop('상호', axis=1)

# total_list = []

# avgs = sorted(avgs, key=lambda x: (x[0], x[1]))
# dataset = sorted(dataset, key=lambda x: (x[0], x[1]))

cnt = 0
for row in np.array(avgs)[:, :2]:
    for data in np.array(dataset)[:, :2]:
        if np.array_equal(row, data):
            cnt += 1
            arr = (dataset.loc[dataset['브랜드'] == data[1]].to_numpy()).tolist()
            print(dataset.loc[dataset['브랜드'] == data[1]])
            # arr.append(avgs.loc[avgs['브랜드'] == row[1]]['최근 2년간 매출 증가율'].to_numpy().tolist()[0])
            # print(arr)
# + )
            break

print(cnt)
print('complete')
