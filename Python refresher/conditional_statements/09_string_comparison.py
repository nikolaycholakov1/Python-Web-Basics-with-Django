string1 = input()
string2 = input()

char_counts = {}

for char in string1:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

for char in string2:
    if char in char_counts:
        char_counts[char] -= 1
    else:
        print('The second string cannot be formed by the characters of the first string.')
        break

else:
    if all(count >= 0 for count in char_counts.values()):
        print('The second string can be formed by the characters of the first string.')
    else:
        print('The second string cannot be formed by the characters of the first string.')
