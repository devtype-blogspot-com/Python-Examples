from functools import partial

x = int("1101", base=2)
print(x)  # 13

int_2 = partial(int, base=2)
x = int_2("1101")
print(x)  # 13

