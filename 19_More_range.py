#More about range
#range(Start, End, Step

x = range(1,10)
print(list(x))
print('Value: ', x[2])
check = 5 in x
print(check)

print('------')

y = x[:6]
print(list(y))
print(len(y))