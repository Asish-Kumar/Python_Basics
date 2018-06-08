# # Author: Asish Kumar
list_1 = ["Asish", "Kumar", "Will"]
with open("Sample.txt", 'w') as file_1:
    # for i in list_1:
    # file_1.write(i)
    print(list_1, file=file_1)
# everything that is written in a file in python is stored as string
# but we could use eval() method to evaluate the stored string while reading the file
with open("Sample.txt", 'r') as file_2:
    list_2 = eval(file_2.read().strip("\n"))
print(list_2[0] + '\n' + list_2[1], '\n', list_2[2])  # observe the space when output is printed
print("Python".strip("on"))  # .strip method removes characters from either start or end of a string

# to copy content of one file to another file where file extension may be different
# with open("F:\\STUDY\\vdo.mp4", "r+b") as videoFile:  # r+b is used for opening a file in byte readable mode
#     with open("F:\\STUDY\\bacd.csd", 'w+b') as bacdFile:  # w+b is used for opening a file in byte writable mode
#         print(videoFile.read)
#         bacdFile.write(videoFile.read())

# Appending data to a file
with open("Sample.txt", "ta") as file_1:
    for i in range(2, 13):
        for j in range(1, 11):
            print("{:>2} times {} is {}".format(i, j, i * j), file=file_1)
        print("=" * 100, file=file_1)
