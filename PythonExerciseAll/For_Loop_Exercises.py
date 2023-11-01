# For Loop Exercises:
# 1. Write a Python program to print the numbers from 1 to 10 using a for loop.
# for i in range(1,11):
#     print(i)
# 2. Write a Python program to calculate the sum of all numbers in a list using a for loop.
# l1 = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in l1:
#     sum = sum +i
# print(sum)
# 3. Write a Python program to find the factorial of a number using a for loop.
num = int(input('Enter a no'))
if num == 0:
    print('Factorial of 0 is 1')
elif num < 0:
    print("Factorial does not exist for negative nos")
else:
    fact = 1
    for i in range (1,num+1):
           fact = fact * i
    print(fact)
# 4. Write a Python program to print all the even numbers between 1 and 50 using a for loop.
# for i in range(1,51):
#     if i%2 == 0:
#         print(i)
# 5. Write a Python program to iterate over a string and print each character using a for loop.
# str = 'ashwini'
# for c in str:
#     print(c)
# 6. Write a Python program to iterate over a list of tuples and print each element using a for loop.
# l1 = [(1,2,3),('str',8),('satara',6)]
# for i in l1:
#     for item in i:
#          print(item)
# 7. Write a Python program to find the largest element in a list using a for loop.
# l1 = [10,9,8,7,6,5,100]
# largest_ele = l1[0]
# for i in range(len(l1)):
#     if largest_ele < l1[i]:
#         largest_ele = l1[i]
# print(largest_ele)
# 8. Write a Python program to check if all elements in a list are even using a for loop.
# l1 = [2,4,6,8,10,13]
# for i in l1:
#     res = all(i % 2 == 0 for i in l1)
# if res == True:
#     print("All elements in list are even")
# else:
#     print("All elements in list are not even")
# 9. Write a Python program to find the common elements between two lists using a for loop.
# l1  = [1,2,3,4,5,6]
# l2 = [7,8,9,10,1,2,3,4]
# common= []
# #for i in range (0,len(l1)):
#  #   for j in range(0,len(l2)):
#    #     if l1[i] == l2[j]:
#      #       common.append(l1[i])
# for i in l1:
#     for j in l2:
#         if i == j:
#             common.append(i)
# print(common)

# 10. Write a Python program to calculate the sum of the digits of a number using a for loop.
num = int(input('Enter a no'))
sum = 0
for digit in str(num):
    sum = sum + int(digit)
print(sum)


