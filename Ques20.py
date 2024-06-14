#20. Write a python program that takes a list of numbers and returns their sum.
def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


example_numbers = [1.5, 2.5, 3.0, 4.0]
total_sum = sum_of_numbers(example_numbers)

print("The sum of the numbers is:", total_sum)
