first_num = int(input())
second_num = int(input())
third_num = int(input())

biggest_num = 0

if first_num >= second_num and first_num >= third_num:
    biggest_num = first_num
elif second_num >= first_num and second_num >= third_num:
    biggest_num = second_num
else:
    biggest_num = third_num

print(biggest_num)
# all_nums = [first_num, second_num, third_num]
# biggest_num = sorted(all_nums)
#
# print(biggest_num[-1])

