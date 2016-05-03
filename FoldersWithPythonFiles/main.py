import os

os.chdir("test2")  # cменить текущую папку
print(os.getcwd())

for current_dir, dirs, files in os.walk("."):
    if len(list(filter(lambda x: ".py" in x, files))) > 0:
        print(current_dir.replace('\\', '/').replace("./", ""))
