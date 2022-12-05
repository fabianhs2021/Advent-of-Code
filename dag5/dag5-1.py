stacks = []

for i in range (0, 9):
    stacks.append([])


with open("dag5/input2.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = line.replace("    ", " ")
        line = line.split(" ")
        for i in range (0, len(line)):
            if line[i] != "":
                stacks[i].append(line[i]) 

with open("dag5/input.txt", "r") as file2:
    for line in file2:
        line = line.strip()
        line = line.replace("move", "").replace("to", "").replace("from", "")
        line = line.lstrip(" ")
        line = line.replace("  ", " ")
        line = line.split(" ")
        number = int(line[0])
        from_crate = (int(line[1])-1)
        to_crate = (int(line[2])-1)

        for i in range(0, number):
            stacks[to_crate].insert(0, stacks[from_crate][0])
            stacks[from_crate].pop(0)


for i in range(0, len(stacks)):
    print(stacks[i][0])