# AoC 2022 Day 3 Challenge 2 - Rucksack Reorg cont

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

# Perform search for every three lines
found_dups = []

for step in range(0, 300, 3):
    tempDict = {}
    l1, l2, l3 = set(rucksack[step]), set(rucksack[step+1]), set(rucksack[step+2]) 
    print("l1 = {} \n l2 = {} \n l3 = {}".format(l1, l2, l3))
    for letter in l1:
        tempDict[letter] = 1
    for letter in l2:
        if tempDict.get(letter):
            tempDict[letter] +=1
        else:
            tempDict[letter] = 1
    for letter in l3:
        if tempDict.get(letter) == 2:
            found_dups.append(alpha_dict[letter])
            
    # print(tempDict)
    print(found_dups)
    print("Length =" + str(len(found_dups)))
    print(sum(found_dups))




#     tempDict = {}    
#     for letter in l1:
#         if tempDict.get(letter) == True:
#             print("Already looked")
#             next
#         elif p2.find(letter) != -1:
#             found_dups.append(alpha_dict[letter])
#             print("Duplicate found! It's {}".format(letter))
#             break
#         else:
#             tempDict[letter] = True
#     print(found_dups)
# print(sum(found_dups))