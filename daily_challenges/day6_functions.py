# Read in data

with open("data/tuning.txt") as f:
    data = f.read()



def tuning(data, num): # num = num of distinct characters
    start_index = 0
    end_index = num

    found = False
    final_range = []

    while found == False:
        # set window to examine
        current_range = data[start_index:end_index]
        non_dup_tracker = []
        for i in current_range:
            # if unique, add to non_dup_tracker
            if current_range.count(i) == 1:
                non_dup_tracker.append(i)
                # if there are *num* unique characters found, end program
                if len(non_dup_tracker) == num:
                    final_range = [start_index, end_index]
                    found = True
            #if more than 1 of a character found, move to next window
            elif current_range.count(i) > 1:
                start_index += 1
                end_index += 1
                break
    
    return end_index

four_chr = tuning(data, 4)
fourteen_chr = tuning(data, 14)

print("Four distinct characters: Last character before marker is index " + str(four_chr)) # 1275
print("Fourteen distinct characters: Last character before marker is index " + str(fourteen_chr)) # 3605
