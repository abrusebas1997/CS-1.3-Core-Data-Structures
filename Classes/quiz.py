def reverse(number):
    stack = []
    result = ""

    for num in str(number):
        stack.append(num)

    for i in range(len(stack)):
        result += stack.pop()

    print(result)
    return int(result)

reverse(3479)
