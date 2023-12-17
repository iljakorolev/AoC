import re
from collections import defaultdict

def get_neighbours(x, y, width, height):
    _out = []

    for _x in range(-1, 2):
        for _y in range(-1, 2):
            if _x == 0 and _y == 0:
                continue
            _nx = x + _x
            _ny = y + _y
            
            if 0 <= _nx < width and 0 <= _ny < height:
                _out.append((_nx, _ny))        
    return _out

def part1(input):
    neighbours = []
    total = 0
    
    with open(input) as file:
        # Each line splitted into list
        lines = file.read().split("\n")
        width = len(lines[0])
        height = len(lines)
        # Loop through each line - index each line using enum
        for lidx, line in enumerate(lines):
            # Loop through each character of that line - index each char using enum
            for cidx, c in enumerate(line):
                # Find symbol and get its neighbours coords around the symbol - skip numbers and dot
                if not c.isdigit() and c != ".":
                    neighbours += get_neighbours(lidx,cidx,width,height)

    # Loop through each line
    for i, line in enumerate(lines):
        # Find number and get it's Object
        for match in re.finditer(r"\d+", line):
            # Loop through number start and end index
            for j in range(*match.span()):
                # Break on first match (comparing coords) if number is neighbour to a symbol.
                # Return full number and add it up to total sum.
                if (i, j) in neighbours:
                    total += int(match.group())
                    break
    print("Part1:", total)    

def part2(input):
    neighbours = defaultdict(list)
    gears = defaultdict(list)
    total = 0
    
    with open(input) as file:
        # Each line splitted into list
        lines = file.read().split("\n")
        width = len(lines[0])
        height = len(lines)
        idx = 0
        # Loop through each line - index each line using enum
        for lidx, line in enumerate(lines):
            # Loop through each character of that line - index each char using enum
            for cidx, c in enumerate(line):
                # Find only "gear" symbol and get its neighbours coords around the symbol
                if c == "*":
                    # Add each symbol neighbours as unique key, even if they are on the same line
                    idx += 1
                    neighbours[idx] = get_neighbours(lidx,cidx,width,height)
    
    # Loop through each line
    for i, line in enumerate(lines):
        # Find number and get it's Object
        for match in re.finditer(r"\d+", line):
            # Loop symbol neighbours
            for key,val in neighbours.items():
                # Break on first match (comparing coords) if part number is neighbour to a symbol
                # Append each full number to its unique key
                for j in range(*match.span()):
                    if (i, j) in val:
                        gears[key].append(int(match.group()))
                        break
    
    # Loop through dict and sum up only two numbers of each symbol
    for nums in gears.values():
        if len(nums) == 2:
            total += nums[0]*nums[1]
    print("Part2:", total)

file = "../../AoC_Data/2023/day03/puzzle_input.txt"
part1(file)
part2(file)