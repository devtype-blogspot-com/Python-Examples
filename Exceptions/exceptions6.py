def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero")
    else:  # если не будет никакого исключения
        print("result is", result)
    finally:  # просто выведем строку "finally"
        print("finally")

divide(2, 1)
divide(2, 0)
divide(2, [])
