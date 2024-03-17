list = [1, 2, 3, 4, 2]

largest_num = list[0]

for num in list[1:]:
    if num >largest_num:
        largest_num = num
print("largest number :", largest_num)

second_largest_num = float('-inf')

for num in list:
    if num != largest_num and num > second_largest_num:
        second_largest_num = num

print("second largest number:", second_largest_num)