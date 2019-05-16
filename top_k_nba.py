import sys

def scan(file):
    linesparsed=0
    while True:
        field = next(file).split(",")
        field = [f.strip() for f in field]
        field = [int(f) for f in field]
        linesparsed+=1
        yield field

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def calculateScore(stat,statmax):
    score = stat/statmax
    return score

def sortedArray(array):
    array = sorted(array, key=lambda score: score[-1])
    return array

def main(argv1,argv2):
    statsarray = argv1.split(',')
    statsarray = [int(stat) for stat in statsarray]
    k = int(argv2)

    for stat in statsarray:
        if(stat == 1):
            trbfile = open("2017_TRB.csv","r")
            trbparser = scan(trbfile)
        elif(stat == 2):
            astfile = open("2017_AST.csv","r")
            astparser = scan(astfile)
        elif(stat == 3):
            stlfile = open("2017_STL.csv","r")
            stlparser = scan(stlfile)
        elif(stat ==4):
            blkfile = open("2017_BLK.csv","r")
            blkparser = scan(blkfile)
        elif(stat == 5):
            ptsfile = open("2017_PTS.csv","r")
            ptsparser = scan(ptsfile)





if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])
