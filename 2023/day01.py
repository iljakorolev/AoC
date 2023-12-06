input = "../../AoC_Data/2023/day01/puzzle_input.txt"

num1 = num2 = ""
total = 0

with open(input) as file:
    for line in file:
        line = line.rstrip()
        for c in line:
            if c.isdigit():
                num1 = c
                break
        for c in line[ : :-1]:
            if c.isdigit():
                num2 = c
                break
        total += int(num1 + num2)
    print(total)