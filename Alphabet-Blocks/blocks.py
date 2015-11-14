import sys

def stringMatch(X, arr):
    if not X:
        return False
    arr1 = []
    X = X.strip()
    X = X.upper()
    dic1 = {}
    dic2 = {}
    count = 0
    for i in X:
        count = X.count(i)
        if count:
            dic1[i] = count
        count = 0
            
    cnt = 0
    for j in X:
        for i in arr:
            if j in i:
                cnt = cnt + 1
                if i not in arr1:
                    arr1.append(i)
        if cnt:
            dic2[j] = cnt
        cnt = 0
    
    dic3 = dict(dic1)
    #dic4 = dict(dic2)
    cout = 0
    for k in dic1:
        if k in dic2:
            if dic2[k] < dic1[k]:
                return False
            elif dic2[k] == dic1[k]:
                good = False
                for i in range(0, dic1[k]):
                    for i in range(0, len(arr1)):
                        if k in arr1[i]:
                            cout = cout + 1
                            good = True
                            del arr1[i]
                            if k in dic3:
                                del dic3[k]
                                #del dic4[k]
                                #del dic2[k]
                                
                            break
                if cout != dic1[k]:
                    return False
                            
        else:
            return False
        cout = 0
    count = 0
    if len(dic3) == 0:
        return True
    
    for k in dic3:
        count = count + dic3[k]
    
    if count <= len(arr1):
        return True
    return False
                            
#creates a file object for input and output
try:
    f = open(sys.argv[1],'r')
except IOError:
    print 'Error in opening file block.txt'
    sys.exit(0)

for string in f:
    array =  string.split('|')
    str1 = ""
    arr = []
    cnt = 0
    r = 0
    if len(array) >= 3:
        str2 = (array[2].strip()).upper()
        for i in str2:
            r = r + 1
            if r % 7 != 0:
                if i != '\n':
                    str1 = str1 + i
                    cnt = cnt + 1
                    if cnt == 6:
                        arr.append(str1)
                        str1 = ""
                        cnt = 0
        print stringMatch(array[1], arr)
f.close()
