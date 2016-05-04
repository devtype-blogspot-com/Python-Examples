from random import random


class RandomIterator:
    def __init__(self, k):  # конструктор
        self.k = k
        self.i = 0

    def __next__(self):  # объект является итератором, когда у него есть данный метод
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration

    def __iter__(self):
        return self

x = RandomIterator(3)
print(next(x))  # next(x) ~ x.__next__()
print(next(x))
print(next(x))

for y in RandomIterator(10):
    print(y)
