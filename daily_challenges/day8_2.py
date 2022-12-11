# Day 8 Challenge 1 - Treetop Tree House

with open("data/treetop.txt", 'r') as f:
    grid = f.read()
grid = grid.splitlines()

# How big is our grid and how many visible trees at border?
length = len(grid[0])
width = len(grid)
visible_border = (length * 2) + (width - 2) * 2

scenic_scores = 0

for row_index, row_contents in enumerate(grid):
    for tree_index, tree_height in enumerate(row_contents):

        top_score = 0
        bottom_score = 0
        left_score = 0
        right_score = 0
        
        # populate top
        if row_index != 0:
            iterator = grid[:row_index]
            if len(iterator) > 1:
                iterator.reverse()
            for i in iterator:
                # top_array.append(i[tree_index])    
                if i[tree_index] >= tree_height:
                    top_score += 1
                    break
                else:
                    top_score += 1
        
        # populate bottom
        if row_index != len(grid) - 1:
            for i in grid[row_index + 1:]:
            # bottom_array.append(i[tree_index])
                if i[tree_index] >= tree_height:
                    bottom_score += 1
                    break
                else:
                    bottom_score += 1
        
        # populate left and right
        if tree_index != 0:
            left_array = list(row_contents[:tree_index].strip(""))
            if len(left_array) > 1:
                left_array.reverse()
            for i in left_array:
                if i >= tree_height:
                    left_score += 1
                    break
                else:
                    left_score += 1

        if tree_index != len(row_contents) - 1:
            right_array = list(row_contents[tree_index + 1:].strip(""))
            for i in right_array:
                if i >= tree_height:
                    right_score += 1
                    break
                else:
                    right_score += 1
        
        total_score = top_score * bottom_score * left_score * right_score
        if total_score > scenic_scores:
            scenic_scores = total_score

# finalVisible = visible_border + tally_visible
# print(finalVisible) # 1733

print(scenic_scores)



    
    
    
    
    
    
    