"""
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов,
на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов,
которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть,
за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">﻿.

Сайты следует выводить в алфавитном порядке.

Пример HTML файла:

<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

Пример ответа:

mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru
"""

import requests
import re

f = open("test3.html", "r")  # открыть файл на чтение
data = f.read()
f.close()

# linkToHTMLFile = "https://stepic.org/media/attachments/lesson/24471/01"
# linkToHTMLFile = input()
# response = requests.get(linkToHTMLFile)
# if response.status_code == 200:
#     data = response.text

result = []
for link in re.findall(r"<a(.*?)href(.*?)=(.*?)(\"|')(((.*?):\/\/)|(\.\.)|)(.*?)(\/|:|\"|')(.*)", data):
    domain = link[8]
    if domain not in result:
        result.append(domain)

result.sort()

for domain in result:
    print(domain)
