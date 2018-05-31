print("Howdy, mob")
first_name = 'Asish'
last_name = "Kumar"
name = first_name + ' ' + last_name
print(name + " is the developer of this python program.")
print(2 + 3, " is  equal to 2+3")
z = lambda x, y: y // x + True + True
# print(z)
print(z(True, False))
for i in range(2, 9):
    if i == 5:
        print(z(1, 0))
        continue
    print(i)
print("Next Loop 'While loop' starts from here: ")
while True:
    for i in range(0, 9):
        z = i + 9
        print(z)
    if z == 17:
        print("for z = 17 i is ", i)
        break
z = lambda x, y: x + y
print(z(z(10, 20), 2))
x = 2
y = 5
print("%d*%d = %d" % (x, y, x * y))

health = input("What is the player's health: ")
print("Ok player helth is \"%s\"" % health, "apples")
print("AAO", "RAja")

splitString = """Ok now this
is something cool
about python\
 yes or no"""
print(splitString)
print("Asish" + "Kumar")
print(2 * 3)
# name = "Pradhan Mantrii"
# for i in range(0,len(name)):
#     print(name[i])
# print(i,' ',len(name))
#
# if " "in name:
#     print("Yes, it's True!!")
# else:
#     print("False")
# print("Hello " "Asish" + str(494)+". How are you today?")
# answer = input()
# ansString = "fine"," good", "mst", "jhakaas", "well", "preety", "happy"# by seperating every word like this answer in ansString will look for exact match to each word
# if answer in ansString:  #for eg. aas is not in ansString but jhakaas is
#     print("Oh! that's excellent sir")
#     print("Please allow me to introduce you to PYTHON, myself!")
# else:
#     ask = input("If I may, What is it that is bothering you Sir?")
#     print("I'm so sorry for that, I'll try my best to distract you from your tension")
#     print("Let's {0:>9} {1}{2:<3}, Just For Fun!!!".format("learn",'Python',3)) #{0},{1} are replacement fields, <,> are used to set left or right alignment
# # after : in {} specifies the width that it will occupy
#
