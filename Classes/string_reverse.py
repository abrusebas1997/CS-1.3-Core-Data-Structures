def reverse_string(my_string):
    reverse_str = ""
    index = len(my_string) - 1
    # we need to keep looping and index can be 0
    while index >= 0:
        # concatenating
        reverse_str += my_string[index]
        #we are going to substract one
        index -= 1
    return reverse_str

print(reverse_string("hello"))
print(reverse_string("even"))
