# Continue Statement Exercises:
# 1. Write a Python program to print all the even numbers between 1 and 20 except for the number 10 using a for loop and continue statement.
# for i in range (1,21):
#     if i%2 == 0:
#         if i==10:
#             continue
#         print(i)
# 2. Write a Python program to print the elements of a list skipping the negative numbers using a while loop and continue statement.
# l1  = [-1,2,-3,9,9,7]
# i = 0
# while i<=(len(l1)-1):
#     if l1[i]<0:
#         i +=1
#         continue
#     print(l1[i])
#     i +=1
# # 3. Write a Python program to print the first 10 multiples of 3 except for the number 9 using a for loop and continue statement.
# for i in range(1,11):
#     #if i==9:
#     if (i*3)==9:
#         continue
#     print(3*i)
# 4. Write a Python program to iterate over a string and print only the consonants using a for loop and continue statement.
# str = 'my name is Ashwini'
# str1 = str.lower()
# vowels ='aeiou'
# for i in str1:
#     if i in vowels:
#         continue
#     print(i,end='')

# 5. Write a Python program to print the elements of a list skipping the even numbers using a while loop and continue statement.
# l1 = [1,2,3,4,5,6,7,8,9,10]
# i = 0
# while i<=(len(l1)-1):
#     if l1[i]%2 == 0:
#         i +=1
#         continue
#     print(l1[i])
#     i +=1
# 6. Write a Python program to find the sum of all numbers between 1 and 100, excluding the multiples of 5 using a for loop and continue statement.
# sum = 0
# for i in range(1,101):
#     if i%5 == 0:
#         continue
#     sum = sum + i
# print(sum)
# 7. Write a Python program to print the uppercase letters in a string using a while loop and continue statement.
# str = 'SAtaRA'
# i = 0
# while i <= (len(str)-1):
#     if str[i].islower():
#         i +=1
#         continue
#     print(str[i],end='')
#     i +=1
# 8. Write a Python program to print the elements of a list skipping the elements divisible by 3 using a for loop and continue statement.
# l1 = [1,2,3,4,5,6,7,8,9,10]
# i = 0
# while i<=(len(l1)-1):
#    if l1[i]%3 == 0:
#        i +=1
#        continue
#    print(l1[i])
#    i +=1
# 9. Write a Python program to iterate over a list of tuples and print only the tuples with a specific condition using a while loop and continue statement.
l1 = [(4,2,6),(4,8,12),(3,6,9)]
i = 0
while i <= (len(l1)-1):
    if sum(l1[i]) % 4 == 0:
       print(l1[i])
       i += 1

# 10. Write a Python program to print the numbers from 1 to 50, skipping the multiples of 7 using a for loop and continue statement.
# for i in range(1,51):
#     if i % 7 == 0:
#         continue
#     print(i,end='  ')