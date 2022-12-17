# --- Day 7: No Space Left On Device ---
# PART 1

from pathlib import Path
from dataclasses import dataclass, field
from typing import List

data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


@dataclass
class myDir:
    dirName: str = ''
    dirSize: int = 0
    thingsInDir: List = field(default_factory=list)


inputFilePath = Path.cwd() / 'adventofcode_day7_input.txt'
with inputFilePath.open('r') as f:
    pass#data = f.read()

system = myDir('/')
myPwd = system
scanningLs = False
for line in data.split('\n'):
    if line.startswith('$'):
        scanningLs = False
        parts = line.split(' ')
        if (parts[1] == 'cd') and (myPwd.dirName != parts[2]):
            newDir = myDir(parts[2])
            myPwd.thingsInDir
            myPwd =
        elif parts[1] == 'ls':
            scanningLs = True

    if scanningLs:





