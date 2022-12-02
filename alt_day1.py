# Day 1, Challenge 2 - top 3 - accepted solution
import datetime
start_time = datetime.datetime.now()

with open("calories.txt") as f:
    calories = f.read()

calories = calories.splitlines()

topThree = [0,0,0]
currentElf = 0

for num in calories:
    if num != "":
        currentElf += int(num)

    elif currentElf > min(topThree):
        topThree.append(currentElf)
        topThree.sort(reverse = True)
        topThree.pop()

        currentElf = 0
    
    else:
        currentElf = 0

print("Final topThree = {}".format(topThree)) # [70374, 68996, 65240]
print(sum(topThree)) # 204610

end_time = datetime.datetime.now()
print(end_time-start_time)
    
