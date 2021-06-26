import random


def dicer_sixer():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_3 = random.randint(1, 6)
    dice_4 = random.randint(1, 6)
    dice_5 = random.randint(1, 6)
    i = 0
    while dice_1 != 6 or dice_2 != 6 or dice_3 != 6 or dice_4 != 6 or dice_5 != 6:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        dice_3 = random.randint(1, 6)
        dice_4 = random.randint(1, 6)
        dice_5 = random.randint(1, 6)
        i += 1
        print(
            f'found after {i} turn Dice_1:{dice_1}||Dice_2:{dice_2}||Dice_3:{dice_3}||Dice_4:{dice_4}||Dice_5:{dice_5}')
dicer_sixer()