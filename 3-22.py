#if 'a' in ['a', 'b', 4]:
#    print('its true')
#elif 4 in ['a', 'b', 4]:
#    print('we\'re in elif')
#else:
#    print('its false')



#fruits = ['apple', 'kiwi', 'lemon', 'mango']


#for fruit in fruits:
#    if fruit == 'kiwi':
#     print('we have {fruit}')
#     print(fruit)

#================================================================================

#list1 = ['string1', 'string2', 'string3']
#list2 = [2, 4, 5, 7, 8, 9, 11, 22, 55, 77]
#print(list2)

#b = list2.index(2)
#print(b)

#a = list2.pop(list2[4])
#print(a)
#print(list2)

#================================================================================

#fruits = ['Apple', 'Banana', 'Tomato', 'Strawberry']

#for index in range(len(fruits)):
#    print(fruits[index])
#    if fruits[index] == 'Banana':
#        fruits[index] = 'Cherry'

#print(fruits)

#=====================================================================================


#fruits = ['Apple', 'Banana', 'Tomato', 'Strawberry']
#for index in range(len(fruits)):
#    if fruits[index] == 'Banana':
#        print('I HAte bananas')
#        continue
#        print('Here continue')
#    else:
#        print(fruits[index])

#==========================================================================================

#fruits = ['Apple', 'Banana', 'Tomato', 'Strawberry']
#for index in range(len(fruits)):
#    if fruits[index] == 'Banana':
#        break
#    else:
#        print(fruits[index])

#============================================================================================


#fruits = ['Apple', 'Banana', 'Tomato', 'Strawberry']
#for index in range(len(fruits)):
#    if fruits[index] == 'Banana':
#        pass
#    else:
#        print(fruits[index])

#===============================================================================================

#a = 5
#b = 10
#c = 3
#d = 7

#def name_for_the_sum():
#    sum1 = a + b
#    print(sum1)

#    sum1 =a + c
#    print(sum1)

#    sum1 = d + c
#    print(sum1)

#name_for_the_sum()

#======================================================================================

# a = 5
# b = 10
# c = 3
# d = 7
#
# sum1 = a + b
# print(sum1)
#
# sum1 =a + c
# print(sum1)
#
# sum1 = d + c
# print(sum1)
#
# def name_for_the_sum(num1, num2):
#     sum1 = num1 + num2
#     print(sum1)
#
# name_for_the_sum(a, b)
# name_for_the_sum(a, c)
# name_for_the_sum(d, c)

#=========================================================================================

# def summing_two_numbers(bird, dog):
#     print(bird, dog)
#
# summing_two_numbers(5, 19)
# summing_two_numbers(a, c)
# summing_two_numbers(d, c)

#===========================================================================================

# def summing_two_numbers(*args):
#     print(args[0] + args[1])
#     sum = 0
#     for number in args:
#         sum += number
#
# summing_two_numbers(5, 19, 10, 128, 128)

