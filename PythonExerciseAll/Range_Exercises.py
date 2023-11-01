# Range Exercises:
# 1. Write a Python program to iterate over a range of numbers and print them.
# for item in range (101,151):
#     print(item)
#  2. Write a Python program to find the sum of all numbers in a range.
# sum = 0
# for item in range (10,19):
#     sum = sum + item
# print(sum)
# 3. Write a Python program to print all even numbers in a given range.
# print('The even numbers from 1 to 100 are:')
# for item in range(1,101):
#     if item % 2 == 0:
#         print(item,end=' ')
# 4. Write a Python program to print all odd numbers in a given range.
# print('The even numbers from 1 to 100 are:')
# for item in range(1,101):
#     if item % 2 != 0:
#         print(item,end=' ')
# 5. Write a Python program to find the average of all numbers in a range.
# num = int(input('Enter the total number'))
# sum = 0
# for item in range(1,num):
#     sum =+ item
# avg = sum / num
# print('Average=',avg)
# 6. Write a Python program to check if a number is present in a given range.
# num = int(input('Enter a no'))
# if num in range(1,100):
#     print('The number is present in given range')
# else:
#      print('The number is not present in given range')
# 7. Write a Python program to reverse a range of numbers and print them.
# for n in reversed(range(5)):
#     print(n)
# 8. Write a Python program to find the product of all numbers in a range.
# product = 1
# for item in range(1,6):
#     product = product * item
# print('The product of all numbers in given range =',product)
# 9. Write a Python program to print the squares of all numbers in a range.
# for item in range(1,11):
#     square = item * item
#     print('The square of ', item ,'=', square )
# 10. Write a Python program to print the cube of all numbers in a range.
for item in range(1,11):
    cube = item ** 3
    print('The cube of ', item ,'=', cube )