#5.Write a program to demonstrate the use of break condition and pass statements.
print("   Using break   ")
for i in range(1, 11):
    if i == 6:
        print("Reached 6, breaking the loop.")
        break
    print(i, end="")

print("         ")

print("    Using continue    ")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")

print("    ")

print("    Using pass    ")
for i in range(1, 6):
    if i == 3:
        pass
    print(i, end=" ")
print()
