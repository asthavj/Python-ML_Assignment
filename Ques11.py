def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))

fib_numbers = fibonacci(n)

print("The first", n, "numbers in the Fibonacci sequence are:", fib_numbers)
