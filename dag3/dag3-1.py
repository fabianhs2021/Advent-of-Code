sum = 0
letter = None

with open ("dag3/input.txt", "r") as file:
    for line in file:
        line = line.strip()

        first_half, second_half = line[:len(line)//2], line[len(line)//2:]
        letter = None

        for letter_1 in first_half:
            for letter_2 in second_half:
                if letter_2 == letter_1:
                    letter = letter_2
        if letter.islower():
            sum += ord(letter) - 96
        else:
            sum += ord(letter) - 38          



print(sum)