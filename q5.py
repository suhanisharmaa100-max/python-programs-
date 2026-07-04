# Write a function count_vowels(word) that returns the number of vowels in the given string.
def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

print(count_vowels("Hello World"))  