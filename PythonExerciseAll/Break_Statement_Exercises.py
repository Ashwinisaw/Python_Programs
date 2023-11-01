# Break Statement Exercises:
# 1. Write a Python program to find the first occurrence of a number in a list using a for loop and break statement.
# l1 = [2,4,6,8,9,6]
# num = 6
# flag = 0
# for i in range(0,len(l1)):
#     if l1[i]==num:
#         flag == 1
#         break
# if flag == 1:
#     print("The number is found at lacation",i)
# else:
#     print("The number is not present in list")
    #__________________________________
# my_list = [1,2,2,3,4,8,6,9,8]
# element_to_find = 8
# for index, element in enumerate(my_list):
#     if element == element_to_find:
#         print("The element found at index",index)
#         break
#____________________________________________________________________________________________________________
# 2. Write a Python program to search for a specific element in a list using a while loop and break statement.
# my_list = [1,2,3,4,5,6,8,9]
# element_to_find = 4
# i = 0
# while i < len(my_list):
#     if my_list[i]==element_to_find:
#         print('The element is present at index',i)
#         break
#     i +=1
#______________________________________________________________________________________________________________
# 3. Write a Python program to find the prime numbers between 1 and 100 using a for loop and break statement.
# for i in range(2,101):
#     for j in range(2,i):
#        if i % j == 0:
#            break
#        else:
#            print(i)
#__________________________________________________________________________________________________________________-
# 4. Write a Python program to check if a number is present in a list using a while loop and break statement.
import flag as flag
# l1 = [1,2,3,4,5,6,7,8,9]
# num = int(input('Enter a no to be search'))
# i = 0
# flag = 0
# while i <= (len(l1)-1):
#     if l1[i] == num:
#         flag = 1
#         break
#     i += 1
# if flag==1:
#     print('the number is present in list at location',i)
# else:
#     print('The number is not present in list')
#____________________________________________________________________________________________________________________
# 5. Write a Python program to find the largest palindrome number in a given range using a for loop and break statement.
# newnum=[]
# for i in range(1,354):
#     n=str(i)
#     num=n[::-1]
#     if int(num)==int(i):
#         newnum.append(i)
# print(max(newnum))
#___________________________________________________________________________________________________________
# 6. Write a Python program to find the first negative number in a list using a while loop and break statement.
# l1 = [1,2,-3,4,5,9,-8]
# i = 0
# while i<= len(l1):
#     if l1[i]<0:
#         break
#     i += 1
# print("The index of first negative no is ",i)
#-----------------------------------------------------------------------------------------------------------------
# 7. Write a Python program to print the elements of a list until a specific condition is met using a for loop and break statement.
# l1 = [1,2,3,4,5,18,7,2]
# for i in l1:
#     if i>10:
#         break
#     print(i)
#-------------------------------------------------------------------------------------------------------------------------------
# 8. Write a Python program to search for a specific character in a string using a while loop and break statement.
# str = 'SATARA'
# i = 0
# while i<len(str):
#     if str[i]=='T':
#         break
#     print(str[i],end='')
#     i += 1
#_------------------------------------------------------------------------------------------------------------------------
# 9. Write a Python program to find the first occurrence of a vowel in a string using a for loop and break statement.
# str = 'Thnhgfo'
# vowels = 'aeiou'
# str1 = str.lower()
# for i in range (0,len(str1)):
#     if str1[i] in vowels:
#         break
#     print(str1[i], end='')
# print('The first occurance of vowel is at index', i)
#-----------------------------------------------------------------------------------------------------------------------
# 10. Write a Python program to find the index of the first occurrence of a substring in a string using a while loop and break statement.
str = 'Hello'
substring = 'llo'
index = str.find(substring)
print(index)
