def check_value():
    global cur_val
    global max_val
    cur_val = 0
    max_val = 0


    with open("dag 1/input.txt", "r") as file:
        for line in file:
            line = line.strip("\n")
            if line == "":
                if cur_val > max_val:
                    max_val = cur_val
                    cur_val = 0
                else:
                    cur_val = 0
            else:
                cur_val += int(line) 
    print(max_val)

check_value()