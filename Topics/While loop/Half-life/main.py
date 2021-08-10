initial_quantity = int(input())
final_quantity = int(input())
next_quantity = initial_quantity / 2
i = 1
while next_quantity > final_quantity:
    next_quantity /= 2
    i += 1
number_of_half_life_periods = i * 12
print(number_of_half_life_periods)
