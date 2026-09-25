#4. Write a program to find the sum of digits of a number using a while loop.
num = int(input("Enter a number: "))
n = abs(num)
total = 0

while n > 0:
    digit = n% 10
    total += digit
    n //= 10

print("fSum of digit of {num} id:{total}")
