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
