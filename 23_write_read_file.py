# Write and read file

try:
    read_file = open('23_file.txt', 'r')
    print(read_file.read())
except FileNotFoundError:
    print('File not exist and/or is not possible to read.')
    write_file = open('23_file.txt', 'w')
    write_file.write('Hello World!')
    write_file.close()
else:
    print('File was read!')
    read_file.close()
finally:
    read_file = open('23_file.txt', 'r')
    print(read_file.read())