######################################################################
# File Name:      mergeSort.py                                   
# Author Name:    Baljot Singh 
# Date:           12/18/2015
# Description:    To sort an array of integer using merge sort       
######################################################################

import random
import time

#Helper function to merge arrays
def merge(arr, first, middle, last):
    lowHalf = [] #array for first half
    highHalf = [] #array for second half
    
    #add the first half of array to lowHalf
    for k in range(first, middle + 1):
        lowHalf.append(arr[k])
        
    #add the second half of array to highHalf
    for k in range(middle + 1, last):
        highHalf.append(arr[k])
        
    i = 0
    j = 0
    k = first
    
    #start merging the both halfs back to original array
    while (i < len(lowHalf) and j < len(highHalf)):
        if(lowHalf[i] < highHalf[j]):
            arr[k] = lowHalf[i]
            i = i + 1
        else:
            arr[k] = highHalf[j]
            j = j + 1
            
        k = k + 1
        
    #If any of the half still have elements
    while (i < len(lowHalf)):
        arr[k] = lowHalf[i]
        i = i + 1
        k = k + 1
    
    while (j < len(highHalf)):
        arr[k] = highHalf[j]
        j = j + 1
        k = k + 1
        
#Recursive function for mergesort
def mergeSort(arr, first, last):
    if(first < last):
        middle = (first + last)/2
        mergeSort(arr, first, middle)
        mergeSort(arr, middle + 1, last)
        merge(arr, first, middle, last+1)

if __name__ == "__main__":
    array = []
    count = 0
    
    while count < 1000:
        array.append(random.randint(1,100))
        count = count + 1;
    
    t1 = time.clock()
    mergeSort(array, 0, len(array)-1)
    print time.clock() - t1, "seconds process time"
    print array
