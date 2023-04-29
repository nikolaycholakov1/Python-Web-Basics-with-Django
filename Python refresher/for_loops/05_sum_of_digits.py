numbers = [10, 23, 456]

output = []

for number in numbers:
    number = str(number)
    number_sum = 0

    for num in number:
        number_sum += int(num)
    output.append(number_sum)

print(output)