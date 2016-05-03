import itertools


def primes():
    i = 2
    while True:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            yield i
        i += 1

gen = primes()
t = next(gen)
print(t)
t = next(gen)
print(t)

print(list(itertools.takewhile(lambda x: x <= 31, primes())))
#  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


