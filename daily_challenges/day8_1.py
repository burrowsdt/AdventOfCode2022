# Day 8 Challenge 1 - Treetop Tree House

with open("data/treetop.txt", 'r') as f:
    grid = f.read()
grid = grid.splitlines()

# How big is our grid and how many visible trees at border?
length = len(grid[0])
width = len(grid)
visible_border = (length * 2) + (width - 2) * 2

tally_visible = 0

for row_index, row_contents in enumerate(grid):
    if row_index == 0 or row_index == len(grid) - 1:
        continue
    for tree_index, tree_height in enumerate(row_contents):
        if tree_index == 0 or tree_index == len(row_contents) - 1:
            continue

        top_array = []
        left_array = []
        right_array = []
        bottom_array = []

        # populate top
        for i in grid[:row_index]:
            top_array.append(i[tree_index])

        # populate bottom
        for i in grid[row_index + 1:]:
            bottom_array.append(i[tree_index])
        
        # populate left and right

        left_array = list(row_contents[:tree_index].strip(""))
        right_array = list(row_contents[tree_index + 1:].strip(""))

        combined_arrays = [top_array, bottom_array, left_array, right_array]

        for arr in combined_arrays:
            if any(num >= tree_height for num in arr):
                continue
            else:
                tally_visible += 1
                break
                
finalVisible = visible_border + tally_visible
print(finalVisible) # 1733



    
    
    
    
    
    
    