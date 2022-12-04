# AoC 2022 Day 3 Challenge 1 - Rucksack Reorg
# success! 7553
# May come back and refactor after the second challenge...

# Generate letter-value pairs

alphabet = []
values = []

for letter in range(97,123):
    alphabet.append(chr(letter))

for letter in range(65,91):
    alphabet.append(chr(letter))

for i in range(1, 53):
    values.append(i)

alpha_dict = dict(zip(alphabet, values))

# Read in data
with open("data/rucksack.txt") as f:
    rucksack = f.read()

rucksack = rucksack.splitlines()

# Divide given line in two
found_dups = []

for line in rucksack:
    p1, p2 = line[:int(len(line)/2)], line[int(len(line)/2):]
    print("p1 = {}, p2 = {}".format(p1, p2))

    tempDict = {}    
    for letter in p1:
        if tempDict.get(letter) == True:
            print("Already looked")
            next
        elif p2.find(letter) != -1:
            found_dups.append(alpha_dict[letter])
            print("Duplicate found! It's {}".format(letter))
            break
        else:
            tempDict[letter] = True
    print(found_dups)
print(sum(found_dups))