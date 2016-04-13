'''
Реализуйте программу, которая будет вычислять количество различных объектов в списке.
Два объекта a и b считаются различными, если a is b равно False.

Вашей программе доступна переменная с названием objects, которая ссылается на список, содержащий не более 100 объектов. Выведите количество различных объектов в этом списке.

Формат ожидаемой программы:﻿

ans = 0
for obj in objects: # доступная переменная objects
    ans += 1

print(ans)
'''

one = 1
two = 2
three = 3
four = 4
five = 5
objects = [one, two, three, four, five, one, two]

uniqueObjects = []
for obj in objects:
    isAdd = True
    for unique in uniqueObjects:
        if unique is obj:
            isAdd = False
    if isAdd:
        uniqueObjects.append(obj)

ans = 0
for obj in uniqueObjects: 
    ans += 1
print(ans)
