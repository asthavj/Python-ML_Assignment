#22. Write a python program that returns the minimum and maximum values in a list of numbers.
def find_min_max(numbers):
    if not numbers:
        return None, None

    min_value = max_value = numbers[0]

    for num in numbers:
        if num < min_value:
            min_value = num
        elif num > max_value:
            max_value = num
    
    return min_value, max_value


example_numbers = [3, 1, 7, 4, 2, 8, 5]
min_value, max_value = find_min_max(example_numbers)
print("Minimum value:", min_value)
print("Maximum value:", max_value)
