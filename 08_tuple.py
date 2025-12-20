#Tuples

#Create tuple
fruit = ('Banana', 'Apple', 'Cherry', 'Strawberry', 'Pineapple')

#Print the ffirst item in the tuple:
print(fruit[0])

#Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
#But there are some workarounds.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

#Convert tuple into list
this_list = list(fruit)
#Update the element in first position to Kiwi
this_list[1] = 'Kiwi'
#Convert listo into tuple
fruit = tuple(this_list)
print(fruit)

#Join tuples
tuple_1 = ('Banana', 'Apple', 'Cherry')
tuple_2 = (1, 2, 3)

tuple_3 = tuple_1 + tuple_2
print(tuple_3)
print(len(tuple_3))