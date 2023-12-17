import re

def part12(input):
    total1 = 0
    total2 = 0
    my_wins = 0
    
    with open(input) as file:
        lines = file.read().split("\n")
        instances = [1 for j in range(len(lines))]
        for line in lines:
            card_value = 0
            my_wins = 0
            
            cards, nums = line.split(" | ")
            win_nums = re.findall(r"\d+", cards)
            my_nums = nums.split()
            for num in win_nums[1:]:
                if num in my_nums:
                    my_wins += 1
                    if card_value == 0:
                        card_value = 1
                    else:
                        card_value *= 2
            total1 += card_value
            
            if my_wins > 0:
                card = int(win_nums[0])
                for i in range(card, my_wins+card):
                    instances[i] += instances[card-1]
            total2 = sum(instances)
            
        print(total1)
        print(total2)      
           
file = "../../AoC_Data/2023/day04/puzzle_input.txt"
part12(file)