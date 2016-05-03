import operator as op

print(op.add(4, 5))  # 9
print(op.mul(4, 5))  # 20
print(op.contains([1, 2, 3], 4))  # False


# достать элемент коллекции

x = [1, 2, 3]
f = op.itemgetter(1)  # f(x) == x[1]
print(f(x))  # 2

y = {"123": 3}
g = op.itemgetter("123")
print(g(y))  # 3


# достать атрибут объекта
p = op.attrgetter("sort")  # p(x) == x.sort
print(p([]))  # <built-in method sort of list object at 0x013144B8>
