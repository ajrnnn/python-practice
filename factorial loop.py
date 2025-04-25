def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):  # Multiply from 1 to n
        result *= i
    return result

print(factorial_loop(5))  # Output should be 120