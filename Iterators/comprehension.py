x = [-2, -1, 0, 1, 2]

y = []
for i in x:
    y.append(i * i)

g = [i * i for i in x]
print(g)  # [4, 1, 0, 1, 4]

w = [i * i for i in x if i > 0]
print(w)  # [1, 4]

z = [(u, o) for u in range(3) for o in range(3) if o >= u]
print(z)  # [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]

# генератор
v = ((u, o) for u in range(3) for o in range(3) if o >= u)
print(v)  # <generator object <genexpr> at 0x01124360>
print(next(v))  # (0, 0)
