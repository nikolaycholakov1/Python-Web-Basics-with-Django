list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = []
for number in list1:
    if number in list2:
        common_elements.append(number)

print(common_elements)
