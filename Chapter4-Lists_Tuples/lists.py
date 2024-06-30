# l1=[1,2,4,"Harry"]
# print(l1[2])
#
# l1[0]="Wow" #lists are mutable
# print(l1)
#
# print(l1[0:2])

l1 = [1,8,7,2,21,15]
l1.sort(reverse=True)
l1.sort()
l1.reverse()
print(l1)

l1.append(32)
print(l1)

l1.insert(2,45)
print(l1)

l1.pop(2)
print(l1)

l1.remove(7)
print(l1)

# l1.remove(3)
# print(l1)  Error
