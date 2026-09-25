#10. Write arogram to generate a sequence of numbers using generator functions and yield keyworl
def generate_number(limit):

    number = 1

    while number <= limit:
        yield number
        number += 1


number = generate_number(5)

print("Generated sequence:")

for value in number:
    print(value)
