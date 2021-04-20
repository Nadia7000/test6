#1.  Write function for list of integers (create own) which returns list but with each element's index added to itself.
#E.g function_name([0, 1, 3, 5]) => [0, 2, 5, 8]

#num = [1, 2, 4, 5, 8, 9,]
#for index in range(len(num)):
#    print(num[index])





#2. Write function for list of elements (create own) that will return indices of all occurrences of that item in list
#e.g. function_name([ 1, 2, 4, 'b', 'b', 'b', 1], 'b') => [3, 4, 5]
#e.g. function_name([ 1, 2, 4, 'b', 'b', 'b', 1], 1) => [0, 6]
#e.g. function_name([ 1, 2, 4, 'b', 'b', 'b', 1], 'c') => []

#num1 =[3, 5, 'a', 'b', 'c', 6, 8, 9,]
#print(num1[3])


#3. Create a function that takes an integer and returns its length.
#e.g. function_name(8) => 1
#e.g. function_name(88) => 2
#e.g. function_name(83894) => 5
#(Can't use len)

#num =['3', '55', 'ang', 'best', 'desert', '66666', '876321', '9085678321',]
#print(len(num[5]))




#4. Write a function that inverts the keys and values of a dictionary.
#e.g. function_name({ 'a': 'b', 'c': 'd' }) => { 'b': 'a', 'd': 'c' }
#e.g. function_name({ 'fruit': 'apple', 'meat': 'beef' }) => { 'apple': 'fruit', 'beef': 'meat' }

#thisdict =	{
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
#}

#thisdict["year"] = 2018

#print(thisdict)



#5. Create a class with attributes for last name and first name, full name and initials. Add functions to print full name, last name, first name, and initials
#object_name = ClassName('john', 'DOE')
#object_name.attribute_for_name => 'John Doe'
#object_name.attribute_for_last_name => 'Doe'
#object_name.attribute_for_first_name => 'John'
#object_name.attribute_for_initials => 'J.D.'
#object_name.print_full_name() => 'John Doe'

class Person:
    name = 'john'
    lastName = 'Doe'
