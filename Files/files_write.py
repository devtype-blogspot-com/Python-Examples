f = open("test1.txt", "w")
lines = ["Line 1", "Line 2", "Line 3"]
contents = "\n".join(lines)
f.write(contents)
f.close()
