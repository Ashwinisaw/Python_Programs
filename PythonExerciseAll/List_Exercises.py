# List Exercises:
# 1. Write a Python program to find the sum of all elements in a list.
# l1 = [2,4,6,8]
# sum = 0
# for i in l1:
#     sum = sum + i
# print(sum)
# 2. Write a Python program to find the maximum and minimum elements in a list.
# l1 = [2,4,6,8]
# max = l1[0]
# min = l1[0]
# for i in l1:
#     if i>max:
#         max = i
#     if i<min:
#         min = i
# print('maximum no =',max)
# print("Minimum no=",min)

# 3. Write a Python program to remove duplicates from a list.
# l1 = [2,4,4,4,'Satara','Satara','Pune',1]
# s1 = set(l1)
# print(s1)
# 4. Write a Python program to check if a list is sorted in ascending order.
# l1 = [2,4,1,6,8]
# print('Original list=',l1)
# l2 = sorted(l1)
# if l1 == l2:
#     print("List is sorted")
# else:
#     print("Given list is not sorted")
# print(l1,l2)

# 5. Write a Python program to find the second largest element in a list.
# l1 = [10,14,16,17,9]
# l2 =sorted(l1,reverse=True)
# print('second largest element in list = ',l2[1])
# 6. Write a Python program to sort a list of strings in alphabetical order.
# l1 = ['Satara','Pune','Sangli','Kolhapur','Mumbai','Goa']
# l2 = sorted(l1)
# print(l2)
# 7. Write a Python program to find the common elements between two lists.
# l1 = [2,4,6,8]
# l2 = [4,8,12,16]
# s1 = set(l1)
# s2 = set(l2)
# common = s1.intersection(s2)
# l2 = list(common)
# print("Common elements are",l2)

# 8. Write a Python program to remove the nth occurrence of an element from a list.
def remele(li,word,n):
    count = 0
    for i in range(0,len(li)):
        if li[i] == word:
            count = count + 1
            if count == n:
               del(li[i])
               return True
    return False
li = ['pune','pune','satara','mumbai','satara']
word = 'mumbai'
n = 1
flag = remele(li,word,n)
if (flag == True):
    print("Updated list is: ", li)
else:
    print("Item not Updated")

# 9. Write a Python program to find the difference between two lists.
# l1 = [2,4,6,8]
# l2 = [4,8,12,16]
# s1 = set(l1)
# s2 = set(l2)
# difference  = s1 - s2
# l2 = list(difference)
# print("different elements are",l2)

# 10. Write a Python program to remove the elements of a list that are divisible by 3.
# li = [2,3,4,5,6,7,8,9]
# lr = [2,3,4,5,6,7,8,9]
# for i in lr:
#     if i%3 == 0:
#         lr.remove(i)
# print("original list=",li)
# print("List after removing",lr)
