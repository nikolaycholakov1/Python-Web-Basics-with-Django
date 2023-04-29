def only_even(nums_list):
    output = []
    for num in nums_list:
        if num % 2 == 0:
            output.append(num)

    return output


print(only_even([1, 2, 3, 4, 5]))
