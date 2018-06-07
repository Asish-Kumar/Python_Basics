# Author: Asish Kumar
# Challenge: Create a program that takes some text and creates a list of
# all the characters in the text which are not vowels, sorted in alphabetical order

text = set(input("Please enter some text: "))
vowels_set = frozenset("aeiou")
text_list = list(text.difference(vowels_set))
text_set = set(text_list)
print(sorted(text_set))
