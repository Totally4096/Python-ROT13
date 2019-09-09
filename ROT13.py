from __future__ import print_function

def ROT13(s):
     alphabet = 'abcdefghijklmnopqrstuvwxyz'
     
     keyShift = 13
     for i in range(len(s)):
         encryptedCharacter = alphabet.index(s[i]) + keyShift
         if encryptedCharacter > 25:
             encryptedCharacter = alphabet.index(s[i]) - keyShift
         print(alphabet[encryptedCharacter], end='')
     print()
     
ROT13(input('Enter a string: '))  
try:
     input('Press Enter to continue...')
except SyntaxError:
     pass
