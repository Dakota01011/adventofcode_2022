# --- Day 4: Camp Cleanup ---
# PART 1

from pathlib import Path

data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

inputFilePath = Path.cwd() / 'adventofcode_day4_input.txt'
with inputFilePath.open('r') as f:
   data = f.read()

pairsList = data.split('\n')
overlap = 0
for pair in pairsList:
    elfs = pair.split(',')  #
    elf1 = elfs[0].split('-')  #
    elf2 = elfs[1].split('-')  #
    elf1s = int(elf1[0])  #
    elf1p = int(elf1[1])  #
    elf2s = int(elf2[0])  #
    elf2p = int(elf2[1])  #

    if (elf1s <= elf2s) and (elf2p <= elf1p):  # Elf2 is subset of Elf1
        overlap += 1
    elif (elf2s <= elf1s) and (elf1p <= elf2p):  # Elf1 is subset of Elf2
        overlap += 1
    elif (elf2s <= elf1s) and (elf1s <= elf2p):  # Elf1 start is within Elf2
        overlap += 1
    elif (elf2s <= elf1p) and (elf1p <= elf2p):  # Elf1 ends is within Elf2
        overlap += 1
    elif (elf1s <= elf2s) and (elf2s <= elf1p):  # Elf2 start is within Elf1
        overlap += 1
    elif (elf1s <= elf2p) and (elf2p <= elf1p):  # Elf2 ends is within Elf1
        overlap += 1

print(overlap)
