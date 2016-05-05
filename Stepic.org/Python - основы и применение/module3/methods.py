# print("abc" in "abcba")
# print("abce" in "abcba")

# print("cabcd".find("abc", 1))  # индекс первого вхождения или -1
# print("cabcd"[1:].find("abc"))
# print(str.find.__doc__)

# print("cabcd".index("abc"))  # индекс первого вхождения или ValueError
# print("cabcd".index("aec"))

# s = "The whale in black fled across the desert, and the gunslinger followed"
# print(s.startswith(("The woman", "The dog", "The man in black")))
# print(s.startswith.__doc__)

# s = "image.png"
# print(s.endswith(".png"))

# s = "abacaba"
# print(s.count("aba"))
# print(s.count.__doc__)
# print(s.find("aba"))
# print(s.rfind("aba"))

# s = "The man in black fled across the desert, and the gunslinger followed"
# print(s.lower())
# print(s.upper())
# print(s.count("the"))
# print(s.lower().count("the"))

# s = "1,2,3,4"
# print(s)
# print(s.replace(",", ", ", 2))
# print(s.replace.__doc__)

# s = "1\t\t 2  3       4       "
# print(s.split())
# print(s.split.__doc__)

# s = "_*__1, 2, 3, 4__*_"
# print(repr(s.rstrip("*_")))
# print(repr(s.lstrip("*_")))
# print(repr(s.strip("*_")))

# numbers = map(str, [1, 2, 3, 4, 5])
# print(repr(" ".join(numbers)))


# capital = 'London is the capital of Great Britain'
# template = '{} is the capital of {}'
# print(template.format("London", "Great Britain"))
# print(template.format("Vaduz", "Liechtenstein"))
# print(template.format.__doc__)


# template = '{capital} is the capital of {country}'
# print(template.format(capital="London", country="Great Britain"))
# print(template.format(country="Liechtenstein", capital="Vaduz"))

#
# import requests
# template = "Response from {0.url} with code {0.status_code}"
#
# res = requests.get("https://docs.python.org/3.5/")
# print(template.format(res))
#
# res = requests.get("https://docs.python.org/3.5/random")
# print(template.format(res))

# from random import random
# x = random()
# print(x)
# print("{:.3}".format(x))