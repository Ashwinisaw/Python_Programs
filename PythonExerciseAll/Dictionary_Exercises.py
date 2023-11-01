# 1. Write a Python program to iterate over a dictionary and print its keys and values.
# d = {'A':1,'B':2,'C':3,'D':4,'E':5}
# print('Keys =',d.keys())
# print('Values=',d.values())
# print('Key-Value pairs=',d.items())
# for key in d:
#     print(key ,':', d[key])
# 2. Write a Python program to check if a key exists in a dictionary.
# d = {'Name':'Ojal','Class':6,'div':'B'}
# print(d)
# key1 = 'div'
# if key1 in d.keys():
#     print('Key is present in dictionary')
# else:
#     print('Key is not present in dictionary')
# # 3. Write a Python program to get the value associated with a key in a dictionary.
# d = {'Name':'Ojal','Class':6,'div':'B'}
# print(d.get('Name'))
# print(d['Class'])
# # 4. Write a Python program to remove a key from a dictionary.
# d = {'Name':'Ojal','Class':6,'div':'B'}
# d.pop('div')
# print(d)
# 5. Write a Python program to sort a dictionary by its values.
# d = {1:500,2:400,5:100,4:200,3:300}
# print(sorted(d.values()))
# print(sorted(d.keys()))
# print(sorted(d.items()))
# 6. Write a Python program to merge two dictionaries.
# d = {'Name':'Ojal','Class':6,'div':'B'}
# d1 = {1:500,2:400,5:100,4:200,3:300}
# d.update(d1)
# print(d)
# d3 = {**d, **d1}
# print(d3)
# 7. Write a Python program to count the frequency of each element in a dictionary.
from collections import Counter

d = {1:10,2:20,3:25,4:10,5:10,6:10}
print(Counter(d.values()))
# 8. Write a Python program to find the length of a dictionary.
# d1 = {1:500,2:400,5:100,4:200,3:300}
# print(len(d1))
# 9. Write a Python program to check if a dictionary is empty.
# d1 = {1:500,2:400,5:100,4:200,3:300}
# if len(d1)==0:
#     print('The dictionary is empty')
# else:
#     print('The dictionary is not empty')

# 10. Write a Python program to find the keys with the maximum and minimum values in a dictionary.
d = {1:500,2:400,5:100,4:200,3:300}
print(min(d))
print(max(d))
print('Key with maximum value=',max(d,key=d.get))
print('Key with minimum value=',min(d,key=d.get))
