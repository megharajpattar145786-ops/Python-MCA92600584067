import re

with open("data.txt.txt.txt", "r") as  file:
    text = file.read()

name = re.search(r"Name:\s*(.*)", text)
email = re.search(r"Email:\s*([\w.]+@[\w.-]+\.\w+)", text)
phone = re.search(r"Phone:\s*(\d+)", text)

if name:
    print("Name:", name.group(1))

if email:
    print("Email:", email.group(1))
if phone:
    print("phone:", phone.group(1))
    
'''with open("D:/megharaj.p67/python/data.txt", "r") as file:
    print(file.read())'''

