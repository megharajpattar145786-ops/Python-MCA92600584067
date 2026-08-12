numbers = [20, 30, 40, 50, 60]

print("Original list:", numbers)

print("First element:", numbers[0])
print("Last element:", numbers[-1])

print("First three element:", numbers[0:3])
print("Last two element:", numbers[3:])
print("Reverse list:", numbers[::-1])

numbers.append(60)
numbers[1] = 25

print("After manipulation:", numbers)

squares = [number * number for number in numbers]

print("Squares:", squares)

even_numbers = [number for number in numbers if number % 2 == 0]

print("Even numbers:", even_numbers)
