#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

first_dict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "colors": ["red", "white", "blue"]
}
print(first_dict)

#Print the "brand" value of the dictionary:
print(first_dict['brand'])

#Check length
print(len(first_dict))

#Check type
print(type(first_dict))

#Print only items
print(first_dict.items())

#Print only only keys
print(first_dict.keys())

#Print only only values
print(first_dict.values())

#update values from a key
first_dict["year"] = 2025
print(first_dict)

#Remove key
del first_dict["year"]
print(first_dict)

#Clear dictionary
first_dict.clear()
print(first_dict)