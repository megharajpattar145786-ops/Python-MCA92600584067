#8. write a program to illustrate cariable scope using local global and nonlocal variables.
x = 10

def use_global():
    global x

    print("Inside use_global, x (global)=", x)
    x = x + 5
    print("After changing, x (global)=", x)

def outer():
    y = 20
    
    def inner():
        nonlocal y
            
        print("Inside inner, y (nonlocal) before change =", y)
        y = y + 7
        print("Inside inner, y (nonlocal) after change =", y)
        
    inner()
    print("Inside outer, y after calling inner =", y)

def local_example():
     z = 30
     print("Inside local_example, z(local) =", z)
     
print("Initial global x =", x)

use_global()

print("Afer use_global, global x =", x)

print()

local_example()

print()

outer()

