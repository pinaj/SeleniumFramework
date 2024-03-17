str = 'aabbbsdfsd'

dict = {}
for char in str:
    dict[char] = dict.get(char,0)+1
print(dict)

'''for char in str:
    if char in dict:
        dict[char]+=1
    else:
        dict[char]=1
print(dict)'''



