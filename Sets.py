#  Author: Asish Kumar
# Sets are mutable objects in Python
# That means they support item assignment just like lists
# Elements of a set are immutable objects
# Sets are unordered just like dict because their elements are hashed
#
# Mutable objects:
# list, dict, set, byte array
# Immutable objects:
# int, float, complex, string, tuple, frozen set, bytes
#
# in sets we use {}
# in tuple we use ()
# in list we use []
# in dict we use {:}
Animal_set = {"Horse", "Goat", "Hen", "Lion"}  # simple way of declaring sets
print(Animal_set)
for i in Animal_set:
    print(i)
Animal_tuple = ("Horse", "Tiger", "Rabbit")
Animal_set_2 = set(Animal_tuple)  # another way of creating a set from existing tuple () or from list []
print(Animal_set_2)
# Animal_tuple[1] = "Hen"  # error : 'tuple' object does not support item assignment
# Fruit_set_3 = {"Orange", {"Banana", "Papaya"}}  # error : unhashable type: 'set'
#
# All the immutable objects are hashable in Python but mutable objects are not
# just like dict, sets's elements are also hashed
# so a set cannot contain any of the mutable objects as its elements

Fruit_tuple = Animal_set, Animal_tuple, "Hello"
print(Fruit_tuple)  # mutable objects can have immutable objects as their elements

Fruit_set = {"Horse", "Horse", "Hen"}  # data duplicacy is automatically removed in sets
print(Fruit_set)

Empty_1 = {}  # this is not an empty set, its an empty dict
Empty_2 = set()  # this is an empty set

Empty_2.add(Animal_tuple)
Empty_2.add("Hello")
Empty_2.add(range(0, 30, 2))
print(Empty_2, '\n', "=" * 50)
for i in Empty_2:
    print(i)
for i in range(0, 30, 2):
    print(i)

set_1 = set(range(0, 60, 4))
# set_1.add("Python")
print("=" * 80, '\n', set_1)

set_2 = set(range(20, 60, 3))
print(set_1.intersection(set_2))
print(set_1 & set_2)  # same as .intersection
print(set_1.union(set_2))
print(sorted(set_1.difference(set_2)))  # .sort is not there for sets
print(sorted(set_1 - set_2))  # .difference or - only works if there are no strings

set_1.difference_update(set_2)  # this does not return anything, simple subtract set_2 from set_1 and update set_1
print("=" * 80, '\n', sorted(set_1))
print(sorted(set_2))
print("Symmetric difference is union minus intersection: ")
print(set_1.symmetric_difference(set_2))
print(set_2.symmetric_difference(set_1))

# two available ways to remove item from set
# 1. remove : this will give error if no such item exists in the set
# 2. discard : this will not give any error whether or not if element exist in set
print(set_1, "Hllllllooooooooo")
set_1.remove(36)
print(sorted(set_1))
set_1.discard(31)  # nothing will be removed because 31 does not exist in set_1 and gives no error
print(sorted(set_1))
try:
    set_1.remove(31)
except KeyError:
    print("Could not do that")
