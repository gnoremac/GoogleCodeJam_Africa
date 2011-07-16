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
        credit = int(fIn.readline())
        items = int(fIn.readline())
        values = map(int, fIn.readline().split(' '))
        for x in range(items):        
            for n in range(x + 1, items):
                if (values[x] + values[n]) ==  credit:
                    print 'Case #%s: %i %i' % (case + 1, x + 1, n + 1)
                    fOut.write('Case #%s: %i %i\n' % (case + 1, x + 1, n + 1))

if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg, '%s.out' % arg)
