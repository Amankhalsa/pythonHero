# Create two dice which generate random number from 1-6
# add those numbers up

import random

dice_one = random.randint(1, 6)
dice_two = random.randint(1, 6)

dice_total = dice_one + dice_two

print(f'Dice_one rolled to {dice_one} number and dice_two rolled to {dice_two} which add up to {dice_total}')