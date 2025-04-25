def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10  # Get the last digit
        number //= 10         # Remove the last digit
    return total

print(sum_of_digits(5678910))  # Output should be 36
print(sum_of_digits(1234567890))  # Output should be 45