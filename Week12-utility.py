def PrintOutput(word):
    print("OUTPUT",word)
    
def LoadFile(filename):
    with open(filename, 'r') as file:
        read = file.readlines()
    return read

def UpdateString(s1, s2, i):
    split = []
    for char in s1:
        split.append(char)
    split[i] = s2
    print("OUTPUT", split)
