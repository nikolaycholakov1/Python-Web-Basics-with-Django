strings = ["apple", "banana", "cherry", "date", "elderberry"]

longest_string = ''

for string in strings:
    if len(string) > len(longest_string):
        longest_string = string

print(longest_string)
