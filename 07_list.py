#List

#Create list
list = ['string', 2, 12.2, True, ['A', 'B']]

# Access specific element
print(list[0])

# check length of the list
print(len(list))

# change specific element
list[0] = 'Change element'

# Access specific element
print(list[0])

#Append new value to the list
list.append("John")
print(list)

#Insert new value in the list in a specific position
list.insert(1, "Peter")
print(list)

#Remove last value in the list
list.pop()
print(list)

#Access with custom return from the list
print(list[1:4])
