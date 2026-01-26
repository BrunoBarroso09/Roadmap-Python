# String format

value1 = 10.45
value2 = 33.54
result = value1 + value2
print(f"Math operation {result:.2f}$")

print("---")

#Percentage
value = 0.2575
print(f"Value: {value:.2%}")

print("---")

#Format in table with modifiers
print(f"|{"Name":^15}|{"Email:":^20}|")
print(f"|{"Peter Grid":^15}|{"pgrid@gmail.com:":^20}|")
print(f"|{"Anna Freud":^15}|{"afreud@gmail.com:":^20}|")