"""
테마 만들기
    우선, 각 유효한 데이터인지 꺼내기
"""

import csv
import numpy as np

# 업종, 브랜드, 가맹사업 년수, 가맹점수, 가맹점평균매출액, 창업비용, 개점률, 폐점률
header = []
total_list = []
with open('2020_dataset.csv', 'r', encoding='utf-8-sig', newline='') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i == 0:
            i += 1
            header = row
            continue
        total_list.append(row)

max_list = [0, 0, 0, 0, 0, 0]
for row in total_list:
    arr = row[2:]
    for data in arr:
        idx = arr.index(data)
        if max_list[idx] < float(data):
            max_list[idx] = float(data)
print(max_list)

norm_list = []
for row in total_list:
    arr = row[2:]
    datas_ = []
    for data in arr:
        idx = arr.index(data)
        datas_.append(round(float(data) / max_list[idx], 6))

    norm_list.append(np.array(datas_))

print(header)
print(total_list[0])
print(norm_list[0])

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons

# x, y = make_moons(n_samples=300, noise=0.05, random_state=42)
df = pd.DataFrame(norm_list)


