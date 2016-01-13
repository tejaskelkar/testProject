import random


def isNumber(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def getInput(row):
    temp = raw_input("Row %s (3 values) =>" % row)
    Row = temp.split(" ")
    return Row


def mainGame():
    MClist1 =[]
    MClist2 =[]
    MClist3 =[]

    while True:
        Row1 =  getInput(1)
        if isNumber(Row1[0]) == True and isNumber(Row1[1]) == True and isNumber(Row1[2]) == True:
            MClist1.append(int(Row1[0]))
            MClist1.append(int(Row1[1]))
            MClist1.append(int(Row1[2]))
            break
        else:
            print "Input is not number, please re-enter"
            continue

    while True:
        Row2 =  getInput(2)
        if isNumber(Row2[0]) == True and isNumber(Row2[1]) == True and isNumber(Row2[2]) == True:
            MClist2.append(int(Row2[0]))
            MClist2.append(int(Row2[1]))
            MClist2.append(int(Row2[2]))
            break
        else:
            print "Input is not number, please re-enter"
            continue

    while True:
        Row3 =  getInput(3)
        if isNumber(Row3[0]) == True and isNumber(Row3[1]) == True and isNumber(Row3[2]) == True:
            MClist3.append(int(Row3[0]))
            MClist3.append(int(Row3[1]))
            MClist3.append(int(Row3[2]))
            break
        else:
            print "Input is not number, please re-enter"
            continue

    print MClist1
    print MClist2
    print MClist3

    hTotal1 = sum(MClist1)
    hTotal2 = sum(MClist2)
    hTotal3 = sum(MClist3)

    vTotal1 = MClist1[0] + MClist2[0] + MClist3[0]
    vTotal2 = MClist1[1] + MClist2[1] + MClist3[1]
    vTotal3 = MClist1[2] + MClist2[2] + MClist3[2]

    dTotal1 = MClist1[0] + MClist2[1] + MClist3[2]
    dTotal2 = MClist1[2] + MClist2[1] + MClist3[0]



    if hTotal1 == hTotal2 == hTotal3 == vTotal1 == vTotal2 == vTotal3 == dTotal1 == dTotal1:
        print "Congratulations! You found a Magic Square!"
    else:
        print "Not a Magic Square, Try again!"


mainGame()

