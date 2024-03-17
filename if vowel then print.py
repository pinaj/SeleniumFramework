str1 = "Pinaj Patro"
#o/p: list1 = ['P', 'n', 'j P', 'tr']
vowels = ['a','e','i','o','u']

lst = list(str1)
for i in lst:
    if i not in vowels:
        print(list(i))

