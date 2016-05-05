import re

pattern = r"((\w+)-\2)"
string = "test-test chow-chow"
duplicates = re.findall(pattern, string)
print(duplicates)
