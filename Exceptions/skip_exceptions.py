"""
Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Или эквивалентно записи:
class Error1(Error2, Error3 ... ErrorK):
    pass

Антон написал код, который выглядит следующим образом.
try:
   foo()
except <имя 1>:
   print("<имя 1>")
except <имя 2>:
   print("<имя 2>")
...

Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить,
так как ранее в коде будет пойман их предок. Но Антон не помнит какие исключения наследуются от каких.
Помогите ему выйти из неловкого положения и напишите программу, которая будет определять обработку каких исключений
можно удалить из кода.

Важное примечание:
В отличие от предыдущей задачи, типы исключений не созданы.
Создавать классы исключений также не требуется
Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить,
потому что мы уже ранее где-то поймали их предка.


Формат входных данных:
В первой строке входных данных содержится целое число n - число классов исключений.

В следующих n строках содержится описание наследования классов.
В i-й строке указано от каких классов наследуется i-й класс.
Обратите внимание, что класс может ни от кого не наследоваться.
Гарантируется, что класс не наследуется сам от себя (прямо или косвенно),
что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
Гарантируется, что никакое исключение не обрабатывается дважды.


Формат выходных данных:
Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода,
не изменив при этом поведение программы. Имена следует выводить в том же порядке, в котором они идут во входных данных.


Пример теста 1:

Рассмотрим код
try:
   foo()
except ZeroDivision :
   print("ZeroDivision")
except OSError:
   print("OSError")
except ArithmeticError:
   print("ArithmeticError")
except FileNotFoundError:
   print("FileNotFoundError")
...

По условию этого теста, Костя посмотрел на этот код, и сказал Антону,
что исключение FileNotFoundError можно не ловить, ведь мы уже ловим OSError -- предок FileNotFoundError

Sample Input:
4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError

Sample Output:
FileNotFoundError
"""

import sys

data = {}
exs = []
for_output = []


def find_ancestor(ex, target_ancestor):
    global data
    for ancestor in data[ex]:
        if ancestor == target_ancestor:
            return True
        elif find_ancestor(ancestor, target_ancestor):
            return True
        else:
            continue
    return False


def read_user_input(file_name_given):
    global data, exs, for_output

    if file_name_given:
        inf = open(file_name_given)
    else:
        inf = sys.stdin

    n = int(inf.readline())
    while n > 0:
        line = inf.readline().rstrip()
        if ':' in line:  # есть предки
            ex, ancestry = map(str, line.split(':'))
            ex = ex.rstrip()
            ancestors = ancestry.strip().split(' ')
        else:  # нет предков
            ex = line
            ancestors = []
        if ex not in data:
            data[ex] = []
        data[ex].extend(ancestors)
        n -= 1
    #  print(data)

    m = int(inf.readline())
    exs = []
    while m > 0:
        ex = inf.readline().rstrip()
        exs.append(ex)
        for_output.append(False)
        m -= 1
    for i in range(0, len(exs)):
        for j in range(i, len(exs)):
            if i == j:
                continue
            elif find_ancestor(exs[j], exs[i]):
                for_output[j] = True

read_user_input("skip_exceptions_input3.txt")
#  read_user_input(None)

for i in range(0, len(exs)):
    if for_output[i]:
        print(exs[i])