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

def calculateScore(playermatrix,i):
    trb = playermatrix[i][3]/1116
    ast = playermatrix[i][4]/906
    stl = playermatrix[i][5]/157
    blk = playermatrix[i][6]/214
    pts = playermatrix[i][7]/2558
    score = trb+ast+stl+blk+pts
    return score

def sortedArray(array):
    array = sorted(array, key=lambda score: score[-1])
    return array

def main():
    nbafile = open ("2017_ALL.csv","r")
    parser = scan(nbafile)
    filelen = file_len("2017_ALL.csv")
    playermatrix = []

    for i in range(filelen):
        player = next(parser)
        playermatrix.append(player)
    playermatrix.pop(0)

    for i in range(0,len(playermatrix)):
        playermatrix[i].append(calculateScore(playermatrix,i))

    playermatrix = sortedArray(playermatrix)
    playermatrix = playermatrix[::-1]

    for i in range(0,len(playermatrix)):
        playermatrix[i].append(calculateScore(playermatrix,i))
        print playermatrix[i]

if __name__ == "__main__":
    main()
