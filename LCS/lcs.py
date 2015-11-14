import sys
#longest common subsequence
def LCS(X, Y):
    matrix = [[0 for x in range(0, len(Y)+1)] for y in range(0, len(X)+1)]
    x = 0
    lcs = []
    for i in X:
        y = 0
        x  = x + 1
        for j in Y:
            y = y + 1
            if i == j:
                matrix[x][y] = matrix[x - 1][y - 1] + 1
            else:
                matrix[x][y] = max(matrix[x - 1][y], matrix[x][y - 1])
    
    i = len(X)
    j = len(Y)
    while i > 0 and j > 0:
        if matrix[i][j] == matrix[i-1][j]:
            i = i - 1
        
        elif matrix[i][j] == matrix[i][j - 1]:
            j = j - 1
        
        elif matrix[i][j] == matrix[i-1][j-1] + 1:
            lcs.append(X[i - 1])
            i = i - 1
            j = j - 1
    
    return matrix[len(X)][len(Y)], lcs
    
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    array = test.split(';')
    length, lcs = LCS(array[0], array[1])
    lcs.reverse()
    print "".join(lcs)
test_cases.close()
