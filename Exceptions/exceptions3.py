def f(x,y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError) as e:
        print(type(e))
        print(e)
        print(e.args)

print(f(5,0))
print(f(5,[]))
