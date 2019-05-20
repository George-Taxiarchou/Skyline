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
    Wk = [None]
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
            playersArray = appendedPlayersArray(temptoken,playersArray)
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
            playersArray = appendedPlayersArray(temptoken,playersArray)
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
            playersArray = appendedPlayersArray(temptoken,playersArray)
            T_Array.append(temptoken)

        if(trbflag+blkflag+astflag+stlflag+ptsflag==len(statsarray)):
            T = 0
            for player in T_Array:
                T += player[3]

        Wk = sortedArray(playersArray,-1)
        t = Wk[min(k,len(Wk))-1][-1]

        # if(trbend+blkend+astend+stlend+ptsend == len(statsarray)):
        #     print "end of file"
        #     exit(0)

        firstparse = 1
        if(t>=T):
            print len(Wk)
            break


    #shrinking phase
    while(t>=T):
        # print t,T
        # print "TOPK"
        # for i in range(len(playersArray)):
        #     # print len(Wk)
        #     print Wk[i]
        # exit(0)
        # kappa = 0
        # keepo = 0
        for player in Wk:
            player_upper_bound = 0
            if(len(player[2])==len(statsarray)):
                player_upper_bound = player[-1]
                player.append(player_upper_bound)
            else:
                for tplayer in T_Array:
                    if(tplayer[2][0] not in player[2]):
                        player_upper_bound += tplayer[-1]
                player_upper_bound+=player[3]
                if(len(player)==4):
                    print "keepo"
                    print player
                    print len(player)
                    player.append(player_upper_bound)
                else:
                    print player
                    player[4]=player_upper_bound
                # print T_Array

        # for i in range(0,k):
        #     if(len(Wk[i][2])==len(statsarray)):
        #         kappa = 1
        #     elif(len(Wk[i][2])!=len(statsarray)):
        #         keepo = 1

        for i in range(0,k):
            if(Wk[i][4]<=t):
                print "TOP K RESULT"
                for j in range(0,k):
                    print len(Wk)
                    print Wk[j]
                exit(0)



    print "WK"
    for player in Wk:
        print player
    print t
    print T


if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])
