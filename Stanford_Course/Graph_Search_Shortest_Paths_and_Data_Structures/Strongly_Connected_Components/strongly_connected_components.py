#!/usr/bin/python2.7
import urllib2

data = urllib2.urlopen('https://d18ky98rnyall9.cloudfront.net/_410e934e6553ac56409b2cb7096a44aa_SCC.txt?Expires=1496188800&Signature=DqU3yW0xafzcfGiTam91VySArpQdDdoSaZ6I2~BiyjmznYHbmaOJDq1jOw1P5dFzNurXra9egOaj~yqs6nkAoUzu08NybJvgvd~AvNqoINavN0C2GVqO21yFQmowcZoXyKZHeDX5JlzNmjyQFnCVx~Nz17VOscGRHKqDrHQ0YL0_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A')
for line in data:
    print line
data.close()

#if __name__ == "__main__":
#	numbers_file = open('SCC.txt', 'r')
#	for i in range(0, 5):
#		print numbers_file[i]
#	numbers_file.close()