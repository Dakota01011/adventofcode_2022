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
fullyContained = 0
for pair in pairsList:
    elfs = pair.split(',')  # 5-11, 11-94
    elf1 = elfs[0].split('-')  # 5, 11
    elf2 = elfs[1].split('-')  # 11, 94
    elf1s = int(elf1[0])  # 5
    elf1p = int(elf1[1])  # 11
    elf2s = int(elf2[0])  # 11
    elf2p = int(elf2[1])  # 94

    if (elf1s <= elf2s) and (elf2p <= elf1p):  # Elf2 is subset of Elf1
        print(f"({elf1s} <= {elf2s}) and ({elf2p} <= {elf1p}), {pair}")
        #if
        fullyContained += 1
    elif (elf2s <= elf1s) and (elf1p <= elf2p):  # Elf1 is subset of Elf2
        print(f"({elf2s} <= {elf1s}) and ({elf1p} <= {elf2p}), {pair}")
        fullyContained += 1

print(fullyContained)
# 511 is too high
# 501 is too high
