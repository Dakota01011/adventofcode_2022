# --- Day 6: Tuning Trouble ---
# PART 1 - size of 4
# PART 2 - size of 14

from pathlib import Path

data = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""

inputFilePath = Path.cwd() / 'adventofcode_day6_input.txt'
with inputFilePath.open('r') as f:
    data = f.read()

found = False
for i in range(14, len(data), 1):
    possibleMarker = data[i-14:i]
    print(f"{possibleMarker}, {i}")
    for let in possibleMarker:
        if possibleMarker.count(let) > 1:
            break
    else:
        break

print(i)
