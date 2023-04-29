# Write a program that takes a list of words as input and prints out the longest word(s) in the list.
# If there are multiple words with the same maximum length, print them all.

# words = ["apple", "banana", "cherry", "date", "elderberry"]

words = input().split()
longest_words = []
max_length = 0

for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_words = [word]
    elif len(word) == max_length:
        longest_words.append(word)

print(f"Longest word(s): {', '.join(longest_words)}")
