a = 1
print(a)
a += 2  # (a = a +2)
a -= 1  # (a = a -1)


a = 'Hello'
print('a'in a)


a = 1
if a == 1:
    print('yeeee')
elif a == 1:
    print('again yeeee')
else:
    print('nooo')


a = 1
b = 3
if a == 1 | b ==4:
    # True or False => True
    # True and False => False
    # False or False => False
    print('yeeee')
elif a == 1 or b != 2:
    print('yeee again')
else:
    print('nope')


list1 = ['string1, string2, string3']
list2 = [list1, 'another string', 42,[1, [23]]]
print(list2)
print(len(list2))
print(list2[-1])
print(list2[1:-1])
list3 = list2[:-2]
print(list3)



list1 = ['string1, string2, string3']
list1.append('string')
print(list1)


list1 = ['string1, string2, string3']
list1[0] = 1
print(list1)
del(list1[0])
print(list1)


list1 = ['string1, string2, string3']
print('string' in list1)

list2 = [1, 2, 3, 4, 10, 0]
print(max(list2))
print(min(list2))


tuple1 = (1, 2, 3, 4, 10, 0)
print(tuple1)

list2 = [1, 2, 3, 4, 10, 0, 10, 0, 10]

list2 = list2.append(14)
print(list2)

list2 = [1, 2, 3, 4, 10, 0, 10, 0, 10]

print(list2)
b = list2.index(2)
print(b)
a = list2.pop(list2[b]-1)
print(a)
print(list2)






list2 = [1, 2, 3, 4, 10, 0, 10, 0, 10]
list2.reverse()
print(list2, list2[::-1])





