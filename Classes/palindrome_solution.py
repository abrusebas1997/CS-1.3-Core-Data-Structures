#Get a left position and a right
# iterative uses a loop
def is_palindrome(string):
    left_index = 0
    right_index = len(string) - 1

    #repeat, or loop
    while left_index < right_index:
        #check if dismatch
        if string[left_index] != string[right_index]:
            return False
        #move to the next characters to check
        # with the left we wanna move forward, so we add 1
        left_index += 1
        #  with right we need to substract
        right_index -= 1
    return True


#recursive
def is_palindrome_recursive(string, left_index, right_index):
    print(left_index)
    print(right_index)
    #base case, it's when we stop
    if left_index == right_index:
        return True
    if string[left_index] != string[right_index]:
        return False
    #recursive case, when we call the function within itself
    if left_index < right_index:
        return is_palindrome_recursive(string, left_index + 1, right_index - 1)
    return True
print(is_palindrome_recursive("talo", 0, len("deed")-1))
# print(is_palindrome_recursive("tacocat"))
# print(is_palindrome_recursive("tasdfklajdf"))
