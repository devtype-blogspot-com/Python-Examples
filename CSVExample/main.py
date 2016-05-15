"""
Подходящим назовем файл, имеющий расширение .csv с данными в формате CSV внутри.
Интересным назовем подходящий файл, в заголовке данных которого есть атрибут Pet в любом регистре (pet, PET, pEt, ...)
Хорошим назовем интересный файл, в данных которого строк с атрибутом Pet равным Cat меньше чем строк
с атрибутом Pet равным Dog (слова pet, cat и dog могут быть в любом регистре).

Вам дана файловая структура. Найдите количество хороших файлов в ней.

Гарантируется, что любой файл с расширением .csv содержит данные в формате CSV.

Пример данных:
sample.zip

Пример ответа:
43

Основные данные:
data.zip
"""

import os
import os.path
import csv

cnt = 0
for current_dir, dirs, files in os.walk("data"):
    for file_name in files:
        if file_name.endswith(".csv"):
            with open(current_dir + "\\" + file_name) as f:
                reader = csv.reader(f)
                first_row = next(reader)
                col_idx = 0
                for field in first_row:
                    if field.lower() == "pet":
                        cats, dogs = 0, 0
                        for row in reader:
                            if row[col_idx].lower() == "dog":
                                dogs += 1
                            elif row[col_idx].lower() == "cat":
                                cats += 1
                        if cats < dogs:
                            cnt += 1
                        break
                    col_idx += 1
print(cnt)
