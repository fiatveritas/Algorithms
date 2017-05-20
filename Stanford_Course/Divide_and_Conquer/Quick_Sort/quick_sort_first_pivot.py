#!/usr/bin/python2.7
if __name__ == "__main__":
    numbers_file = open('Quick_Sort.txt', 'r')
    unsorted_list = [int(i) for i in numbers_file.read().split()]
    print unsorted_list
    numbers_file.close()