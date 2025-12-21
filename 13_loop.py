#For loop

fruits_list = ['Apple', 'Cherry', 'Banana']

#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

#Loop list
print('---List---')
for fruit in fruits_list:
    print(fruit)

#Loop tuple
fruits_tuple = ('Apple', 'Cherry', 'Banana')

print('\n---Tuple---')
for fruit in fruits_tuple:
    print(fruit)

#Loop set
fruits_set = {'Apple', 'Cherry', 'Banana'}

print('\n---Set---')
for fruit in fruits_set:
    print(fruit)

#Loop string
new_string = "This is a string"

print('\n---String---')
for string in new_string:
    print(string)