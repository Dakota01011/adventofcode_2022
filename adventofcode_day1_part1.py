# How many total Calories is that Elf carrying?

from pathlib import Path

data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

inputFilePath = Path.cwd() / 'adventofcode_day1_input.txt'
with inputFilePath.open('r') as f:
    data = f.read()

dataList = data.split('\n')
calTots = [0]
for calEntry in dataList:
    if calEntry == '':
        calTots.append(0)
    else:
        calTots[-1] += int(calEntry)

print(calTots)
calTots.sort(reverse=True)
print(calTots[:3])
print(sum(calTots[:3]))

