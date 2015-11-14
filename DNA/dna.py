#DNA alignment

import sys

def LCS(X, Y):
    matrix = [[float('-inf') for x in range(0, len(Y)+1)] for y in range(0, len(X)+1)]
    XX = [[float('-inf') for x in range(0, len(Y)+1)] for y in range(0, len(X)+1)]
    YY = [[float('-inf') for x in range(0, len(Y)+1)] for y in range(0, len(X)+1)]
    matrix[0][0] = 0
    for i in range(0, len(X) + 1):
        XX[i][0] = -(8 + i)
    for i in range(0, len(Y) + 1):
        YY[0][i] = -(8 + i)
    x = 0
    for i in X:
        y = 0
        x  = x + 1
        for j in Y:
            y = y + 1
            if i == j:
                matrix[x][y] = max(matrix[x - 1][y - 1] + 3, XX[x - 1][y - 1] + 3, YY[x - 1][y - 1] + 3)
            else:
                matrix[x][y] = max(matrix[x - 1][y - 1] - 3, XX[x - 1][y - 1] - 3, YY[x - 1][y - 1] - 3)
            XX[x][y] = max(matrix[x-1][y] + (-8), XX[x-1][y] - 1)
            YY[x][y] = max(matrix[x][y-1] + (-8), YY[x][y-1] - 1)
    
    return max(matrix[len(X)][len(Y)], XX[len(X)][len(Y)], YY[len(X)][len(Y)])

try:
    f = open(sys.argv[1],'r')
except IOError:
    print 'Error in opening file.'
    sys.exit(0)

for string in f:
    array =  string.split('|')
    if len(array) > 1:
        print LCS(array[0].strip(), array[1].strip())
f.close()
