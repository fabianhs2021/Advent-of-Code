

with open("dag4/input.txt", "r") as file:
    overlap = 0
    for line in file:
        line = line.strip("\n")
        first_element, last_element = line.split(",")
        first_element_1, first_element_2 = first_element.split("-")
        last_element_1, last_element_2 = last_element.split("-")

        if int(last_element_1) > int(first_element_2):
            overlap += 1
        elif int(last_element_2) < int(first_element_1):
            overlap += 1
        else:
            continue

print(1000 - overlap)