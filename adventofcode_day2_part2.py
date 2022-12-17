# --- Day 2: Rock Paper Scissors ---
# PART 2

from pathlib import Path


def winHand(opponent: str) -> str:
    if opponent == 'A':  # Rock
        return 'B'  # Paper
    elif opponent == 'B':  # Paper
        return 'C'  # Scissors
    elif opponent == 'C':  # Scissors
        return 'A'  # Rock


def loseHand(opponent: str) -> str:
    if opponent == 'A':  # Rock
        return 'C'  # Scissors
    elif opponent == 'B':  # Paper
        return 'A'  # Rock
    elif opponent == 'C':  # Scissors
        return 'B'  # Paper


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
        roundTotal += 0
        plays[1] = loseHand(plays[0])
    elif plays[1] == 'Y':
        roundTotal += 3
        plays[1] = plays[0]
    elif plays[1] == 'Z':
        roundTotal += 6
        plays[1] = winHand(plays[0])
    if plays[1] == 'A':
        roundTotal += 1
    elif plays[1] == 'B':
        roundTotal += 2
    elif plays[1] == 'C':
        roundTotal += 3
    myTotal += roundTotal
print(myTotal)
# correct is 10560



