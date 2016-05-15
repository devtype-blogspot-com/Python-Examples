

# Класс, представляющий собой структуру данных,
# которая позволяет осуществлять следующие операции с точками из пространства Z^k
class Points:
    def __init__(self, k):
        # k -- размерность пространства
        self.k = k
        self.arr = []

    # добавить точку
    def add(self, *coords):
        # Принимает k целых чисел, i-е из которых соответствует i-й координате добавляемой точки.
        self.arr.append(coords)

    # удалить точку
    def remove(self, *coords):
        # Принимает то же, что и add.
        # В случае, если точек с такими координатами несколько, удаляется только одна из них.
        # В случае, если точек с такими координатами нет, никакая точка не удаляется.
        for point in self.arr:
            if point == coords:
                self.arr.remove(point)
                break

    # запросить точки из гиперпрямоугольника
    def range_query(self, *coord_ranges):
        # Принимает k кортежей из двух целых чисел a[i], b[i] (a[i] ≤ b[i]).
        # Точка x удовлетворяет запросу, если ∀i (1 ≤ i ≤ k) a[i] ≤ x[i] ≤ b[i], где x[i] – i-я координата точки
        # Результатом данной операции является объект-генератор.
        # Последовательность, получаемая в результате итерации по генератору должна содержать ровно один раз
        # каждую добавленную и не удаленную на момент запроса точку, удовлетворяющую запросу.
        # Точки с одинаковыми координатами считаются различными.
        # Точка представляется кортежем своих координат.
        for point in self.arr:
            if len(point) == len(coord_ranges):
                skip = False
                coord_ranges_it = iter(coord_ranges)
                for coord in point:
                    a, b = next(coord_ranges_it)
                    if not (a <= coord <= b):
                        skip = True
                if skip:
                    continue
                else:
                    yield point


ps = Points(2)
ps.add(1, 1)
ps.add(3, 1)
print(list(ps.range_query((1, 3), (1, 1))))  # [(1, 1), (3, 1)]
ps.add(3, 1)

# print(ps.arr)

print(list(ps.range_query((2, 3), (1, 1))))  # [(3, 1), (3, 1)]
ps.remove(2, 1)
ps.remove(3, 1)

# print(ps.arr)

print(list(ps.range_query((1, 3), (1, 1))))  # [(1, 1), (3, 1)]
