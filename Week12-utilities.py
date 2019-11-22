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
