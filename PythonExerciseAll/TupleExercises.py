# Tuple Exercises:
# 1. Write a Python program to find the length of a tuple.
# t = (1,2,3,4,5,6,8)
# t1 = ('Pune',4,6,9,'Satara')
# print(len(t1))
# print(len(t))
#_____________________________________________________________________________________________
# 2. Write a Python program to concatenate two tuples.
# t = (1,2,3,4,5,6,8)
# t1 = ('Pune',4,6,9,'Satara')
# print((t1+t))
#________________________________________________________________________________________________
# 3. Write a Python program to convert a tuple to a list.
# t = (1,2,3,4,5,6,8)
# t1 = ('Pune',4,6,9,'Satara')
# print(list(t))
# print(list(t1))
#_________________________________________________________________________________________________
# 4. Write a Python program to find the index of an element in a tuple.
from functools import reduce

# t1 = ('Pune',4,6,9,'Satara')
# index = t1.index("Satara")
# print("Index of given element is",index)
#___________________________
# 5. Write a Python program to check if an element exists in a tuple.
# t1 = ('Pune',4,6,9,'Satara')
# flag = 0
# if 'Puna' in t1:
#     flag = 1
# if flag==1:
#     print("THe given element is present in tuple ")
# else:
#     print("The element is not present in tuple")
# 6. Write a Python program to count the number of occurrences of an element in a tuple.
# t1 = ('Pune',4,6,9,'Satara','Satara','Satara')
# print(t1.count('Pune'))
# 7. Write a Python program to find the maximum and minimum elements in a tuple.
# t1 = ('Pune','Satara','Mumbai','Kolhapur')
# t2 = (2,8,46,87,96)
# print(min(t2))
# print(max(t2))
# print(max(t1))
# print(min(t1))
# 8. Write a Python program to reverse a tuple.
# t2 = (2,8,46,87,96)
# reversetuple = t2[::-1]
# print(reversetuple)
# 9. Write a Python program to check if all elements in a tuple are the same.
# t2 = (2,8,46,87,96)
# t1 = ('Pune','Pune','Pune','Pune')
# result=all(i==t1[0]for i in t1)
# if result == True:
#     print("All elements are equal")
# else:
#     print('Elements are not equal')
# 10. Write a Python program to create a new tuple with the elements from two existing tuples.
t1 = (1,2,3,4)
t2 = (5,6,7,8)
# t3=lambda t1,t2 :reduce((lambda x,y:x+y,[t1,t2]))
t3 = t1 + t2
print(t3)