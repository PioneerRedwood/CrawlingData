from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
# from selenium.webdriver.support.select import Select
import time
import csv
import os

lines = []

with open('2020_PageDetail_#1.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for line in reader:
        lines.append(line)

for line in lines:
    if len(line) < 64:
        print(len(line), line)


print('complete')
