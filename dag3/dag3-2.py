from itertools import islice

checked = 0
global letter
letter = None
global svar
svar = 0
line_1 = None
line_2 = None
line_3 = None



with open("dag3/input.txt", "r") as file:
    while checked != 300:
        break_true = False

        lines_gen = list(islice(file, 3))
        stripped = list(map(str.strip, lines_gen))
        line_1, line_2, line_3 = lines_gen[0], lines_gen[1], lines_gen[2]
        for letter_1 in line_1:
            for letter_2 in line_2:
                if letter_2 == letter_1:
                    for letter_3 in line_3:
                        if letter_3 == letter_2:
                            letter = letter_3
                            break_true = True
                            print(letter)
                            break
                        if break_true == True:
                            break

        if letter.islower():
            svar += ord(letter) - 96
        else:
            svar += ord(letter) - 38 
        checked += 3
print(svar)
