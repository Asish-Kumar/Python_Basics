ipaddress = input("Enter an IP address: ")
length = 0
segcount = 0
for i in range(0, len(ipaddress) + 1):
    if i < len(ipaddress) and ipaddress[i] in "0123456789":
        length += 1
    elif i == len(ipaddress) or ipaddress[i] == '.' or ipaddress[i] == ':':
        segcount += 1
        print("Segment {0} found with length {1}".format(segcount, length))
        length = 0
    else:
        print("Invalid IP address. Check condition terminated.")
        break
print("There are exactly", ipaddress.count("."), "dots(.) and ", ipaddress.count(":"), "colons(:) in the IpAddress")
