#3 Write a program to generete a multiplication table using a for loop.
num = int(input("Enter a number: "))

print(f"Multiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
