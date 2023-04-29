list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

list3 = list1 + list2
unique_numbers = set()
for number in list3:
    unique_numbers.add(number)

print(unique_numbers)
