list = [1, 2, 3, 4, 2]

non_dup_list = []
dup_list = []
for char in list:
    if char not in non_dup_list:
        non_dup_list.append(char)
    else:
        dup_list.append(char)

#print(non_dup_list)
print(dup_list)

