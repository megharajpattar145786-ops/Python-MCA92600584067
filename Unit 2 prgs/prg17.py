#7. write a program to demonstarte list dictionary and set comprehensions.
nums = [1, 2, 3, 4, 5]
words = ["apple, bananna, dog"]

squares = [n * n for n in nums]

even_squares = [n * n for n in nums if n % 2 == 0]

num_to_square = {n: n * n for n in nums}

num_to_square = {n: n * n for n in nums}

first_letters = {w[0] for w in words}

print("squares:", squares)
print("even_squares:", even_squares)
print("num_to_square:", num_to_square)
print("first_letters:", first_letters)
