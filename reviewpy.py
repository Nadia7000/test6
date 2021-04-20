# #  instance v = different values can be
# #  Class  variable- one value
# # init= for def var to use in dif methods and with different value
# # https://stackoverflow.com/questions/38377276/instance-variables-in-methods-outside-the-constructor-python-why-and-how
# class Car:
#     wheels = 4
#
#     def __init__(self, brand, color):
#         self.color = color
#         self.brand = brand
#
#     def print_car_color(self):
#         print(self.color)
#
#     def print_car_brand(self):
#         # self.a = "b"  # var in def
#         print(self.brand)
#
#     def print_wheels(self):
#         print(Car.wheels)
#
#     def print_all(self):
#         print(f'{self.color} {self.brand} has {Car.wheels} wheels')
#
# #
# my_car = Car('jeep', 'black')
# your_car = Car('toyota', 'brown')
# #
# my_car.print_car_color()
# my_car.print_car_brand()
# my_car.print_wheels()
# #
# your_car.print_car_color()
# your_car.print_car_brand()
# your_car.print_all()

# # static def = doesnt requred instans to call
# NOTE: for code (line 39-44) to work move to line 25
   # @staticmethod
   # def print_cls_wheels():
   #     print(Car.wheels)

# #
# # Car.print_cls_wheels()

#=================================================================================================



#sorted dict



# vegetables_dict = {1:'carrot', 9:'pea', 5:'potato', 2:'squash'}
# new_dict = sorted(vegetables_dict, key=lambda k: int(k))
# new_dict = sorted(vegetables_dict.items(), key=lambda kv_pair: kv_pair[0])
# new_dict1 = sorted(vegetables_dict.items(), key=lambda kv_pair: kv_pair[1])
# print(new_dict)
# print(new_dict1)


# dictionary =Словари используются для хранения значений данных в парах ключ: значение. key:value , key =unique
#a_dictionary = {'a': 1, "b": 2, 3:'c', 3:'ab', 4:'ab'}
#
# print(a_dictionary)
# #
# a_dictionary['a'] = 3
# print(a_dictionary)
# #
# a_dictionary['test'] = 123
# print(a_dictionary)
# #
# print(len(a_dictionary))
# # #
# print(a_dictionary[1:3])

# key = 'ck'
# if key in a_dictionary:
#     print(f'{key} in {a_dictionary}')
# else:
#     print(f'{key} not in {a_dictionary}')


# b_dictionary = {'a': 1, 'b': 2, 15:1}
# print(b_dictionary)
# reversed_dictionary = {}
# for k, v in b_dictionary.items():
#     reversed_dictionary[v] = k
# print(reversed_dictionary)

#
# a_dictionary = {'a': 1, 'b': 2, 3:'c', 3:'ab', 4:'ab'}
# looking_for = 'ab'
# for k, v in a_dictionary.items():
#     if v == looking_for:
#         print(k)

#====================================================================================================


# # return
#def number_of_digits_in_list():
#   l = [1, 2, 3]
 #  return len(l)


#n = number_of_digits_in_list()


# obj = to save the value and use later

#def n_in_use_after_return(x):
 #   print(x + 5)

#n_in_use_after_return(n)


# def n2_in_use_after_return(x):
#     print(x + l)
#
#
# n2_in_use_after_return(n)
#
#
#def number_of_digits_in_list_insert(value,):
#   return len(str(value))


#print(number_of_digits_in_list_insert(1234))


# HW : understand code and explain for next class
#def digits(value):
#     result = 0
#     while value >= 1:
#         result += 1
#         value = value / 10
#     return result
#
#
 #print(digits(99999090394005556987950))

