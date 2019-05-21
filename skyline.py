import sys

def scan(file):
    firsttime=0
    while True:
        field = next(file).split(",")
        field = [f.strip() for f in field]
        if(firsttime!=0):
            for i in range(3,8):
                field[i]=float(field[i])
        firsttime=1
        yield field

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def dominationarray(playermatrix,i,stats):
    scorearray = []
    for stat in stats:
        stat+=2
        if(stat==3):
            trb = playermatrix[i][3]
            scorearray.append(trb)
        elif(stat==4):
            ast = playermatrix[i][4]
            scorearray.append(ast)
        elif(stat==5):
            stl = playermatrix[i][5]
            scorearray.append(stl)
        elif(stat==6):
            blk = playermatrix[i][6]
            scorearray.append(blk)
        elif(stat==7):
            pts = playermatrix[i][7]
            scorearray.append(pts)
    return scorearray

def dominates(player1,player2):
    dominates=False
    nodominance=False
    for i in range(0,len(player1[-1])):
        if(player1[-1][i]>player2[-1][i]):
            dominates=True
        if(player1[-1][i]<player2[-1][i]):
            nodominance=True
    if(dominates==True and nodominance==False):
        return True
    else:
        return False


def main(argv1):

    statsarray = argv1.split(',')
    statsarray = [int(stat) for stat in statsarray]

    for stat in statsarray:
        if stat!=1 and stat!=2 and stat!=3 and stat!=4 and stat!=5:
            print "------Error!!! Stat out of range------"
            exit(0)

    playersfile = open ("2017_ALL.csv","r")
    o = []
    length = file_len("2017_ALL.csv")-1
    parser = scan(playersfile)
    W = []
    T = []

    for i in range(length+1):
        player = next(parser)
        o.append(player)
    o.pop(0)

    for i in range(0,len(o)):
        o[i].append(dominationarray(o,i,statsarray))

    i=0
    while(i<length):
        if(i==0):
            W.append(o[i])

        flag = 0
        for object in W:
            if(dominates(object,o[i])):
                continue
            else:
                for object in W:
                    if(dominates(o[i],object)):
                        W.remove(object)
                    if(flag!=1):
                        W.append(o[i])
                        flag = 1
        i+=1
        print len(W)
    for skylinePlayer in W:
        print skylinePlayer
    print len(W)


if __name__ == "__main__":
    main(sys.argv[1])
