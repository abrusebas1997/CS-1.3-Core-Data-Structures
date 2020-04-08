def iterative_search(list, target):
    for item in list:
        if item == target:
            return item

    return None


target = 3


def recursive_search(list, target, index):
    if list[index] == target:#base case
        return target #found it!
    if index == len(list):#didn't find it
        return None
    else:
        return recursive_search(list, target, index + 1)


#     if list:         # checks if list exists
#         if list[0] == target:        # base case - first index is key
#             return 0
#
#         s = recursive_search(list[1:], target)   # recursion
#         if s is not False:
#             return s+1
#         return False        # returns false if key not found
#
# print(recursive_search(list, target))
