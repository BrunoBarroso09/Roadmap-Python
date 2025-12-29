#try except

try:
    print(name)
except NameError:
    print("The variable is not defined.")
else:
    print("Everything is all right.")
finally:
    print("This always happens, regardless of whether there is an error or not.")