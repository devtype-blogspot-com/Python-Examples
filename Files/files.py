f = open("test.txt", "r")  # открыть файл на чтение

for line in f:
    line = line.rstrip()
    print(repr(line))

x = f.read()
print(repr(x))  # ''

f.close()
