"""Write a function that will reverse a string using a stack"""

# Python program to reverse a string using stack

# Function to create an empty stack.
# It initializes size of stack as 0

def reverse_string_with_stack(input_string):
    my_stack = []
    reverse_string = ""

    #put the caracters on the stack
    for character in input_string:
        my_stack.append(character)

    while len(my_stack) !=0:
        character = my_stack.pop(-1)
        reverse_string += character

    return reverse_string


print(reverse_string_with_stack("abc"))
print(reverse_string_with_stack("abc"))
print(reverse_string_with_stack("abc"))
