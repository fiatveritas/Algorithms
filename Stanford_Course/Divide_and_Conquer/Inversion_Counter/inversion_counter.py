#!/usr/bin/python2.7
def merge_sort(to_sort):
    if len(to_sort) > 1:
        [left_half, right_half] = divide(to_sort)
        #print x1,x2
        left_half, leftInv = merge_sort(left_half)
        right_half, rightInv = merge_sort(right_half)
        #print leftInv,rightInv
        merged, splitInv = merge(left_half, right_half)
        #print splitInv
        return merged,(leftInv + rightInv + splitInv)
    else:
        return to_sort, 0


def divide(to_sort):
    size = len(to_sort)
    half_size = size / 2
    left_half = []
    right_half = []
    for index in xrange(0, half_size):
        left_half.append(to_sort[index])
    for index in xrange(half_size, size):
        right_half.append(to_sort[index])
    return [left_half, right_half]


def merge(left_half, right_half):
    sorted_list = []
    left_half_index = 0
    right_half_index = 0
    inv_count = 0
    size1 = len(left_half)
    size2 = len(right_half)
    while (left_half_index < size1 and right_half_index < size2):
        if left_half[left_half_index] <= right_half[right_half_index]:
            sorted_list.append(left_half[left_half_index])
            left_half_index += 1
        else:
            sorted_list.append(right_half[right_half_index])
            right_half_index += 1
            inv_count += size1 - left_half_index

    for i in range(left_half_index, size1):
         sorted_list.append(left_half[i])

    for i in range(right_half_index, size2):
         sorted_list.append(right_half[i])

    return sorted_list, inv_count

#alist = [54,26,93,17,77,31,44,55,20]
#print merge_sort(alist)
#print(alist)

if __name__ == "__main__":
    numbers_file = open('integerArray.txt', 'r')
    unsorted_list = [int(i) for i in numbers_file.read().split()]
    print merge_sort(unsorted_list)
    #print unsorted_list
    numbers_file.close()