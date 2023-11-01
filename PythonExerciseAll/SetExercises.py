# Set Exercises:
# 1. Write a Python program to find the union of two sets.
# s1 = {10,20,30,40,50}
# s2 = {60,70,80,90,100}
# print(s1,s2)
# print(s1.union(s2))
# 2. Write a Python program to find the intersection of two sets.
# s1={10,20,30,40,50}
# s2 = {10,20,30,70,80}
# print('Intersection=',s1.intersection(s2))
# 3. Write a Python program to check if a set is a subset of another set.
# s1={10,20,30,40,50}
# s2 = {10,20,30}
# if s2.issubset(s1):
#     print('S2 is subset of s1')
# else:
#     print("s2 is not subset of s1")
# 4. Write a Python program to remove duplicate elements from a set.
# l1 = [10,20,30,10,30,45]
# print(set(l1))
# 5. Write a Python program to add an element to a set.
# s1={10,20,30,40,50}
# s1.add(60)
# print(s1)
# 6. Write a Python program to remove an element from a set.
# s1={10,20,30,40,50}
# s1.remove(50)
# s1.discard(40)
# print(s1)
# 7. Write a Python program to find the difference between two sets.
# s1 = {10,20,30,40,50,60,70,80}
# s2 = {10,20,30}
# print(s1-s2)
# 8. Write a Python program to check if two sets are disjoint.
# s1 = {10,20,30}
# s2 = {40,50,60}
# if s1.isdisjoint(s2):
#     print('s1 and s2 are disjoint sets')
# else:
#     print("S1 and s2 are not disjoint sets")
# 9. Write a Python program to find the symmetric difference between two sets.
# s1 = {10,20,30,40,50,60,70,80}
# s2 = {10,20,30}
# print(s1.symmetric_difference(s2))
# 10. Write a Python program to check if a set is empty.
s1 = {10,20,30,40,50,60,70,80}
print(len(s1))
if len(s1)==0:
    print('set is empty')
else:
    print('set is not empty')