import random

rolls = 20  # Number of times to roll the die
count_6 = 0
count_1 = 0
two_6 = 0
previous_roll = 0

for i in range(rolls):
    current_roll = random.randint(1, 6)
    
    if current_roll == 6:
        count_6+= 1
        if previous_roll == 6:
            two_6+= 1
    
    if current_roll == 1:
        count_1+= 1
    
    previous_roll = current_roll

print("Number of times 6 was rolled:", count_6)
print("Number of times 1 was rolled:", count_1)
print("Number of times two 6s were rolled in a row:", two_6)
