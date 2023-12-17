import re

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
    print(total)    

file = "../../AoC_Data/2023/day03/puzzle_input.txt"
part1(file)