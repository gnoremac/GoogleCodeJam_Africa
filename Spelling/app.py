import os
import sys
import array

def main(fileIn, fileOut):   
    fIn = open(fileIn, 'r')
    fOut = open(fileOut, 'w')
    # Skip the first line
    fIn.readline()
    solve(fIn, fOut)

    fIn.close()
    fOut.close()


ascii_a  = ord('a')
ints  = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
mult  = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,4,1,2,3,1,2,3,4]

def map_char(c):
    ascii_c = ord(c)
    if ascii_c == 32:
        return ['0']
    return [str(ints[ascii_c - ascii_a]) * mult[ascii_c - ascii_a]]

def reduce_maps(x,y):    
    left = x[-1][-1]
    right = y[0][0]
    if left == right:
        return x + [' '] + y
    return x + y

def solve(fIn, fOut):   
    for index, line in enumerate(fIn.readlines()):
        result = "".join(reduce(reduce_maps, map(map_char, line.rstrip('\n'))))
        print 'Case #%i: %s' % (index + 1, result)
        fOut.write('Case #%i: %s\n' % (index + 1, result))

if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg, '%s.out' % arg)
