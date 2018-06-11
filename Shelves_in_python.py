# Author: Asish Kumar
# Topic: Shelves in python
# Shelves are like dict, but they store data in files
# DO NOT USE SHELVES FILES FROM UNTRUSTED SOURCES, LIKE INTERNET
# shelve uses database to store data
# Difference between a dict and a shelve:
#   keys of a dict can be any immutable objects
#   keys of a shelve must be strings, but values can be near about anything in python
# Drawback of using shelves is that because shelve uses pickling and unpickling, so if the data is very much complex,
# it can consume a noticeable time and resources for storing them
# concurrent write access is not allowed in shelves
# shelves are not secure to store data that will be used on a server or will be used across a network

import shelve

# sfile = shelve.open("Shelve_File")
with shelve.open("Shelve_File") as sfile:
    sfile['key1'] = "value 1"
    sfile["India"] = "Incredible country"
    sfile["Moon"] = "natural Satellite of Earth"
    sfile["Jupiter"] = "A very big planet far from Earth and Sun"
    sfile[chr(64)] = ["Well 64 is just a number", "64 = 60 + 3 + 1"]
    # once the shelve is open we can do both read and write operations
    print(sfile["Jupiter"])
    print(sfile["key1"])
    print("\n" + chr(64))
    print(sfile['@'])
    Dict_1 = sfile.dict  # this does not convert the shelve into a dict
    print(Dict_1['@'])
    Dict_2 = dict(sfile)  # this does convert the shelve into a dict
    print(Dict_2)

# Shelve is persistent to the file, that means if we add new content to file older content will not be lost

with shelve.open("Shelve_File") as sfile:
    sfile['key2'] = "value 2"
    print(sfile["key2"])
    print(sfile["key1"] + "\n\n")

    sfile["@"].append("Hello My Friend")  # this does not actually update the original shelve,
    #  rather it updates a copy of the shelve which is not stored on the disk
    # to actually update we should do  it as:
    List_1 = list(sfile['@'])
    List_1.append("Hello My Friend")
    sfile['@'] = List_1

    for key in sfile:
        print(key, ":", sfile[key])
    sfile["key1"] = "This is a value man!"  # updating value for a key
    del sfile["key2"]  # to delete a particular entry corresponding to the key
    print("=" * 55)
    for key in sfile:
        print(key, ":", sfile[key])
    # sfile.clear()  # to delete every entry
    # print("="*55)
    # for key in sfile:
    #     print(key, ":", sfile.get(key))  # sfile.get(key) is used in place of sfile[key]

# another method to update the value in the original shelve

with shelve.open("Shelve_File", writeback=True) as sfile:
    sfile["key1"] = "Oh! my God, that's a value"
    sfile.sync()
    print("=" * 55)
    for key in sfile:
        print(key, ":", sfile.get(key))

# with shelve.open("Shelve_File") as Sfile:
#     Sfile = {"Java": "A widely used programing language",
#              "Python": "A very powerful Scripting language"}
# # This is not how we can set values to the shelve, here we just redeclared 'Sfile' as dict
