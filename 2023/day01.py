import re

def part1(input):
    total = 0

    with open(input) as file:
        for line in file:
            num = ""
            line = line.rstrip()
            for c in line:
                if c.isdigit():
                    num += c
                    break
            for c in reversed(line):
                if c.isdigit():
                    num += c
                    break
            total += int(num)
        print("Part1:", total)

def part2(input):
    DIGITS = {
        "one"   : 1,
        "two"   : 2,
        "three" : 3,
        "four"  : 4,
        "five"  : 5,
        "six"   : 6,
        "seven" : 7,
        "eight" : 8,
        "nine"  : 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }
    
    total = 0
    
    with open(input) as file:
        for line in file:
            line = line.rstrip()
            newLine = re.findall("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", line)
            total += DIGITS[newLine[0]]*10+DIGITS[newLine[-1]]
        print("Part2:", total)
                
file = "../../AoC_Data/2023/day01/puzzle_input.txt"
part1(file)
part2(file)
       
    