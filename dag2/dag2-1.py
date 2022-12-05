score = {"X":0, "Y":0, "Z":0, "W":0, "D":0}

def count():
    with open ("dag2/input.txt", "r") as file:
        for line in file:
            your_hand, my_hand = line.strip().split()
            score[my_hand] += 1

            if my_hand == "Y":
                if your_hand == "B":
                    score["D"] += 1
                elif your_hand == "A":
                    score["W"]+= 1
                else:
                    continue

            if my_hand == "X":
                if your_hand == "B":
                    continue
                elif your_hand == "A":
                    score["D"]+= 1
                else:
                    score["W"] += 1

            if my_hand == "Z":
                if your_hand == "B":
                    score["W"] += 1
                elif your_hand == "A":
                    continue
                else:
                    score["D"] += 1

    score["Y"] = score["Y"] * 2
    score["Z"] = score["Z"] * 3
    score["W"] = score["W"] * 6
    score["D"] = score["D"] * 3
def points():
    print(score["X"] + score["Y"] + score["Z"] + score["W"] + score["D"])
        
count()
points()                    
