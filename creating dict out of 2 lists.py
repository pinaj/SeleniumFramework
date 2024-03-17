list1 = ["a","b","c","d","e"]
list2 = [11,22,33,44,55]
#Output: dict1 = {'a': 11, 'b': 22, 'c': 33, 'd': 44, 'e': 55}

output = dict(zip(list1,list2))
print(output)
