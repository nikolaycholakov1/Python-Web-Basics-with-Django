first_num = int(input())
second_num = int(input())

# biggest_num = max(first_num, second_num)
biggest_num = 0
if first_num > second_num:
    biggest_num = first_num
else:
    biggest_num = second_num

print(biggest_num)
