# Day 5.1 - Supply Stacks
# Success - answer at bottom
# Super crude to start with but shouldn't be hard to refactor later

import re

# Read in data, but have to do some extra work to parse

with open("data/stacks.txt") as f:
    init_data = f.read()

init_data = init_data.splitlines()
stacks = init_data[:init_data.index("")]
steps = init_data[init_data.index(""):]
del steps[0]

# turn stacks into lists/arrays

stacks.reverse()
del stacks[0]

# to make code a bit more human readable/trackable, putting stacks in a labeled dict

#init dict
stack_dict = {}

#create and populate stacks
for num in range(1,10):
    name = "stack_" + str(num)
    stack_dict[name] = []

initial_arrays = []
for num in range (0, 9):
    initial_arrays.append([])

for line in stacks:
    items = re.sub("    ", "*", line)
    items = items.replace("[","").replace("]","").replace(" ", "")
    i = 0
    for item in items:
        if item != "*":
            initial_arrays[i].append(item)
        i += 1

stack_dict = dict(zip(stack_dict, initial_arrays))

# # Parse steps into lists
for step in steps:
    num_to_move, from_stack, to_stack = re.findall("\\d+", step)
    from_stack = "stack_" + from_stack
    to_stack = "stack_" + to_stack
    
    items_to_move = stack_dict[from_stack][-int(num_to_move):]
    items_to_move.reverse()
    stack_dict[to_stack].extend(items_to_move)
    del stack_dict[from_stack][-int(num_to_move):]

print(stack_dict)

# get final top items
top_items = []
for key in stack_dict.keys():
    top_items.append(stack_dict[key][-1])

top_items = "".join(top_items)

print(top_items) # Success - MQSHJMWNH




    

    



