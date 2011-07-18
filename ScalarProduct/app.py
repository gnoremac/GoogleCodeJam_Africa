import os
import sys

def main(fileIn, fileOut):   
    fIn = open(fileIn, 'r')
    fOut = open(fileOut, 'w')

    solve(fIn, fOut)

    fIn.close()
    fOut.close()

def solve(fIn, fOut):
    for case in range(int(fIn.readline())):
        count = int(fIn.readline())
        smallest_to_largest = map(int, fIn.readline().split())
        largest_to_smallest = map(int, fIn.readline().split())

        smallest_to_largest.sort(reverse=False)
        largest_to_smallest.sort(reverse=True)
        
        result = 0;
        for i in range(0,count):
            result += smallest_to_largest[i] * largest_to_smallest[i]

        print "Case #%d: %d" % (case + 1, result)
        fOut.write("Case #%d: %d\n" % (case + 1, result))

if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg, '%s.out' % arg)
