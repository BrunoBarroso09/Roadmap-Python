#Set

#A set is a collection which is unordered, unchangeable,
# unindexed, do not allow duplicate values and
# True and 1 are considered the same value in sets, and are treated as duplicates

#Create set
first_set = {'Banana', 'Apple', 'Cherry', 'Apple', True, False, 1, 0}
print(first_set) #Output {'Banana', 'Apple', 'Cherry'} Not allow duplicate values

#Set length
print(len(first_set))

#Add new value in the set
first_set.add("Strawberry")
print(first_set)

#Remove a value from a set
first_set.remove('Banana')
print(first_set)

#A set can contain different data types:
second_set = {"abc", 34, True, 40, "male"}
print(second_set)
#check the type
print(type(second_set))

#Union set's
set1 = {1,2,3,4}
set2 = {5,6,7,8}
set3 = {9,10,11,12}

#First possible to union set's
set4 = set1.union(set2, set3)
print(set4)

#Second option to union set's
set5 = set1 | set2 | set3
print(set5)