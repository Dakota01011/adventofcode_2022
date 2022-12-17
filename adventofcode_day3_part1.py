# --- Day 3: Rucksack Reorganization ---
# PART 1

from pathlib import Path

data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

inputFilePath = Path.cwd() / 'adventofcode_day3_input.txt'
with inputFilePath.open('r') as f:
   data = f.read()

rucksackList = data.split('\n')
commonTypes = []
for rucksack in rucksackList:
    splitpoint = int(len(rucksack) / 2)
    compart1 = rucksack[:splitpoint]
    compart2 = rucksack[splitpoint:]
    for letter in compart1:
        if letter in compart2:
            commonTypes.append(letter)
            break

print(commonTypes)

priorityTotal = 0

for letter in commonTypes:
    if letter.islower():
        priority = ord(letter) - ord('a') + 1
    else:
        priority = ord(letter) - ord('A') + 27
    print(f'{priority} {letter}')
    priorityTotal += priority

print(priorityTotal)
# 7990 is correct
