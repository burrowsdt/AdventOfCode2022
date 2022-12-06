# Day 6, Challenge 2 - Tuning
# Change number of distinct characters to 14
# Success - output at bottom
 
# Read in data

with open("data/tuning.txt") as f:
    data = f.read()

# brute force, performance be damned

start_index = 0
end_index = 14

found = False

final_range = []

while found == False:
    current_range = data[start_index:end_index]
    non_dup_tracker = []
    for i in current_range:
        if current_range.count(i) == 1:
            non_dup_tracker.append(i)
            if len(non_dup_tracker) == 14:
                final_range = [start_index, end_index]
                found = True
        elif current_range.count(i) > 1:
            start_index += 1
            end_index += 1
            break
            

print(start_index, end_index)
print("Last character before marker is index " + str(end_index)) # 1275
