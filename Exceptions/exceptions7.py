GREETING = "Hello, "


class BadName(Exception):
    pass


def greet(n):
    if n[0].isupper():
        return GREETING + n
    else:
        raise BadName(n + " is inappropriate name")

__all__ = ["BadName", "greet"]

# while True:
#     try:
#         name = input("Please enter your name: ")
#         greeting = greet(name)
#         print(greeting)
#     except ValueError:
#         print("Please try again")
#     else:
#         break

print("Import is execution")
