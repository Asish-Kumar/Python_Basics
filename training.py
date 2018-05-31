# # print("Enter ip address")
# # ip=input()
# # r=len(ip)
# # count = 0
# # for i in ip:
# #     if i=='.' :
# #      count+=1
# # print(count)
# # segment =1
# # for i in ip:
# #             if i=='.' or i==':':
# #                 segment+=1
# # print("No of segments in ip are ",segment)
# # count=0
# # for i in ip:
# #     if i=='.' or i==':' or i:
# #         print(" next segment size is ",count)
# #         count=0
# #     else:
# #         count+=1
#
# # x =range(0, 100)[0:100:-2] # this will not work, x= range(0, 100)[100:0:-2] or [::-2] will work
# # for i in x:
# #     print(i)
# bak = "python is a good language"
# print(bak[::-1])
# #### Difference between bak[len(bak):0:-1] and bak[::-1] is that the first one will not print 'p' in python
# o = range(0, 100, 4)
# print(o)
# p = o[::5]
# q = range(0, 100, 4)[::5][::2][100: 0: -1]
# print(q)
# for z in q:
#     print(z)
# for i in p:
#     print(i)
start = stop = 0
str_2 = []
str_1 = "Hello My Name is Asish"
str_2 = str_1.split()
print(str_2)
print('e' in str_2)
str_1 = ' '.join(str_1.split())
print(str_1)
