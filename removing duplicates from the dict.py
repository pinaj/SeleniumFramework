dict1 = {'a': 10, 'b': 20, 'a': 10, 'c': 30, 'd': 50, 'e': 70, 'b': 20}

unique = {}
for key,value in dict1.items():
    if key not in unique:
        unique[key] = value
print(unique)