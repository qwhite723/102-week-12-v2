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

def Union(list1, list2):
    temp = list1 + list2
    final = []
    filler = 0
    for value in temp:
        if value in final:
            filler += 1
        else:
            final.append(value)
    return final

def Intersection(uno, dos):
    fin = []
    for name in uno:
        if name in dos:
            fin.append(name)
    return fin
        
def NotIn(uno, dos):
    finn = []
    filler = 0
    for name in uno:
        if name in dos:
            filler += 1
        else:
            finn.append(name)
    return finn


