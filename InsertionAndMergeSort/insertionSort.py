######################################################################
# File Name:      insertionSort.py                                   
# Author Name:    Baljot Singh 
# Date:           12/18/2015
# Description:    To sort an array of integer using insertion sort       
######################################################################

import random
import time

array = []
count = 0

#Create an array of 1000 random integers
while count < 1000:
    array.append(random.randint(1,1000))
    count = count + 1;
    
#timer to get the time for sort
t1 = time.clock()

#insertion sort
for i in range(1, len(array)):
    temp = array[i]
    while i > 0 and array[i - 1] > temp:
            array[i] = array[i - 1]
            i = i - 1
    array[i] = temp
    
print time.clock() - t1, "seconds process time"
print array;
