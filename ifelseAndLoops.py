# # import random
# # maximum = 10
# # answer = random.randint(1, maximum)
# # count = 0
# # print("Guess a number between {} and {} or enter 0 to quit".format(1, maximum))
# # while count < 3:
# #     guess = int(input())
# #     if guess == 0:
# #         break
# #     count += 1
# #     if guess != answer and count <= 3:
# #         if guess < answer:
# #             print("Guess higher")
# #         else:
# #             print("Guess lower")
# #     elif count <= 3:
# #         print("Congratulations you have guessed it.")
# #         break
# # else:
# #     print("Better Luck next time!")
# # print(answer, "is the correct answer.")
#
# # meal =["Apple", "Papaya", "Rotten tomatoes", "eggs"]
# # for iteam in meal:
# #     if(iteam == "Rotten tomatoes"):
# #         print("Dirty food")
# #         break
# # else: # else doesn't executes if the break in the for loop executes,
# #       # else will execute if there is no break in the for loop
# #       # or the break didn't executes
# #     print("good food")
# # print("Foor is good man!")
# # x = 60
# # x //= 6
# # print(x)
# ########################################################################################################
# for state in ["Asish", "Rohit", "Bhanwar"]:  # elements stored in a list
#     print("Helo {0}".format(state))
#
# for state1 in {"Asish", "Rohit", "Bhanwar"}:  # elements stored in a set, and hence everytime different o/p
#     print("Helo {}".format(state1))
#
# for i in range(ord('a'), ord('z') + 1):
#     print("Helo " + chr(i))
# #########################################################################################################
# number = "121,3,,4,533,54,3434,2667,686,866,76"
# onlydigit = ''
# commas = ''
# for i in range(0, len(number)):
#     if number[i] in "0123456789":
#         onlydigit += number[i]
#     else:
#         commas += number[i]
# print("Number is : {} and commas are {}".format(int(onlydigit), commas))
# onlydigit = commas = ''
#
# for i in number:
#     if i in "0123456789":
#         onlydigit += i
#     else:
#         commas += i
# print("Number is : {} and commas are {}".format(int(onlydigit), commas))
#
# #############################################################################################################
# # name = input("Enter Name: ")
# # age = int(input("Enter your age(in years): "))
# # if(age>18 and age<=30):
# #     print("Hi",name+", we welcome you to 18-30 holiday")
# # elif(age<=18):
# #     print("Hi {}, it's a good news,"
# #           "you can come to enjoy the 18-30 holiday just in {} years".format(name,18-age))
# # else:
# #     print("""Hi {}, 18-30 holiday package is no more available for you,
# #             we will inform you for any alternative options.
# #      Meanwhile you can enjoy our excuisite free spaa.""".format(name))
# ############################################################################################################
dict_1 = {"Key1": "Value 1",
          "Key2": "value 2",
          "Key3": "value 3"}
for key, value in dict_1.items():
    print(key, value)
