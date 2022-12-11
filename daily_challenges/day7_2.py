# I adapted the code I "borrowed" to get past the first part to solve the second part. Answer at bottom.

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

# Find required space
total_diskspace = 70000000
min_required = 30000000
current_unused = total_diskspace - sizes["/"]
min_to_clear = min_required - current_unused

# find directories of at least min_to_clear
candidates = []
for key, value in sizes.items():
    if value >= min_to_clear:
        candidates.append(value)
# find lowest value of the candidates
candidates.sort()
        

# print answer - 2568781
print(candidates[0])