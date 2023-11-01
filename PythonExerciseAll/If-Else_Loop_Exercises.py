# If-Else Loop Exercises:
# 1. Write a Python program to check if a number is positive, negative, or zero.
# num = -9
# if num > 0:
#     print("The number is positive")
# elif num < 0:
#     print("The number is negative")
# else:
#     print("The number is zero")
#___________________________________________________________________________________________________________________
# 2. Write a Python program to check if a number is even or odd.
# number = int(input("Enter a number"))
# if number % 2 == 0:
#     print("The number is Even")
# else:
#     print("The number is odd")
#____________________________________________________________________________________________________________________
# 3. Write a Python program to check if a year is a leap year or not.
# year = int(input("Enter the year"))
# if year % 4 ==0:
#     print("The year is leap year")
# else:
#     print("The year is not a leap year")
#__________________________________________________________________________________________________________________
# 4. Write a Python program to find the maximum of three numbers using if-else.
# num1 = int(input("Enter first no."))
# num2 = int(input("Enter second no."))
# num3 = int(input("Enter third no."))
# if num1 > num2 and num1>num3:
#     print(" The greastes no. is num1 ",num1)
# elif num2 > num3 and num2 > num1:
#     print(" The greastes no. is num2 ", num2)
# else:
#     print(" The greastes no. is num3 ", num3)
#_____________________________________________________________________________________________________________________
# 5. Write a Python program to check if a number is prime.
# num = int(input("Enter a no."))
# count =0
# for i in range(1,num+1):
#     if num % i == 0:
#         count +=1
#
# if count>2:
#     print("The number is not prime number")
# else:
#     print("The number is prime number")
#________________________________________________________________________________________________________________________
# 6. Write a Python program to check if a number is divisible by both 3 and 5.
# num = int(input("Enter a no"))
# if num % 3 == 0 and num % 5==0:
#     print('divisible by both 3 and 5')
# else:
#     print('Not divisible by both 3 and 5')
#_____________________________________________________________________________________________________________________
# 7. Write a Python program to check if a character is a vowel or consonant.
# c = input('Enter a character')
# str = 'AEIOUaeiou'
# if c in str:
#     print("vowel")
# else:
#     print('Consonants')
#____________________________________________________________________________________________________________________
# # 8. Write a Python program to check if a given string is a palindrome using if-else.
# str = input("Enter a string")
# rev = str[::-1]
# if str == rev:
#     print('the string is palindrome')
# else:
#     print('The string is not palindrome')
#___________________________________________________________________________________________________________________--
# 9. Write a Python program to determine the largest among three numbers using nested if-else.
# num1 = int(input("Enter first no."))
# num2 = int(input("Enter second no."))
# num3 = int(input("Enter third no."))
# if num1 > num2 and num1>num3:
#     print(" The greastes no. is num1 ",num1)
# elif num2 > num3 and num2 > num1:
#     print(" The greastes no. is num2 ", num2)
# else:
#     print(" The greastes no. is num3 ", num3)
#_________________________________________________________________________________________________________________
# 10. Write a Python program to check if a triangle is equilateral, isosceles, or scalene based on its side lengths using if-else.
side1 = int(input('Enter first side of triangle'))
side2 = int(input('Enter second side of triangle'))
side3 = int(input('Enter third side of triangle'))
if side1 == side2 and side2 == side3:
    print('Equilateral triangle')
elif side1 == side2 or side1==side3:
    print('Isosceles triangle')
else:
    print('Scalene triangle')