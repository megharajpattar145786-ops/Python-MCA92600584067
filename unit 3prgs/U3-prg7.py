import shutil
import os

with open("sample.txt", "w")as file:
    file.write("This is a sample file.")

shutil.copy("Sample.txt", "copy.txt")
print("File copied successfully.")

shutil.move("copy.txt", "moved.txt")
print("File moved.txt")

os.remove("moved.txt")
print("File deleted successfully.")
