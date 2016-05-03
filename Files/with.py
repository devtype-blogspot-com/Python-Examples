with open("test.txt") as f, open("test_copy.txt", "w") as w:
    for line in f:
        w.write(line)
