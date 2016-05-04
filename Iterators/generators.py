from random import random


def random_generator(k):
    for i in range(k):
        yield random()
gen = random_generator(3)
print(type(gen))
for i in gen:
    print(i)
