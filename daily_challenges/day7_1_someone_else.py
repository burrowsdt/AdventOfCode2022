# Not my own work!!! This was one of the first Day 7 Python entries I looked at (after I gave up! failure is preserved in another file for posterity) that was concise but not unintelligible. Taken from u/junefish's shared answer on Reddit.

# I figure this is still a win for me. I learned about defaultdict + a good chunk of the anytree module. I do want to try and figure out where I went wrong but I'm moving forward for now.

# import modules
from collections import defaultdict

# initialise variables
terminal_output = []
filepath = []
sizes = defaultdict(int)
total = 0
max_size = 100000

# read input file
with open('data/nospace.txt', 'r') as file:
    for line in file:
        terminal_output.append(line.strip())

# parse input commands
for line in terminal_output:
    # change directories
    if(line.startswith('$ cd')):
        directory = line.split()[-1]
        # go to previous directory
        if(directory == '..'):
            filepath.pop()
        # add directory to filepath
        else:
            filepath.append(directory)
    
    # list contents
    elif(line.startswith('$ ls')):
        continue
    
    # parse ls output for sizes
    else:
        size, _ = line.split()
        if(size.isdigit()):
            size = int(size)
            for i in range(len(filepath)):
                sizes['/'.join(filepath[:i+1])] += size

# calculate sum of directories with size at most 100k
for key, value in sizes.items():
    if(value <= 100_000):
        total += value

# print answer
print(total)