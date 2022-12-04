# Day 4, Challenge 1 - Camp Cleanup
# Success - 532

# Read in data
with open("data/sections.txt") as f:
    sections = f.read()

sections = sections.splitlines()

containedSections = 0

for line in sections:
    # turn lines into lists with integers separated
    s1, s2 = line.split(sep = ",")
    s1, s2 = s1.split(sep = "-"), s2.split(sep = "-")
    s1, s2 = [eval(i) for i in s1], [eval(i) for i in s2]

    print("s1 = {}; s2 = {}".format(s1,s2))

    if (s1[0] <= s2[0] and s1[1] >= s2[1]) or (s2[0] <= s1[0] and s2[1] >= s1[1]):
        containedSections += 1

print(containedSections)




    