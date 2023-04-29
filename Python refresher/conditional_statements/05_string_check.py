fruits = ["apple", "banana", "cherry", "date", 'ananas']

# Example 1
for fruit in fruits:
    if fruit[0] == 'a':
        print(fruit)

# Example 2
output = [fruit for fruit in fruits if fruit[0] == 'a']
print(', '.join(output))