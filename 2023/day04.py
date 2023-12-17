import re

def part1(input):
    total = 0
    
    with open(input) as file:
        lines = file.read().split("\n")
        for line in lines:
            card_value = 0
            
            cards, nums = line.split(" | ")
            win_nums = re.findall(r"\d+", cards)
            my_nums = nums.split()
            for num in win_nums[1:]:
                if num in my_nums:
                    if card_value == 0:
                        card_value = 1
                    else:
                        card_value *= 2
            total += card_value
            
        print(total)           
file = "../../AoC_Data/2023/day04/puzzle_input.txt"
part1(file)