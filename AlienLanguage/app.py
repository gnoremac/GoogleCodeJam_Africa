import os
import sys

def main(fileIn, fileOut):   
    fIn = open(fileIn, 'r')
    fOut = open(fileOut, 'w')

    solve(fIn, fOut)

    fIn.close()
    fOut.close()

def solve(fIn, fOut):
    meta_data = map(int, fIn.readline().split())
    word_length = meta_data[0]
    dict_length = meta_data[1]
    test_cases = meta_data[2]
    
    alien_dict = []
    for i in range(dict_length):        
        alien_dict.append(fIn.readline().rstrip())
        
    for case in range(test_cases):
        pos = 0
        index = 0
        encrypted_word = fIn.readline().rstrip()
        valid_chars = [[]] * word_length
        print encrypted_word

        while index < len(encrypted_word):

            chars = []
            if encrypted_word[index] == '(':
                index += 1
                while encrypted_word[index] != ')':
                    chars.append(encrypted_word[index])
                    index += 1
                index += 1
            else:
                chars.append(encrypted_word[index])
                index += 1
            
            valid_chars[pos] = chars
                
            pos += 1
        
        print valid_chars
        
        result = 0
        for word in alien_dict:
            count = 0
            for pos, c in enumerate(word):
                for valid_c in valid_chars[pos]:
                    if valid_c == c:
                        count += 1
                        break;
            if count == word_length:
                result += 1
            
        print 'Case #%d: %d' % (case + 1, result)
        fOut.write('Case #%d: %d\n' % (case + 1, result))
               
if __name__ == '__main__':
    arg = sys.argv[1]
    main(arg, '%s.out' % arg)
