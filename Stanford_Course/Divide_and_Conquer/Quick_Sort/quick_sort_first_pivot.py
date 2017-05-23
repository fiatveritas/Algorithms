#!/usr/bin/python2.7

first_comparison = 0
last_comparison = 0
median_comparison = 0

#A method for partition around the first element of the array
def partition_first(array, left_end, right_end):
    pivot = array[left_end]
    i = left_end + 1
    for j in range(left_end + 1, right_end):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    left_endval = array[left_end]
    array[left_end] = array[i-1]
    array[i-1] = left_endval
    return i - 1 

#A method for partitioning around the last element of the array
def partition_last(array, left_end, right_end):
    
    pivot = array[right_end - 1]
    array[right_end - 1] = array[left_end]
    array[left_end] = pivot
    
    i = left_end + 1
    for j in range(left_end + 1, right_end):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    left_endval = array[left_end]
    array[left_end] = array[i - 1]
    array[i - 1] = left_endval
    return i - 1 

#A method to calculate the median of three numbers using two comparisons
def median(a, b, c):
    if (a - b) * (c - a) >= 0:
        return a
    elif (b - a) * (c - b) >= 0:
        return b
    else:
        return c

#A method to partition around the median
def partition_median(array, left_end, right_end):
    left = array[left_end]
    right = array[right_end - 1]
    length = right_end - left_end
    if length % 2 == 0:
        middle = array[left_end + length/2 - 1]
    else:
        middle = array[left_end + length/2]

    pivot = median(left, right, middle)
    pivotindex = array.index(pivot) #only works if all values in array unique
    array[pivotindex] = array[left_end]
    array[left_end] = pivot

    i = left_end + 1
    for j in range(left_end + 1, right_end):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    left_endval = array[left_end]
    array[left_end] = array[i - 1]
    array[i - 1] = left_endval
    return i - 1 

    
#Implement quicksort while partitioning around the first index
def quick_sort1(array, leftindex, rightindex):
    global first_comparison
    if leftindex < rightindex:
        
        newpivotindex = partition_first(array, leftindex, rightindex)
        first_comparison += (rightindex - leftindex - 1)
        quick_sort1(array, leftindex, newpivotindex) 
        quick_sort1(array, newpivotindex + 1, rightindex)
        
def quicksort_last(array, leftindex, rightindex):
    global last_comparison
    if leftindex < rightindex:
        newpivotindex = partition_last(array, leftindex, rightindex)
        last_comparison += (rightindex - leftindex - 1)
        quicksort_last(array, leftindex, newpivotindex)
        quicksort_last(array, newpivotindex + 1, rightindex)

 
def quicksort_median(array, leftindex, rightindex):
     global median_comparison
     if leftindex < rightindex:
         newpivotindex = partition_median(array, leftindex, rightindex)
         median_comparison += (rightindex - leftindex - 1)
         quicksort_median(array, leftindex, newpivotindex)
         quicksort_median(array, newpivotindex + 1, rightindex)

if __name__ == "__main__":
    numbers_file = open('Quick_Sort.txt', 'r')
    unsorted_list = [int(i) for i in numbers_file.read().split()]
    unsorted_list_2 = unsorted_list[:]
    unsorted_list_3 = unsorted_list[:]
    quick_sort1(unsorted_list, 0, len(unsorted_list))
    print first_comparison
    quicksort_last(unsorted_list_2, 0, len(unsorted_list_2))
    print last_comparison
    quicksort_median(unsorted_list_3, 0, len(unsorted_list_3))
    print median_comparison
    numbers_file.close()