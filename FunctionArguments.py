def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res

print('s(21) = ', s(21)) # 31
print('s(11, 10) = ', s(11, 10)) # 31
print('s(0, 0, 31) = ', s(0, 0, 31)) # 41

# TypeError: s() missing 1 required positional argument: 'a'
# print('s(b=31) = ', s(b=31))

print('s(11, 10, b=10) = ', s(11, 10, b=10)) # 31
print('s(11, b=20) = ', s(11, b=20)) # 31
print('s(5, 5, 5, 5, 1) = ', s(5, 5, 5, 5, 1)) # 31
print('s(11, 10, 10) = ', s(11, 10, 10)) # 41

# SyntaxError
# positional argument follows keyword argument
# print('s(b=31, 0) = ', s(b=31, 0))
