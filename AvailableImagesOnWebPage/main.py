"""
Вам дана ссылка на HTML документ.
Посчитайте количество живых картинок в нем.

Живой картинкой назовем тег <img ... src="url" ... >, который отображается на странице, ﻿
в котором url ведет на страницу, при запросе которой сервер вернет сообщение с status code равным 200
и заголовком Content-Type, начинающимся с image (например image/png)

Пример живой картинки
<img src="https://stepic.org/media/attachments/lesson/25669/nya.png">

Sample Input:
https://stepic.org/media/attachments/lesson/25669/sample.html

Sample Output:
2

"""

import requests
import re

# page_url = input()
page_url = 'https://stepic.org/media/attachments/lesson/25669/sample.html'
res = requests.get(page_url)
images = re.findall(r"<img.*? src=\"(.+?)\".*?>", res.text.lower())
cnt = 0
for img_url in images:
    res = requests.get(img_url)
    if res.status_code == 200 and res.headers['Content-Type'].lower().startswith('image'):
        cnt += 1
print(cnt)
