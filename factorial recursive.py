# This is a factorial recursive
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1  # Base case
    return n * factorial_recursive(n - 1)  # Recursive call

print(factorial_recursive(9))  # Output should be 362880
print(factorial_recursive(10))  # Output should be 3628800
