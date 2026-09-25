#2. write aprogram to check whether a number is positive negitive or zero using nested conditions.
num = float(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negitive.")
