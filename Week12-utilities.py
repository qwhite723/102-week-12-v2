#  Incremental Build Model
#  Quintin White
#  CSCI 102-Section B
#  Week 12 Part B

def PrintOutput(word):
    print("OUTPUT",word)

def LoadFile(filename):
    with open(filename, 'r') as file:
        read = file.readlines()
    return read

def UpdateString(string1, string2, index):
    one = []
    RS = ''
    for char in string1:
        one.append(char)
    one[index] = string2
    for let in one:
        RS += let
    return RS

def FindWordCount(my_list, string):
    count = 0
    for value in my_list:
        if value == string:
            count += 1
    return count

def ScoreFinder(names, scores, name):
    uNames = []
    lNames = []
    holder = ''
    index = 0
    for x in names:
        holder  = x
        uNames.append(holder.upper())
        lNames.append(holder.lower())
    if name in names or name in uNames or name in lNames:
        count = 0
        for player in names:
            if player == name:
                index = count
            count += 1
        count = 0
        for player in uNames:
            if player == name:
                index = count
            count += 1
        count = 0
        for player in lNames:
            if player == name:
                index = count
            count += 1
        print("OUTPUT", name, "got a score of", scores[index])
    else:
        print("OUTPUT player not found")

