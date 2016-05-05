"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa﻿
"""


# s, t = input(), input()

s, t = "aaaaa", "a"
# s, t = "abc", "abc"
# s, t = "abababa", "abc"
# s, t = "abababa", "aba"

cnt = 0
pos = 0
while True:
    idx = s[pos:].find(t)
    if idx != -1:
        cnt += 1
        pos += idx + 1
    else:
        break
print(cnt)

