# 1. Write a Python program to count the number of characters in a string.
# str = 'CodeNucleus'
# print(len(str))
#_______________________________________________________________________________
# 2. Write a Python program to reverse a string.
# str = 'Codenucleus'
# rev = ''
# for i in range((len(str)-1),-1,-1):
#     rev=rev + str[i]
# print(rev)
#___________________________________________________________________________________
# 3. Write a Python program to check if a string is a palindrome.
# str = input('Enter a string')
# rev = ''
# for i in range((len(str)-1),-1,-1):
#     rev = rev + str[i]
# print("Reverse string=",rev)
# if str==rev:
#     print("The given string",str,"is a palindrome string")
# else:
#     print("The given string", str,"is not a palindrome")
#______________________________________________________________________________________
# # 4. Write a Python program to remove all the vowels from a string.
# vowels ='aeiou'
# str = input('Enter a string')
# str = str.lower()
# str1 = ''
# for i in str:
#     if i not in vowels:
#         str1 = str1 + i
# print("the string without vowels=",str1)
# #______________________________________________________________________________________________
# 5. Write a Python program to find the first non-repeating character in a string.
# from collections import Counter
#
# str = input('Enter a string')
# fre = Counter(str)
# print(fre)
# for i in str:
#     if fre[i] == 1:
#         print("The first non repeating character is", i)
#         break
# _______________________________________________________________________________________
# 6. Write a Python program to capitalize the first letter of each word in a string.
# str = input("Enter a string")
# print(str.title())
#__________________________________________________________________________________________
# 7. Write a Python program to check if a string is an anagram of another string.
# def anagram(str1,str2):
#     flag = 0
#     if sorted(str1) == sorted(str2):
#         flag = 1
#     if flag==1:
#         print("the strings are anagram")
#     else:
#         print('strings are not anagram')
# anagram('table','listen')
# anagram('silent','listen')
#_____________________________________________________________________________________
# from collections import Counter
# # 8. Write a Python program to find the most frequent character in a string.
# str ='geeksforgeeks'
# counter = Counter(str)
# print(counter)
# most_frequent = counter.most_common(1)
# print(most_frequent)
#______________________________________________________________________________________________
# 9. Write a Python program to check if a string is a valid email address.
# import re
# def check(s):
#    # regexp = r'\b[A-Za-z0-9._-+%]+@[A-Za-z0-9.-]+\.[a-zA-Z{2,7}]\b'
#    # regexp = r'\b[A-Za-z0-9._%]+@[A-Za-z0-9.-]+\.[a-zA-Z{2,7}\b'
#     regexp = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
#     if re.match(regexp,s):
#         print("valid email")
#     else:
#         print("Invalid email")
# email='ashwinisawant0@gmail.com'
# email1 = 'codenucleus'
# check(email)
# check(email1)
                                              #______________________________

# from email_validator import validate_email, EmailNotValidError
# def check(email):
#     try:
#         # validate and get info
#         v = validate_email(email)
#         # replace with normalized form
#         email = v["email"]
#         print("True")
#     except EmailNotValidError as e:
#         # email is not valid, exception message is human-readable
#         print(str(e))
# check("my.ownsite@our-earth.org")
# check("ankitrai326.com")

# 10. Write a Python program to find the length of the longest substring without repeating characters.