options = ['C B', 'B A', 'C A', 'B C', 'A B', 'A C']
expectedOutcome = [False, False, True, True, True, False]

for ops, exp in zip(options, expectedOutcome):
    parts = ops.split(' ')
    val = parts[0] < parts[1]
    if ops in ['A C', 'C A']:
        val = not val
    if val != exp:
        print("WRONG", end='')
    print(val)

