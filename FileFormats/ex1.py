"""
Вам дана частичная выборка из датасета зафиксированных преступлений,
совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv
"""

import csv
import time

count = {}

with open("Crimes.csv") as f:
    reader = csv.reader(f)
    skip = True
    for row in reader:
        date = row[2]
        if skip:
            skip = False
            continue
        if time.strptime(date, '%m/%d/%Y %I:%M:%S %p').tm_year == 2015:
            primaryType = row[5]
            if primaryType in count:
                count[primaryType] += 1
            else:
                count[primaryType] = 0
print(count)
