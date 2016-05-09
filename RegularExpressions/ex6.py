"""
Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.

Sample Input:
I need to understand the human mind
humanity

Sample Output:
I need to understand the computer mind
computerity
"""

import sys
import re

for line in sys.stdin:
    line = re.sub(r"human", "computer", line.rstrip())
    print(line)
