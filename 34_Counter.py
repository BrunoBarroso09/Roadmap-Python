from collections import Counter

#Ex 1 - Using traditional count
fruits = ['Apple', 'Banana', 'Apple', 'Banana', 'Apple', 'Orange']
count = {}
for fruit in fruits:
    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1

print(count)

print('------')
#Ex 2 - Using Counter
count = Counter(fruits)
print(count)

print('------')
#Ex 3 - Find element with most frequently
count_frequently = Counter(fruits)
print(count_frequently.most_common(1))
