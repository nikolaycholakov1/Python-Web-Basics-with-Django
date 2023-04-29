word = input('Enter a word: ')
for char in word:
    if word.count(char) == 1:
        print(f'The first non repeating character is {char}')
        break
else:
    print("There are no non-repeating characters in the string")