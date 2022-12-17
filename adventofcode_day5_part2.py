# --- Day 5: Supply Stacks ---
# PART 2

from pathlib import Path

data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

inputFilePath = Path.cwd() / 'adventofcode_day5_input.txt'
with inputFilePath.open('r') as f:
    data = f.read()


def convertBoardListToObj(boardIn):
    boardOut = []
    while len(boardIn[-1]):
        boardOut.append([])
        boardIn[-1] = boardIn[-1][4:]
        for i in range(len(boardIn)-2, -1, -1):
            let = boardIn[i][1].strip()
            boardIn[i] = boardIn[i][4:]
            if let:
                boardOut[-1].append(let)
    return boardOut


def makeMoveOnBoard(board, move):
    numMoved = move[0]
    srcPile = move[1]
    dstPile = move[2]
    moved = []
    for _ in range(numMoved):
        let = board[srcPile-1].pop(-1)
        moved.append(let)
    moved.reverse()
    board[dstPile - 1].extend(moved)


boardList = []
boardObj = []
movesList = []
board = True
for line in data.split('\n'):
    if line == '':
        board = False
        boardObj = convertBoardListToObj(boardList)
    elif board:
        boardList.append(line)
    elif not board:
        moves = line.split(' ')
        movesList.append([int(m) for m in moves if m.isdigit()])

for move in movesList:
    makeMoveOnBoard(boardObj, move)


print(boardObj)

for stack in boardObj:
    print(stack[-1], end='')

