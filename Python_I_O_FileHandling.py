file_1 = open("Sets.py", "r")
for i in file_1:
    if "print" in i:
        print(i, end='')
file_1.close()

print("=" * 100)

# another better way of file opening and closing handling is using 'with'
# 1. using with statement, we do not need to close the file when its use is no more
#    with does that by it self
# 2. using with statement gives us the advantage of error handling while reading and writing
#    into the file, also if there is any error during the file reading or writing the with
#    reads the error and closes the file which prevents data corruption
with open("Sets.py", 'r') as file_2:
    for i in file_2:
        if 'print' in i:
            print(i, end='')

print("=" * 100)

with open("Sets.py", 'r') as file_3:
    line = file_3.readline()
    while line:
        if "print" in line:
            print(line, end='')
        line = file_3.readline()
    # after when this loop is over the pointer in the file is at the end of the file, therefore lines will be an empty list
    # to make it working we need to first close the file (which will be automatically done by with when we open a new file)
    # then open the file once again
    print("=" * 100)
with open("Sets.py", 'r') as file_3:
    lines = file_3.readlines()
    # print(lines)
    for i in lines[::-1]:  # this reads from last line of file to first line, this reads line by line in reverse order
        print(i, end='')

    print("=" * 100)
with open("Sets.py", 'r') as file_3:
    line = file_3.read()
    # print(line)
    for i in line[::-1]:  # this reads from last character of file to first character
        print(i, end='')

    print("=" * 100)

    print(file_3.readable())
