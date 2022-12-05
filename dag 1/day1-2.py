def check_value():
    cur_val = 0
    max_val_1 = 0
    max_val_2 = 0
    max_val_3 = 0


    with open("dag 1/input.txt", "r") as file:
        for line in file:
            line = line.strip("\n")
            if line == "":
                if cur_val > max_val_3:
                    if cur_val > max_val_2:
                        if cur_val > max_val_1:
                            max_val_3 = max_val_2
                            max_val_2 = max_val_1
                            max_val_1 = cur_val
                            cur_val = 0
                            continue
                        else:
                            max_val_3 = max_val_2
                            max_val_2 = cur_val
                            cur_val = 0
                            continue
                    else:
                        max_val_3 = cur_val
                        cur_val = 0
                        continue
                else:
                    cur_val = 0
            else:
                cur_val += int(line) 

        print(max_val_1+max_val_2+max_val_3)

check_value()