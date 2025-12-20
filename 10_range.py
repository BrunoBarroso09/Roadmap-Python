#Range function

# Function range works with 2 option arguments

#Omit the first argument | if you omit the first arg the range start in 0
for i in range(6):
    print(i)

#The second arg is not included, so it's 1 to 10
print('----')
for x in range(1,11):
    print(x)

#The third argument means that it starts at 0 and goes from 2 to 2.
print('----')
for y in range(0,11,2):
    print(y)