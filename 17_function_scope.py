#Scope

value = 100

def my_function():
    global value1
    value1 = 200
    print('Function value: ', value, value1)

my_function()
print(value, value1)

print('------------')

#Nested functions
name = 'John'

def second_function():
    name = 'Peter'
    print('Second function: ', name)

    def thrid_function():
        last_name = 'Grid'
        print('Thrid function: ', name, last_name)

    thrid_function()

second_function()
print(name)