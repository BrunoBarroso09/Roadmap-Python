#While loop

#With the while loop we can execute a set of statements as long as a condition is true.

#print values while x <= 10
x = 1
while x <= 10:
    print(x)
    x+=1
print("---")
#print values while x is different the 5
y = 1
while y <= 10:
    if y == 5:
        print(y)
        break
    else:
        print(y)
        y+=1
        continue