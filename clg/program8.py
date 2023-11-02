# li=[]
# n=int(input("Enter size of list :")) 
# for i in range(0,n):
#     e=int(input("Enter element of list :")) 
#     li.append(e)
# print("Original list: ",li) 
# list_copy = li.copy()
# print("After cloning: ",list_copy)

# my_list = [11,12,13,14,15]
# copy_list = my_list[:]
# print('Old List:',my_list) 
# print('New List:',copy_list)

# li=[]
# n=int(input("Enter size of list :")) 
# for i in range(0,n):
#     e=int(input("Enter element of list :")) 
#     li.append(e)
# print("Original list: ",li) 
# list_copy = list(li)
# print("After cloning: ",list_copy)

import copy
old_list = [[11, 21, 31], [12, 22, 32], [13, 23, 33]]
new_list = copy.deepcopy(old_list) 
print("Old list:", old_list) 
print("New list:", new_list)