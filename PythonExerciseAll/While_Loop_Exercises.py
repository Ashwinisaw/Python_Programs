# While Loop Exercises:
# 1. Write a Python program to print the numbers from 1 to 10 using a while loop.
# n=1
# while n <= 10:
#     print(n)
#     n +=1
# 2. Write a Python program to calculate the sum of all numbers from 1 to 100 using a while loop.
# n= 1
# sum = 0
# while n <=100:
#     sum = sum + n
#     n += 1
# print(sum)
# 3. Write a Python program to find the factorial of a number using a while loop.
# i=1
# fact = 1
# num = int(input('Enter a num'))
# while i<=num:
#     fact = fact * i
#     i += 1
# print(fact)

# 4. Write a Python program to print all the even numbers between 1 and 50 using a while loop.
# i = 1
# while i <= 50:
#     if i % 2 == 0:
#         print(i)
#     i +=1
# 5. Write a Python program to iterate over a string and print each character using a while loop.
# str = 'ashwinisawant'
#
# i = 0
# while i<= (len(str)-1):
#     print(str[i])
#     i +=1
# 6. Write a Python program to iterate over a list of tuples and print each element using a while loop.
# l1 = [(1,2,3),('A','B',4),(6,8,'A')]
# i = 0
# while i<= (len(l1)-1):
#     print(l1[i])
#     i +=1
# 7. Write a Python program to find the largest element in a list using a while loop.
# l1 = [10,20,300,40,50,60,70]
# i = 0
# max = l1[0]
# while i <= (len(l1)-1):
#     if l1[i] >= max:
#         max = l1[i]
#     i +=1
# print(max)
# 8. Write a Python program to check if all elements in a list are even using a while loop.
# l1 = [10,20,30,40,50,65]
# i = 0
# while i <= (len(l1)-1):
#     if all(number % 2 == 0 for number in l1):
#         flag = 1
#
#     else:
#         flag = 0
#     i +=1
# if flag == 1:
#     print('All elements are even')
# else:
#     print('All elements are not even')

# 9. Write a Python program to find the common elements between two lists using a while loop.
# l1 = [10,20,30,40,50,60]
# l2 = [10,20,60]
# common  = set(l1).intersection(set(l2))
# print(common)
# 10. Write a Python program to calculate the sum of the digits of a number using a while loop.
num = int(input('enter a no'))
sum = 0
while num > 0:
    remainder = num % 10
    sum  = sum + remainder
    num = num // 10
print(sum)
