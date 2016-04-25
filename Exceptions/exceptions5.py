try:
    15 / 0
    # e
except ZeroDivisionError: # isinstance(e, ZeroDivisionError) == True
    print("Division by zero")
except ZeroDivisionError: # не имеет смысла, т.к. все арифметические ошибки мы поймали выше
    print("zero division")

print(ZeroDivisionError.mro())