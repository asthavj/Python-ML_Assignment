def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        digit = number % 10
        sum_digits += digit
        number //= 10
    return sum_digits

number = int(input("Enter a number: "))

result = sum_of_digits(number)

print("The sum of digits in the number", number, "is:", result)
