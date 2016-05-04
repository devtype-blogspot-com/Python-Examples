from exceptions7 import BadName, greet as exc_greet
import exceptions7 as exc


def greet():
    print("Greetings!")

print(BadName)
print(greet)
greet()
print(exc_greet("Student"))
print(exc)


