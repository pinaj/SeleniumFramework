list_1 = [1,2,45,6,7]
list_2 = [11,21,45,6,7]

#print[(1,11),(1,21),(1,45),(1,6),(1,7),(2,11)………]
list = []
for i in list_1:
    for j in list_2:
        list.append((i,j))
print(list)