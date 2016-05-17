"""
Ссылка на задачу 1: https://goo.gl/6dKeVN

Из генеральной совокупности получена выборка (1.08, 0.19, 0.14, 0.27, 0.10, 0.38, 0.14, 0.23, 0.14, 0.50).
Найдите значение выборочной функции распределения в точке 0.25.
Формат ответа: значение функции распределения с точностью не менее 1 знака после запятой
"""


# См. https://abstract-repr-sys.blogspot.com/2016/05/Vyborka-Vyborochnoe-prostranstvo.html
# Параграф "Эмпирическая вероятностная мера"
def empirical_distribution_foo(sample, x):
    sample.sort()
    if x <= sample[0]:
        return 0
    elif x > sample[-1]:
        return 1
    else:
        for i in range(1, len(sample)):
            if sample[i - 1] < x <= sample[i]:
                return i / len(sample)


def solution1():
    sample = [1.08, 0.19, 0.14, 0.27, 0.10, 0.38, 0.14, 0.23, 0.14, 0.50]
    x = 0.25
    val = empirical_distribution_foo(sample, x)
    return val

assert solution1(), 0.6

"""
Ссылка на задачу 2: https://goo.gl/ImxC0t

По предложенной выборке постройте выборочную функцию распределения.
Найдите значения выборочной функции распределения в точках  0.8, 4.3, 8.5, 15.0
Формат ответа: значения функции распределения с точностью до 2 знака указываются через запятую и пробел.
Sample Input: 20, 1, 6, 13, 6, 9, 3, 7, 15, 13
Sample Output: 0.0, 0.2, 0.5, 0.8
"""


def solution2(sample):
    answer = []
    for x in [0.8, 4.3, 8.5, 15.0]:
        val = empirical_distribution_foo(sample, x)
        answer.append(val)
    return answer

test1 = solution2([20, 1, 6, 13, 6, 9, 3, 7, 15, 13])
assert test1, [0.0, 0.2, 0.5, 0.8]

for file_name in ["dataset_26209_13.txt", "input2.txt", "input3.txt", "input4.txt", "input5.txt"]:
    with open(file_name) as f:
        for line in f:
            line = line.rstrip()
            lst = list(map(int, line.split(",")))
            print(lst, ":", solution2(lst))
