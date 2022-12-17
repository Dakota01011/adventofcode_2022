# --- Day 7: No Space Left On Device ---
# Part 1

from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Union, Any

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

dataPath = Path.cwd() / 'adventofcode_day7_input.txt'
with dataPath.open('r') as f:
    pass  # data = f.read()


@dataclass
class myDir:
    name: str = ''
    size: int = 0
    thingsInIt: List = field(default_factory=list)
    parent: Union[Any, None] = None

root = myDir(name='/')
myPwd = root
parsingLs = False
for line in data.split('\n'):
    print(line)
    parts = line.split(' ')
    if line.startswith('$'):
        if parts[1] == 'cd':
            newPath = parts[2]
            if newPath == '..':
                myPwd = myPwd.parent
            elif newPath == myPwd.name:
                continue
            else:
                for d in myPwd.thingsInIt:
                    if d.name == newPath:
                        myPwd = d
        elif parts[1] == "ls":
            continue
    elif parts[0] == 'dir':
        newDir = myDir(name=parts[1], parent=myPwd)
        myPwd.thingsInIt.append(newDir)
    else:
        myPwd.size += int(parts[0])

print(root)
