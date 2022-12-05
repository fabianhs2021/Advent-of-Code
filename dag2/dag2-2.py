score = {"R":0, "P":0, "S":0, "W":0, "D":0}

def count():
    with open ("dag2/input.txt", "r") as file:
        for line in file:
            your_hand, outcome = line.strip().split()
            if outcome == "Z":
                score["W"] += 1
                if your_hand == "A":
                    score["P"] += 1
                elif your_hand == "B":
                    score["S"] += 1
                else:
                    score["R"] += 1
                    
            elif outcome =="Y":
                score["D"] += 1
                if your_hand == "A":
                    score["R"] += 1
                elif your_hand == "B":
                    score["P"] += 1
                else:
                    score["S"] += 1
            else:
                if your_hand == "A":
                    score["S"] += 1
                elif your_hand == "B":
                    score["R"] += 1
                else:
                    score["P"] += 1



    score["P"] = score["P"] * 2
    score["S"] = score["S"] * 3
    score["W"] = score["W"] * 6
    score["D"] = score["D"] * 3
def points():
    print(score["R"] + score["P"] + score["S"] + score["W"] + score["D"])
        
count()
points()                    
