# --- Day 2: Rock Paper Scissors ---
# PART 1

from pathlib import Path

data = """A Y
B X
C Z"""

inputFilePath = Path.cwd() / 'adventofcode_day2_input.txt'
with inputFilePath.open('r') as f:
    data = f.read()

roundsList = data.split('\n')
myTotal = 0
for aRound in roundsList:
    plays = aRound.split(' ')
    roundTotal = 0
    if plays[1] == 'X':
        roundTotal += 1
        plays[1] = 'A'
    elif plays[1] == 'Y':
        roundTotal += 2
        plays[1] = 'B'
    elif plays[1] == 'Z':
        roundTotal += 3
        plays[1] = 'C'
    if plays[0] == plays[1]:
        roundTotal += 3  # Draw
    else:
        roundWon = plays[0] < plays[1]
        if f"{plays[0]} {plays[1]}" in ['A C', 'C A']:
            roundWon = not roundWon
        if roundWon:
            roundTotal += 6  # Win
    myTotal += roundTotal
print(myTotal)
# 10731 is wrong and too high
# correct is 9651



