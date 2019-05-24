import sys
from top_keepo import scan,file_len,calculateScore,sortedArray


def parseNext(gphase,playersArray,T_Array,firstparse,trbparser,astparser,stlparser,blkparser,ptsparser,trbflag,astflag,stlflag,blkflag,ptsflag,trblen,astlen,stllen,blklen,ptslen,trbmax,astmax,stlmax,blkmax,ptsmax):
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
        else:
            temptoken = token
            temptoken.append(['trb'])
            temptoken.append(calculateScore(token[0][1],trbmax))
            # print temptoken

        playersArray = appendedPlayersArray(temptoken,playersArray,gphase)
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
            # print temptoken
        else:
            temptoken = token
            temptoken.append(['ast'])
            temptoken.append(calculateScore(token[0][1],astmax))
            # print temptoken
        playersArray = appendedPlayersArray(temptoken,playersArray,gphase)
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
            # print temptoken
        else:
            temptoken = token
            temptoken.append(['stl'])
            temptoken.append(calculateScore(token[0][1],stlmax))
            # print temptoken
        playersArray = appendedPlayersArray(temptoken,playersArray,gphase)
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
            # print temptoken
        else:
            temptoken = token
            temptoken.append(['blk'])
            temptoken.append(calculateScore(token[0][1],blkmax))
            # print temptoken
        playersArray = appendedPlayersArray(temptoken,playersArray,gphase)
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
            # print temptoken
        else:
            temptoken = token
            temptoken.append(['pts'])
            temptoken.append(calculateScore(token[0][1],ptsmax))
            # print temptoken
        playersArray = appendedPlayersArray(temptoken,playersArray,gphase)
        T_Array.append(temptoken)





def appendedPlayersArray(player,playersArray,gphase):
    FILE = 2
    ID = 0

    found = False
    if(playersArray==[]):
        player.append(0)
        playersArray.append(player)
    else:
        for p in playersArray:
            if(player[0][ID] == p[0][ID]):
                p[FILE]+=player[FILE]
                p[3]+=player[3]
                found = True
        if(not found): # if not found add player
            player.append(0)
            playersArray.append(player)
    return playersArray

def updateUpperBounds(Wk,statsarray,T_Array):
    for player in Wk:
        player_upper_bound = 0
        if( len(player[2])==len(statsarray) ): # if found on every line
            player_upper_bound = player[3]    # upper bound is lower bound
            player[-1] = player_upper_bound  # save upper bound
        else:
            for newPlayer in T_Array:
                if newPlayer[2][0] not in player[2]:
                    player_upper_bound += newPlayer[3]
            player_upper_bound += player[3]    # upper bound is lower bound
            player[-1] = player_upper_bound # save upper bound

def main(argv1,argv2):
    #init stats array , k
    statsarray = argv1.split(',')
    statsarray = [int(stat) for stat in statsarray]
    k = int(argv2)
    trbparser = astparser = stlparser = blkparser = ptsparser= None
    #open files
    trblen=astlen=stllen=blklen=ptslen=0
    trbmax = blkmax = astmax = stlmax = ptsmax = 0
    for stat in statsarray:
        if(stat == 1):
            trbfile = open("2017_TRB.csv","r")
            trbparser = scan(trbfile)
            trblen = file_len("2017_TRB.csv")
            trbmax = float(trbfile.readline().split(',')[-1])
        elif(stat == 2):
            astfile = open("2017_AST.csv","r")
            astparser = scan(astfile)
            astlen = file_len("2017_AST.csv")
            astmax = float(trbfile.readline().split(',')[-1])
        elif(stat == 3):
            stlfile = open("2017_STL.csv","r")
            stlparser = scan(stlfile)
            stllen = file_len("2017_STL.csv")
            stlmax = float(trbfile.readline().split(',')[-1])
        elif(stat ==4):
            blkfile = open("2017_BLK.csv","r")
            blkparser = scan(blkfile)
            blklen = file_len("2017_BLK.csv")
            blkmax = float(trbfile.readline().split(',')[-1])
        elif(stat == 5):
            ptsfile = open("2017_PTS.csv","r")
            ptsparser = scan(ptsfile)
            ptslen = file_len("2017_PTS.csv")
            ptsmax = float(trbfile.readline().split(',')[-1])

    trbend = blkend = astend = stlend = ptsend = 0

    firstparse = 0
    playersArray = []
    Wk = []
    t = 0
    prevTarray = T_Array
    gphase = True

    while gphase == True:
        trbflag = astflag = stlflag = blkflag = ptsflag = 0
        T_Array = []
        T = 0

        parseNext(gphase,playersArray,T_Array,firstparse,trbparser,astparser,stlparser,blkparser,ptsparser,trbflag,astflag,stlflag,blkflag,ptsflag,trblen,astlen,stllen,blklen,ptslen,trbmax,astmax,stlmax,blkmax,ptsmax)

        for player in T_Array:
            T+=player[3]
        Wk = sortedArray(playersArray,3)
        t = Wk[ min(k,len(Wk))-1 ][3]

        # if(len(Wk)==trblen):
        #     break

        firstparse = 1

        if( t >= T):
            print "growing phase complete"
            gphase=False
            break
    #endgrowingphase

    updateUpperBounds(playersArray,statsarray,T_Array)

    # W = Wk[0:k]
    W = []
    # while(gphase==False):
    #     trbflag = astflag = stlflag = blkflag = ptsflag = 0
    #     T_Array = []
    #     T=0
    #
    #     parseNext(gphase,playersArray,T_Array,firstparse,trbparser,astparser,stlparser,blkparser,ptsparser,trbflag,astflag,stlflag,blkflag,ptsflag,trblen,astlen,stllen,blklen,ptslen,trbmax,astmax,stlmax,blkmax,ptsmax)
    #
    #     for player in T_Array:
    #         T+=player[3]
    #
    #     updateUpperBounds(Wk,statsarray,T_Array)
    #     Wk = sortedArray(playersArray,3)
    #
    #     # W = Wk[0:k]
    #     t = Wk[k-1][3]
    #
    #     tempupperbounds = sortedArray(playersArray,4)
    #
        for player in tempupperbounds:
            for wplayer in Wk[0:k]:
                if(player[0][0]==wplayer[0][0]):
                    tempupperbounds.remove(player)

        umax = tempupperbounds[0][-1]
    #
        # for i in range(0,len(Wk)-1):
        #     if(Wk[i][3]>=umax):
        #         if(Wk[i] not in W):
        #             W.append(Wk[i])
        #             # Wk.remove(Wk[i])
        #             playersArray.remove(Wk[i])
        #         # print len(W)
        #         if(len(W)==k):
        #             W = sortedArray(W,3)
        #             print "----"
        #             for player in W:
        #                 print player
        #             print "-----"
        #             exit(0)
    #
    #
    #     print t,T
    #
    #     if(t>=umax):
    #         break

        # print umax
        # print len(tempupperbounds)
        # print len(Wk)
        # print len(W)



    for item in playersArray:
        print item
    print len(Wk)





if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])
