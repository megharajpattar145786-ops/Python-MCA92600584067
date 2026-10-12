import os
import sys

print("current diectory:", os.getcwd())

folder = "myfolder"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Directory created:", folder)
else:
    print("Directory already exists")

file_path = os.path.join(folder,"sample.txt")

with open(file_path, "w") as file:
    file.write("This is a sample file.")

print("File created:", file_path)

print("Contents of current directory:")
print(os.listdir())

print("program name:", sys.argv[0])
