# Day 1, Challenge 2 - top 3 - accepted solution
import datetime
start_time = datetime.datetime.now()

with open("data/calories.txt") as f:
    calories = f.read()

calories = calories.splitlines()

topThree = []
currentElf = 0

for num in calories:
    if num != "":
        currentElf += int(num)

    else:
        if len(topThree) < 3:
            topThree.append(currentElf)
        elif currentElf > min(topThree):
            topThree.append(currentElf)
            topThree.sort(reverse = True)
            topThree.pop()

        currentElf = 0

print("Final topThree = {}".format(topThree)) # [70374, 68996, 65240]
print(sum(topThree)) # 204610

end_time = datetime.datetime.now()
print(end_time-start_time)
    
