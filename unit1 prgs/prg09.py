def add(a, b):
    return a + b
def greet(name = "Student"):
    print("Hello", name)

def student(name, age):
    print("Name:", name)
    print("Age:", age)

def total(*numbers):
    return sum(numbers)

print("Addition:", add(10,20))
greet()
greet("Arjun")

student(age=21, name="Varun")
print("Total:", total(10, 20, 30, 40))
