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


def fillRow(rowNum):
    MClist = []
    while True:
        Row =  getInput(rowNum)
        if len(Row) != 3:
            print "Please ensure you enter only 3 numbers!"
            continue
        if isNumber(Row[0]) and isNumber(Row[1]) and isNumber(Row[2]):
            MClist.append(int(Row[0]))
            MClist.append(int(Row[1]))
            MClist.append(int(Row[2]))
            break
        else:
            print "Input is not number, please re-enter"
            continue
    return MClist


def mainGame():
    MClist1 =[]
    MClist2 =[]
    MClist3 =[]

    MClist1 = fillRow(1)
    MClist2 = fillRow(2)
    MClist3 = fillRow(3)

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


while True:
    mainGame()
    choice = raw_input("Would you like to play this again (Y/N) ? =>").upper()
    if choice == "Y":
        continue
    else:
        print "Thanks for playing!"
        break

