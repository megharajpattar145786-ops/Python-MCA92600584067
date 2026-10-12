import math
n = int(input("Enter a number: "))

print("square root =", math.sqrt(n))
print("squre =", math.pow(n, 2))
print("Factorial =", math.factorial(n))
print("Floor =", math.floor(n))

if n>0:
    print("natural logarithum:", math.log(n))
else:
    print("Naturla logarithum: not avialable")

print("value of pi:", math.pi)
print("value of e:", math.e)
