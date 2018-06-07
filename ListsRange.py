# PlayerList = []
# Ranks = []
# print("Please Enter Player Name and Their Ranks or enter q to quit: ")
# while True:
#     entered = input("Enter Player Name: ")
#     if entered == 'q':
#         break
#     PlayerList.append(entered)
#     Ranks.append(input("Now enter Rank of {}: ".format(entered)))
# for i in range(0, len(PlayerList)):
#     print("Player: {:13} has rank: {:2}".format(PlayerList[i], Ranks[i]))
# Ranks.short() # This actually changes or shorts the values in the Ranks List
# print(shorted(Ranks)) # This creates another object and shorts the values
# so the actual values are not changed
# List_1 =[4, 6, 8, 1]
# List_2 = []
# List_2 = List_1 # This assigns the same List_1 to the List_2
# # List_2.sort() # Therefore sorting List_2 will sort List_1
# print(List_1)
# List_3 = list(List_1) # This creates a new List_3 and then copies every element of List_1 to List_3
# List_3.sort() # Therefore sorting List_3 does not sort List_1
# print(List_1)
# List_1 = [5, 4, 3, 2, 1]
# List_2 = [6, 7, 8, 9, 0]
# List_3 = [List_1, List_2, "Asish", [0]]
# print(List_1)
# print(List_2)
# print(List_3)
# print(List_3[0][0:4])
# print(List_3[1])
# print(List_3[2][0:3])
# print(List_3[3])
# for iteams in List_3:
#     print(iteams)
#     for iteam in iteams:
#         print(iteam)

List_4 = ["Asish", [24, 23], "98", 99]
a, b, c, d = List_4  # this is called list unpacking, but it is not recommended as lists are mutable

print(a)
print(b)
print(c)
print(d)

menu = []
food = ""
menu.append(["Apple", "Spam", "Orange"])
menu.append(["Spam", "Orange"])
menu.append(["Apple", "Banana", "Orange"])
menu.append(["Apple", "Spam", "Banana"])
menu.append(["Apple", "Apple", "Orange"])
menu.append(["Spam", "Spam", "Orange"])

for meal in menu:
    if "Spam" not in meal:
        for food in meal:
            print(food)
menu_2 = []
i = 0
for meal in menu:
    for food in meal:
        i = 0
        for iteam in menu_2:
            if iteam is food:
                i = 1
        if i == 0:
            menu_2.append(food)
print("Next List")
print(menu_2)

for i in range(0, len(menu)):
    print(next(iter(menu)))

my_List = list(range(ord('a'), ord('z') + 1, 2))
my_List_2 = []
for i in my_List:
    my_List_2.append(chr(i))
print(my_List)
print(my_List_2)

my_string = 'abcdefghijklmnopqrstuvwxyz'
print(my_string.index('ijk'))
print(my_string[8:14])

seven = range(0, 10, 2)
print(range(0, 10, 2)[2])

print(range(0, 5, 2) == range(0, 7, 2))
for i in range(0, 30, -2):
    print(i)  # this doesn't print anything,
# because range(0, 30, -2) means start from 0 every time add -2 until you reach 30
