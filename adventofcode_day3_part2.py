# --- Day 3: Rucksack Reorganization ---
# PART 2

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
for i in range(0, len(rucksackList), 3):
    elf1 = rucksackList[i]
    elf2 = rucksackList[i+1]
    elf3 = rucksackList[i+2]
    commonTypesR1 = [letter for letter in elf1 if letter in elf2]
    commonTypes.extend([letter for letter in set(commonTypesR1) if letter in elf3])

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
# 2602 is correct
