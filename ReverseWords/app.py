import os
import sys

def main(fileIn, fileOut):   
    fIn = open(fileIn, 'r')
    fOut = open(fileOut, 'w')
    # Skip the first line
    fIn.readline()
    solve(fIn, fOut)

    fIn.close()
    fOut.close()

def solve(fIn, fOut):    
    for index, line in enumerate(fIn.readlines()):
        line = line.rstrip().split()
        line.reverse()
        print 'Case #%i: %s' % (index + 1, ' '.join(line))
        fOut.write('Case #%i: %s\n' % (index + 1, ' '.join(line)))

if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg, '%s.out' % arg)
    
