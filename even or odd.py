# This checks even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(9))  # Output should be "Odd"
print(check_even_odd(10))  # Output should be "Even"
