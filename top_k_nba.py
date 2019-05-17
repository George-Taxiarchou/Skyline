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
    return array

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
            ptslen = file_len("2017_PTS.csv.csv")+1

    trbend = blkend = astend = stlend = ptsend = 0
    trbmax = blkmax = astmax = stlmax = ptsmax = 0
    firstparse = 0
    playersArray = []

    for i in range(0,4):
        for stat in statsarray:
            if(trbparser!=None):
                token = next(trbparser)
                if(firstparse == 0):
                    trbmax = token[0][1]
                if(token[1] == trblen):
                    trbend = 1
                    print token
                else:
                    print token
            if(astparser!=None):
                token = next(astparser)
                if(firstparse == 0):
                    astmax = token[0][1]
                if(token == astlen):
                    astend = 1
                    print token
                else:
                    print token
            if(stlparser!=None):
                token = next(stlparser)
                if(firstparse == 0):
                    stlmax =  token[0][1]
                if(token == stllen):
                    stlend = 1
                    print token
                else:
                    print token
            if(blkparser!=None):
                token = next(blkparser)
                if(firstparse == 0):
                    blkmax =  token[0][1]
                if(token == blklen):
                    blkend = 1
                    print token
                else:
                    print token
            if(ptsparser!=None):
                token = next(ptsparser)
                if(firstparse == 0):
                    ptsmax =  token[0][1]
                if(token == ptslen):
                    ptsend = 1
                    print token
                else:
                    print token
            firstparse = 1

        if(trbend+blkend+astend+stlend+ptsend == len(statsarray)):
            print trbmax,blkmax
            exit(0)


if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])
