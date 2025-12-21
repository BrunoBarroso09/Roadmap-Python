#Functions

#declare function
def personalInfo():
    print('Name: John Snow')
    print('Age: 22 \n')

personalInfo()

#declare function with return
def sum():
    result = 0
    for x in range(1,11):
        result += x
    return result

print(sum(), '\n')

#declare function with arguments
def carInfo(brand, year, km):
    print('Brand:', brand, '\nYear:', year, '\nKM:', km, '\n')

carInfo('Renault', 2025, 10000)

#declare function with default arguments
def doorState(state = True):
    if state:
        print('Door is open \n')
    else:
        print('Door is closed \n')

doorState()

#declare function with key arguments
def printABC(a, b, c):
    print('Value A:', a)
    print('Value B:', b)
    print('Value C:', c, '\n')

printABC(c = 1, a = 2, b = 3)

#declare function with flexible arguments
def printArgs(*args):
    for arg in args:
        print('Argument:', arg)

printArgs('Hello', True, 33, ['A', 'B'], ('C', 'D'), {"abc", 34, True, 40, "male"})