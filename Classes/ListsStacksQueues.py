

"""Imagine you are wrtiing a function for a new code editor that
will check if a string expression contains correctly balanced parentheses.
 This function will return True if the string expression is correct and
 False if not"""

open_bracket = ["[", "{", "("]
closed_bracket = ["]", "}", ")"]
bracket_stack = []

def check(expression):
     #Going to push open on stack
     #if find an end compare to top of stack
    for character in expression:
        if character in open_bracket: #add open bracket to stack
             bracket_stack.append(character)
        if character in closed_bracket:
            position = closed_bracket.index(character)
             #check if the open bracket at the top matches the closed bracket
            open_bracket_attop = bracket_stack.pop(len(bracket_stack) - 1)
            if open_bracket_attop != open_bracket[position]:
                return False
    if len(bracket_stack) == 0:
        return True
    else:
        return False


print(check("[[hello]], ((jess))"))
print(check("[[hello]], ((jess)"))
print(check("[[hello]], ((jess))("))
