def fib(k):
    if k == 0 or k == 1:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)

if __name__ == "__main__":
    print(__name__)
    print(fib(31))
