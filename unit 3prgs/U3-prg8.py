import re
text = input("Enter a sentence: ")

pattern = r"\d+"

result = re.search(pattern, text)

if result:
    print("Number found:",result.group())

else:
    print("No number found!!")





