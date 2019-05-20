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

def sortedArray(array,i):
    array = sorted(array, key=lambda score: score[i])
    array = array[::-1]
    return array

def appendedPlayersArray(player,playersArray):
    FILE = 2
    ID = 0

    found = False
    if(playersArray==[]):

        playersArray.append(player)

    else:

        for p in playersArray:

            if(player[ID][ID] == p[ID][ID]):

                p[FILE]+=player[FILE]
                p[-1]+=player[-1]

                found = True

        if(not found): # if not found add player
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
    Wk = []
    t = -1
    T = 0

    #growing phase
    while True:
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

        if(trbflag+blkflag+astflag+stlflag+ptsflag == len(statsarray)):
            T = 0
            for player in T_Array:
                T += player[3]

        Wk = sortedArray(playersArray,-1)

        t = Wk[len(Wk) - min(k-1,1) ][-1]
        # if(trbend+blkend+astend+stlend+ptsend == len(statsarray)):
        #     print "end of file"
        #     exit(0)

        firstparse = 1
        if( t >= T):
            print "W K"
            # for item in Wk:
            #     print item
            print len(Wk)
            exit(0)
            break

    #shrinking phase
    prevTarray = T_Array

    for player in Wk:
        player_upper_bound = 0

        if( len(player[2])==len(statsarray) ): # if found on every line
            player_upper_bound = player[-1]    # upper bound is lower bound
            player.append(player_upper_bound)  # save upper bound
        else:
            for newPlayer in T_Array:
                if newPlayer[2][0] not in player[2]:
                    player_upper_bound += newPlayer[-1]
            player_upper_bound += player[-1]    # upper bound is lower bound
            player.append(player_upper_bound)  # save upper bound


    upperboundsarray = sortedArray(Wk,4)
    fcub = upperboundsarray[0][-1]

    t = Wk[k-1][3]

    if(fcub>t):
        print fcub , t
        exit(0)

    while(fcub>t):
        T_Array = []
        trbflag = blkflag =0

        if trbparser!=None and trbflag == 0 :
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
            #playersArray = appendedPlayersArray(temptoken,playersArray)
            T_Array.append(temptoken)

        if blkparser!=None and blkflag==0:
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
            #playersArray = appendedPlayersArray(temptoken,playersArray)
            T_Array.append(temptoken)



        for newPlayer in T_Array:
            for player in Wk:
                if newPlayer[2][0] not in player[2]:
                    idx = T_Array.index(newPlayer)
                    player[2].append(newPlayer[2][0])
                    player[-1] -= prevTarray[idx][-1] - newPlayer[-1]


        prevTarray = T_Array
        Wk = sortedArray(Wk,3)
        print Wk
        t = Wk[k-1][3]

        upperboundsarray = sortedArray(Wk,4)
        fcub = upperboundsarray[0][-1]
        print t,fcub
        if(fcub < t):
            print "from shrinking phase"
            for i in range(0,k):
                print(Wk[i])
            exit(0)
            break

        T = Wk[k-1][-1]


    print('##############################################################')
    print "kekeke"
    print temptoken[1]
    for i in range(0,k):
        print(Wk[i])


if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])
