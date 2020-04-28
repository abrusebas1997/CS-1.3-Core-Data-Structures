

#class 2
#interview question

def get_intersection(list1, list2):
    item_dictionary = {}
    intersection = []
    #loop through first list
    for item in list1:
        if item not in item_dictionary.keys():
            item_dictionary[item] = 1
    #loop through second list
    for item in list2:
        if item in item_dictionary.keys():
            item_dictionary[item] += 1

    for key, value in item_dictionary.items():
        if value > 1:
            intersection.append(key)
    return intersection

get_intersection([1,5,7,9], [2,3,1,9])
