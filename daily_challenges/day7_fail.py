# For posterity, my failed effort to use anytree to create a tree structure and iterate to find the answer. Approached it from several angles and kept winding up with the same (wrong) answer -- not sure what I was doing wrong.
# Day 7, Challenge 1 - No space left on device
# Oh shoot, things just got real....
from anytree import Node, RenderTree, AsciiStyle, PreOrderIter
import re

# Read input

with open("data/nospace.txt") as f:
    data = f.read()

data = data.splitlines()

dict_str = {"/": Node("/")}
current_dir = dict_str["/"]

for line in data:
    if re.search("^\\$ ls", line):
        next
    elif re.search("^\\$ cd", line):
        if re.split("\\s", line)[-1] == "..":
            current_dir = dict_str[current_dir.parent.name]
        elif re.split("\\s", line)[-1] == "/":
            current_dir = dict_str["/"]
        else:
            current_dir = dict_str[re.split("\\s", line)[-1]]
    elif re.search("^dir", line):
        dict_str[re.split("\\s", line)[-1]] = Node(re.split("\\s", line)[-1], parent = current_dir)
    elif re.search("^\\d+", line):
        dict_str[re.split("\\s", line)[0]] = Node(re.split("\\s", line)[0], parent = current_dir)
    
print(dict_str)

# Traverse and log in tally
tally = []
tallyDict = {}
completed = []


def tallyDirs(node):
    # tempTally = 0
    for i in [node.name for node in PreOrderIter(dict_str[node])]:
        if i == node:
            next
        elif re.search("^\\d+", i):
            if tallyDict.get(node) == None:
                tallyDict[node] = int(i)
            elif completed.count(node) == 0:
                tallyDict[node] += int(i)
        else:
            tallyDirs(i)
    completed.append(node)
    # if tempTally <= 100000:
    #   tally.append(tempTally)

tallyDirs("/")

for i in tallyDict.items():
    if i[1] <= 100000:
        tally.append(i[1])

finalSum = sum(tally)

print(finalSum)

# first answer was 1549317 - which I believe was too low. What is wrong?