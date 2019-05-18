import sys

def scan(file):
    linesparsed=0
    while True:
        field = next(file).split(",")
        field = [f.strip() for f in field]
        field = [int(f) for f in field]
        linesparsed+=1
        yield [field,linesparsed]

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def calculateScore(stat,statmax):
    score = float(stat)/float(statmax)
    return score

def sortedArray(array):
    array = sorted(array, key=lambda score: score[-1])
    array = array[::-1]
    return array

def appendedPlayersArray(player,playersArray):
    flag = 0
    if(playersArray==[]):
        playersArray.append(player)
    else:
        for p in playersArray:
            if(player[0][0] == p[0][0]):
                p[2]+=player[2]
                p[-1]+=player[-1]
                flag = 1
        if(flag==0):
            playersArray.append(player)
    return playersArray

def main(argv1,argv2):
    statsarray = argv1.split(',')
    statsarray = [int(stat) for stat in statsarray]
    k = int(argv2)
    trbparser = astparser = stlparser = blkparser = ptsparser= None

    for stat in statsarray:
        if(stat == 1):
            trbfile = open("2017_TRB.csv","r")
            trbparser = scan(trbfile)
            trblen = file_len("2017_TRB.csv")
        elif(stat == 2):
            astfile = open("2017_AST.csv","r")
            astparser = scan(astfile)
            astlen = file_len("2017_AST.csv")
        elif(stat == 3):
            stlfile = open("2017_STL.csv","r")
            stlparser = scan(stlfile)
            stllen = file_len("2017_STL.csv")
        elif(stat ==4):
            blkfile = open("2017_BLK.csv","r")
            blkparser = scan(blkfile)
            blklen = file_len("2017_BLK.csv")
        elif(stat == 5):
            ptsfile = open("2017_PTS.csv","r")
            ptsparser = scan(ptsfile)
            ptslen = file_len("2017_PTS.csv")

    trbend = blkend = astend = stlend = ptsend = 0
    trbmax = blkmax = astmax = stlmax = ptsmax = 0
    firstparse = 0
    playersArray = []
    Wk = [None] * k
    t = -1
    T = 0

    while t<T:
        trbflag = astflag = stlflag = blkflag = ptsflag = 0
        T_Array = []
        if(trbparser!=None and trbflag == 0):
            trbflag = 1
            token = next(trbparser)
            if(firstparse == 0):
                trbmax = token[0][1]
            if(token[1] == trblen):
                trbend = 1
                temptoken = token
                temptoken.append(['trb'])
                temptoken.append(calculateScore(token[0][1],trbmax))
                print temptoken
            else:
                temptoken = token
                temptoken.append(['trb'])
                temptoken.append(calculateScore(token[0][1],trbmax))
                print temptoken
            playersArray = appendedPlayersArray(temptoken,playersArray)
            T_Array.append(temptoken)
        if(astparser!=None and astflag==0):
            astflag = 1
            token = next(astparser)
            if(firstparse == 0):
                astmax = token[0][1]
            if(token[1] == astlen):
                astend = 1
                temptoken = token
                temptoken.append(['ast'])
                temptoken.append(calculateScore(token[0][1],astmax))
                print temptoken
            else:
                temptoken = token
                temptoken.append(['ast'])
                temptoken.append(calculateScore(token[0][1],astmax))
                print temptoken
            playersArray.append(temptoken)
            T_Array.append(temptoken)
        if(stlparser!=None and stlflag == 0):
            stlflag = 1
            token = next(stlparser)
            if(firstparse == 0):
                stlmax =  token[0][1]
            if(token[1] == stllen):
                stlend = 1
                temptoken = token
                temptoken.append(['stl'])
                temptoken.append(calculateScore(token[0][1],stlmax))
                print temptoken
            else:
                temptoken = token
                temptoken.append(['stl'])
                temptoken.append(calculateScore(token[0][1],stlmax))
                print temptoken
            playersArray.append(temptoken)
            T_Array.append(temptoken)
        if(blkparser!=None and blkflag==0):
            blkflag = 1
            token = next(blkparser)
            if(firstparse == 0):
                blkmax =  token[0][1]
            if(token[1] == blklen):
                blkend = 1
                temptoken = token
                temptoken.append(['blk'])
                temptoken.append(calculateScore(token[0][1],blkmax))
                print temptoken
            else:
                temptoken = token
                temptoken.append(['blk'])
                temptoken.append(calculateScore(token[0][1],blkmax))
                print temptoken
            playersArray = appendedPlayersArray(temptoken,playersArray)
            T_Array.append(temptoken)
        if(ptsparser!=None and ptsflag==0):
            ptsflag = 1
            token = next(ptsparser)
            if(firstparse == 0):
                ptsmax =  token[0][1]
            if(token[1] == ptslen):
                ptsend = 1
                temptoken = token
                temptoken.append(['pts'])
                temptoken.append(calculateScore(token[0][1],ptsmax))
                print temptoken
            else:
                temptoken = token
                temptoken.append(['pts'])
                temptoken.append(calculateScore(token[0][1],ptsmax))
                print temptoken
            playersArray.append(temptoken)
            T_Array.append(temptoken)

        if(trbflag+blkflag+astflag+stlflag+ptsflag==len(statsarray)):
            T = 0
            for player in T_Array:
                T += player[3]

        tempWK = sortedArray(playersArray)
        Wk = tempWK
        t = Wk[0][-1]

        if(trbend+blkend+astend+stlend+ptsend == len(statsarray)):
            print "end of file"
            exit(0)
        firstparse = 1

    print "WK"
    for player in Wk:
        print player
    print t
    print T


if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])
