# In dictionaries we use immutable objects for key, like tuple
dict_1 = {'Jaipur': 'The capital of Rajasthan',
          "Rajasthan": "A beautiful state in India",
          "India": "An incredible country in Asia",
          "Asia": "A wonderful continent on Earth",
          "Earth": "A crystal like blue planet that revolves around sun.."}
print("India is " + dict_1["India"] + "\n" + "Earth is " + dict_1["Earth"])
print(dict_1)
dict_1["Moon"] = "Natural Satellites of a planet"  # this is how we add new entries to the dictionaries
print(dict_1)
del dict_1["Moon"]  # deleting an entry from the dictionary
print(dict_1)
# dict_1.clear()  # deleting all the contents on the dictionary
# del dict_1  # deleting complete dictionary
while True:
    user_input = input("Enter a key value: ")
    if user_input == 'quit':
        break
    description = dict_1.get(user_input, "We don't {} in the dictionary".format(user_input))
    print(description)

key = input("Enter a key: ")
print(key in dict_1)

for key in dict_1:
    print(key, ":", dict_1[key])
dict_2 = {1: 11111, 8: 8888, 5: 55555, 0: 00000}
print("=" * 100)
for key in dict_2:
    print(key, ":", dict_2[key])
keys = list(dict_2.keys())
print("=" * 100)
keys.sort()
for i in keys:
    print(dict_2[i])
# or this line could be used  to sort sorted(dict_2.keys())
dict_key = dict_1.keys()
print(dict_key)
dict_1["New"] = "Hello new item"
print(dict_key)

dict_2 = {1: 11111, 8: 8888, 5: 55555, 0: 00000}
for i in dict_2.values():
    print(i)
# dict_1.update(dict_2)  # this return none
dict_4 = dict_1.copy()  # to copy one dictionary to another
print(dict_4)
