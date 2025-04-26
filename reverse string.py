#This reverses how words appear
def reverse_string(text): #This reverses a string using a for loop
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text  # Add characters to the front
    return reversed_text

print(reverse_string("hello"))  # Output should be "olleh"
