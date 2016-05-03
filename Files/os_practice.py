import os
import os.path
import shutil

shutil.copy("tests/test1.txt", "tests/test2.txt")  # копировать файл
shutil.copytree("tests/", "tests/tests")  # копировать папку tests внутрь себя же

for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)
