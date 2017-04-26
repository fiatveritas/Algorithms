#!/usr/bin/python2.7
def merge_sort(alist):
    counter = 0
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


#alist = [54,26,93,17,77,31,44,55,20]
#merge_sort(alist)
#print(alist)

if __name__ == "__main__":
    numbers_file = open('integerArray.txt', 'r')
    unsorted_list = [int(i) for i in numbers_file.read().split()]
    print merge_sort(unsorted_list)
    print unsorted_list
    numbers_file.close()