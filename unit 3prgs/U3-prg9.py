import re

text = "Python 123 is easy. I have 456 books."

pattern =r"\d+"

result1 = re.match(pattern, text)

if result1:
    print("Match: ", result1.group())
else:
    print("No match at the beginning")

result2 = re.search(pattern, text)

if result2:
    print("Search result: ", result2.group())
else:
    print("No number found")

result3 = re.findall(pattern, text)
print("All number:", result3)





