tuple1 = "asish", 'kumar', 494  # this is a tuple
tuple2 = ("asish", "ashwin", 321, 433, 'python')  # this is also a tuple
print(tuple1)
print(tuple2)
print("asish", 'kumar', 494)  # this not a tuple
print(("asish", 'kumar', 494))  # this is a tuple
#  tuple1[0] = 'Asish'  # this is not allowed
tuple1 = 'Asish', tuple1[1], tuple2[2], tuple2[3]  # this is how updation is allowed
tuple2 = 'kuldeep'
print(tuple1)
print(tuple2)
tuple2 = 'PAPAYA', 876, 'dsss'
print(tuple2)
# tuple1.append("Hello")  # cannot do that

# Different ways to assign values to variables
a = b = c = d = 24
print(a, b, c, d)
a, b, c, d = 1, 2, 3, 4  # @@@ THIS IS CALLED UNPACKING
print(a, b, c, d)

# Unpacking tuples:
a, b, c, d = tuple1  # correct unpacking
print(a, b, c, d)
# a, b = tuple1 # valueError: too many values to unpack
tuple3 = (tuple1, tuple2, "Punjab", (92, 76, 78))
print(tuple3)
list1 = [tuple3, 'Dabangg', 'Havana', 00]  # a list can contain a tuple
print(list1)
tuple4 = (list1, 56)
print(tuple4)  # a tuple can contain a list
print(tuple4[0][0][1][0])  # we can print or extract individual item of the tuple
for i in tuple4:
    print(i)
tuple4[0].append("Hawayei")
for i in tuple4:
    print(i)
