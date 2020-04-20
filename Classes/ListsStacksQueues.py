"""Imagine you are wrtiing a function for a new code editor that
will check if a string expression contains correctly balanced parentheses.
 This function will return True if the string expression is correct and
 False if not"""



 def check(expression):
     #Going to push open on stack
     #if find an end compare to top of stack
     open_bracket = "[{("
     close_bracket = "]})"
     bracket_stack = []

     for character in expression:
         if character in open_bracket: #add open bracket to stack
             bracket_stack.append(character)


print(check("[[hello]], ((jess))"))
print(check("[[hello]], ((jess)"))
print(check("[[hello]], ((jess))("))
