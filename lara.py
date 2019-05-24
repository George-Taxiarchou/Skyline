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

def appendedPlayersArray(player,playersArray,growing):
    FILE = 2
    ID = 0

    found = False
    if(playersArray==[]):
        playersArray.append(player)
    else:
        for p in playersArray:
            if(player[ID][ID] == p[ID][ID]):
                p[FILE]+=player[FILE]
                p[3]+=player[3]
                found = True
        if(not found and growing == True): # if not found add player
            playersArray.append(player)
    return playersArray



def main(argv1,argv2):
    statsarray = argv1.split(',')
    statsarray = [int(stat) for stat in statsarray]
    k = int(argv2)
    trbparser = astparser = stlparser = blkparser = ptsparser= None
    trbmax = blkmax = astmax = stlmax = ptsmax = 0
    trblen=astlen=blklen=ptslen=stllen = 0

    playersArray = []
    for stat in statsarray:
        if(stat == 1):
            trbfile = open("2017_TRB.csv","r")
            trbparser = scan(trbfile)
            trblen = file_len("2017_TRB.csv")
            with open('2017_TRB.csv') as f:
                trbmax = float(f.readline().split(',')[-1])
                f.close()
        elif(stat == 2):
            astfile = open("2017_AST.csv","r")
            astparser = scan(astfile)
            astlen = file_len("2017_AST.csv")
            with open('2017_AST.csv') as f:
                astmax = float(f.readline().split(',')[-1])
                f.close()
        elif(stat == 3):
            stlfile = open("2017_STL.csv","r")
            stlparser = scan(stlfile)
            stllen = file_len("2017_STL.csv")
            with open('2017_STL.csv') as f:
                stlmax = float(f.readline().split(',')[-1])
                f.close()
        elif(stat ==4):
            blkfile = open("2017_BLK.csv","r")
            blkparser = scan(blkfile)
            blklen = file_len("2017_BLK.csv")
            with open('2017_BLK.csv') as f:
                blkmax = float(f.readline().split(',')[-1])
                f.close()
        elif(stat == 5):
            ptsfile = open("2017_PTS.csv","r")
            ptsparser = scan(ptsfile)
            ptslen = file_len("2017_PTS.csv")
            with open('2017_PTS.csv') as f:
                ptsmax = float(f.readline().split(',')[-1])
                f.close()

    filelen = max(trblen,astlen,blklen,ptslen,stllen)

    #extreme if more than existing players get asked
    if(k>filelen):
        k = filelen

    growing = True
    Wk = []
    firsttime=0
    prevTarray = []

    while True:
        T_Array  = []
        trbflag = astflag = stlflag = blkflag = ptsflag = 0
        if(trbparser!=None and trbflag == 0):
            trbflag = 1
            token = next(trbparser)
            if(token[1] == trblen):
                trbend = 1
                temptoken = token
                temptoken.append(['trb'])
                temptoken.append(calculateScore(token[0][1],trbmax))
                temptoken[0].pop(-1)
            else:
                temptoken = token
                temptoken.append(['trb'])
                temptoken.append(calculateScore(token[0][1],trbmax))
                temptoken[0].pop(-1)
            playersArray = appendedPlayersArray(temptoken,playersArray,growing)
            T_Array.append(temptoken)

        if(astparser!=None and astflag==0):
            astflag = 1
            token = next(astparser)
            if(token[1] == astlen):
                astend = 1
                temptoken = token
                temptoken.append(['ast'])
                temptoken.append(calculateScore(token[0][1],astmax))
                temptoken[0].pop(-1)
            else:
                temptoken = token
                temptoken.append(['ast'])
                temptoken.append(calculateScore(token[0][1],astmax))
                temptoken[0].pop(-1)
            playersArray = appendedPlayersArray(temptoken,playersArray,growing)
            T_Array.append(temptoken)

        if(stlparser!=None and stlflag == 0):
            stlflag = 1
            token = next(stlparser)

            if(token[1] == stllen):
                stlend = 1
                temptoken = token
                temptoken.append(['stl'])
                temptoken.append(calculateScore(token[0][1],stlmax))
                temptoken[0].pop(-1)
            else:
                temptoken = token
                temptoken.append(['stl'])
                temptoken.append(calculateScore(token[0][1],stlmax))
                temptoken[0].pop(-1)
            playersArray = appendedPlayersArray(temptoken,playersArray,growing)
            T_Array.append(temptoken)

        if(blkparser!=None and blkflag==0):
            blkflag = 1
            token = next(blkparser)

            if(token[1] == blklen):
                blkend = 1
                temptoken = token
                temptoken.append(['blk'])
                temptoken.append(calculateScore(token[0][1],blkmax))
                temptoken[0].pop(-1)
            else:
                temptoken = token
                temptoken.append(['blk'])
                temptoken.append(calculateScore(token[0][1],blkmax))
                temptoken[0].pop(-1)

            playersArray = appendedPlayersArray(temptoken,playersArray,growing)
            T_Array.append(temptoken)

        if(ptsparser!=None and ptsflag==0):
            ptsflag = 1
            token = next(ptsparser)
            if(token[1] == ptslen):
                ptsend = 1
                temptoken = token
                temptoken.append(['pts'])
                temptoken.append(calculateScore(token[0][1],ptsmax))
                temptoken[0].pop(-1)
            else:
                temptoken = token
                temptoken.append(['pts'])
                temptoken.append(calculateScore(token[0][1],ptsmax))
                temptoken[0].pop(-1)

            playersArray = appendedPlayersArray(temptoken,playersArray,growing)
            T_Array.append(temptoken)

        if(trbflag+blkflag+astflag+stlflag+ptsflag == len(statsarray)):
            T = 0
            for player in T_Array:
                T += player[3]

        if(growing == True):

            lowerbounds = sortedArray(playersArray,3)

            t = lowerbounds[min(k-1,len(lowerbounds)-1)][3]

            if(len(statsarray)==1):
                W = lowerbounds
                if(len(lowerbounds)==k):
                    print "\t\tTOP-K"
                    print "------------------------------------------"
                    for lb in playersArray:
                        print lb
                    print "------------------------------------------"
                    print "\t  lines parsed: " + temptoken[1].__str__()
                    exit(0)

            if(t>=T and len(statsarray)!=1):
                growing = False
                Wk = lowerbounds[0:k]
            prevTarray = T_Array

        else:
            if(firsttime==0):
                for player in playersArray:
                    player_upper_bound = 0
                    if( len(player[2])==len(statsarray) ): # if found on every line
                        player_upper_bound = player[3]    # upper bound is lower bound
                        player.append(player_upper_bound)  # save upper bound
                    else:
                        for newPlayer in T_Array:
                            if newPlayer[2][0] not in player[2]:
                                player_upper_bound += newPlayer[3]
                        player_upper_bound += player[3]    # upper bound is lower bound
                        player.append(player_upper_bound)  # save upper bound
                firsttime=1


            elif(firsttime==1):
                for player in playersArray:
                    player_upper_bound = 0
                    if(len(player[2])==len(statsarray) ): # if found on every line
                        player_upper_bound = player[3]    # upper bound is lower bound
                        player[4]=player_upper_bound  # save upper bound
                    else:
                        for newPlayer in T_Array:
                            if newPlayer[2][0] not in player[2]:
                                player_upper_bound += newPlayer[3]
                        player_upper_bound += player[3]    # upper bound is lower bound
                        player[4]=player_upper_bound # save upper bound



            lowerbounds = sortedArray(playersArray,3)
            upperbounds = sortedArray(playersArray,4)

            W = []

            ub = upperbounds[0][-1]

            #extreme pruning play
            prevub = ub
            for player in lowerbounds:
                if(player[3]>=ub):
                    W.append(player)
                    upperbounds.remove(player)
                    upperbounds = sortedArray(upperbounds,4)
                    if(len(W)>=k):
                        print "\t\tTOP-K"
                        print "------------------------------------------"
                        W = sortedArray(W,3)
                        for w in W[0:k]:
                            print w
                        print "------------------------------------------"
                        print "\t  lines parsed: " + temptoken[1].__str__()
                        exit(0)

                    if(upperbounds!=[]):
                        ub = upperbounds[0][-1]
                        prevub = ub
                    else:
                        ub = prevub



            if(len(W)>=k):
                print "\t\tTOP-K"
                print "------------------------------------------"
                W = sortedArray(W,3)
                for w in W[0:k]:
                    print w
                print "------------------------------------------"
                print "\t  lines parsed: " + temptoken[1].__str__()
                exit(0)

            seenAll = 0
            for player in playersArray:
                if(len(player[2])==len(statsarray)):
                    seenAll+=1
            if(seenAll >= len(playersArray)):
                print "\t\tTOP-K"
                print "------------------------------------------"
                W = sortedArray(W,3)
                for w in W[0:k]:
                    print w
                print "------------------------------------------"
                print "\t  lines parsed: " + temptoken[1].__str__()
                exit(0)

            t = lowerbounds[min(k-1,len(lowerbounds)-1)][3]

            #extreme pruning play

            prevTarray = T_Array


if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])
