######################################################################
# File Name:      mergeSortedArrays.py                                   
# Author Name:    Baljot Singh 
# Date:           12/18/2015
# Description:    To merge sorted arrays       
######################################################################

#Function to merge two sorted arrays
def mergeArrays(twoArrays, sortedArray, lo, hi):
    i = 0
    j = 0
    while (i < len(twoArrays[lo]) and j < len(twoArrays[hi])):
        #if element of first array is less than element of second array
        if(twoArrays[lo][i] < twoArrays[hi][j]):
            sortedArray.append(twoArrays[lo][i])
            i = i + 1
        else:
            sortedArray.append(twoArrays[hi][j])
            j = j + 1
    
    #If there are still elements in any of array
    while (i < len(twoArrays[lo])):
        sortedArray.append(twoArrays[lo][i])
        i = i + 1
    
    while (j < len(twoArrays[hi])):
        sortedArray.append(twoArrays[hi][j])
        j = j + 1
        
if __name__ == "__main__":
    
    #An array of sorted arrays
    arrayOfSortedArrays = [[300, 305, 509, 908, 9089], [1,2,3,4,21,25], [100, 900, 9001, 10000], [-3,-1,2,4,5,30],[-2,4,10,19], [54, 56, 89, 100, 105]]
    #An array which will be passed to mergeArrays function as set of two arrays
    twoArray = []
    #This array will be sorted array returned from mergeArrays function
    sortedArray = []
    
    #Append the first two arrays of sorted arrays
    twoArray.append(arrayOfSortedArrays[0])
    twoArray.append(arrayOfSortedArrays[1])

    mergeArrays(twoArray, sortedArray, 0, len(twoArray) - 1)
    index = 2
    while index < len(arrayOfSortedArrays):
        twoArray[0] = sortedArray
        twoArray[1] = arrayOfSortedArrays[index]
        sortedArray = []
        mergeArrays(twoArray, sortedArray, 0, len(twoArray) - 1)
        index = index + 1
        
    for i in range(0,len(sortedArray)):
        print sortedArray[i]
