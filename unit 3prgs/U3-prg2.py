#This file module name is my_module2p
#1
import my_module2p

print("1. Complete module: ")
print(my_module2p.add(6767, 6565))

#2
import my_module2p as mm

print("2. print's with alians: ")
print(mm.message("varun"))

#3
from my_module2p import add, message

print("3.Specific function: ")
print(add(654, 564))
print(message("Megharaj"))

#4
from my_module2p import add as addition

print("4. Function withn alias: ")
print(addition(654, 2345))

#5
from my_module2p import *

print("5. All Members: ")
print(number)
print(add(65, 69))

