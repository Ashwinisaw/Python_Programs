# l1 = [2,4,1,5,6,8]
# t = tuple(l1)
# d = {}
# d=dict.fromkeys(l1,)
# print(d)
#___________________________________
# str1 = "Ashwini"
# rev = ''
# for i in range(len(str1)-1,0):
#     rev = rev + str[i]
# print(rev)
#++++++++++++++++++++++++++++++++++++++
# d1 = {}
# for i in range (0,3):
#     key = input('Enter the key')
#     value = input('Enter the value')
#     d1[key]= value
#
# print(d1)
#____________________________________________________
# str1 = "Ashwini"
# rev = ''
# for i in range(len(str1)-1,-1,-1):
#     rev = rev + str1[i]
# print(rev)
#__________________________________________________
l1 = [2,4,1,5,6,8]
d = {}
for i in l1:
    # key = i
    # value = i * i
    d[i] = i ** 2
print(d)