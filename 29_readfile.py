with open("29_file.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
        print(f"{line}")