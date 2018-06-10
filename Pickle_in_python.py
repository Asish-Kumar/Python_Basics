# Author: Asish kumar
# Topic: Pickle in  python
# Important methods: dump(), load(), dumps(), loads()
# dump() and load() are used to writing to or reading from a file
# dumps() and loads() are used to send data to or get data from a bytes object
# pickling protocols above 2 do not check for any security of the data,
# so pickling should only be done for that data that we trust
# do not load data from any non trusted source
# https://docs.python.org/3.4/library/pickle.html

import pickle

Names_list = ["Jarvis", "Jane Foster", "Kavin Stell", ["Howdy", "pickles", ["kilo"]]]
Word_touple = ("Refers to single entity",
               "Unmarried male human being",
               "Key to invention",
               ("Havana",
                "You Belong With Me",
                "Ae Dil Hai Mushkil"))
word_set = {"helllo", "Javan"}
with open("Pickle_File.extention", "wb") as pfile:
    pickle.dump(Names_list, pfile, protocol=3)  # there 4 protocols for pickling: 0, 1, 2, 3, 4
    pickle.dump(Word_touple, pfile, protocol=pickle.DEFAULT_PROTOCOL)
    # default protocol is protocol 3 and this is not compatible with python 2.x
    pickle.dump(word_set, pfile, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(Names_list, pfile)  # we can dump a single object more than once

with open("Pickle_File.extention", "rb") as ppfile:
    New_Names_list = pickle.load(ppfile)  # to get the original data in the same format
    New_Word_touple = pickle.load(ppfile)
    New_word_set = pickle.load(ppfile)
    New_Names_list_2 = pickle.load(ppfile)
# the first variable dumped will be the first to be loaded

print(New_Names_list)
print(New_Word_touple)

word1, word2, word3, word4 = New_Word_touple
print(word1)
print(word2)
print(word3)
print(word4)
print(word4[2])
print(New_word_set)
print("=" * 100)
print(pickle.HIGHEST_PROTOCOL, pickle.DEFAULT_PROTOCOL)
print(New_Names_list_2)
