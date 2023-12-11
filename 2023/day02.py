import re

def part12(input):
    total1 = 0
    total2 = 0
    with open(input) as file:
        for line in file:
            line = line.rstrip()
            game, sets = line.split(":")
            red = re.findall(r"(\d+) (red)", sets)
            maxRed = max([int(i[0]) for i in red])
            green = re.findall(r"(\d+) (green)", sets)
            maxGreen = max([int(i[0]) for i in green])
            blue = re.findall(r"(\d+) (blue)", sets)
            maxBlue = max([int(i[0]) for i in blue])
            if maxRed <= 12 and maxGreen <= 13 and maxBlue <= 14:
                total1 += int(re.findall(r"\d+", game)[0])
            total2 += maxRed * maxGreen * maxBlue
            
        print("Part1:", total1)
        print("Part2:", total2)
        
file = "../../AoC_Data/2023/day02/puzzle_input.txt"
part12(file)
       
    