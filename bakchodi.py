# import random
# ls = [0]
# # for i in range(1,20):  
# #     ls.append(random.randint(0,1000000))
# # print(sorted(ls))
# list =[1,2,3,4,5,12,1,2,3]
# a = str(list)
# print(a)
# print(list)
# print(type(a))
# print(type(list))
# b = set(list)
# print(type(b))
# print(sorted(b))
# print(len(b))
# print(len(list))
nums=[1,2,3,1]
if len(set(nums)) == len(nums):
    print(True)
else:
    print(len(set(nums)))