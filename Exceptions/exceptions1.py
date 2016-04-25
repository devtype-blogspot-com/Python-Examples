try:
    x = [1, 2, "hello", 7]
    x.sort()
    print(x)
except TypeError:
    print("Type error :(")

print("I can catch")