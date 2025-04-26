#This does sum list of elements
def sum_list(numbers):
    total = 0  # Start with 0
    for num in numbers:
        total += num  # Add each number
    return total

print(sum_list([3, 10, 29, 35, 69]))  # Output should be 146
