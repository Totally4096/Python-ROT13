#!/usr/bin/env python
from __future__ import print_function

def ROT13(s):
     alphabet = 'abcdefghijklmnopqrstuvwxyz'
     s = s.lower().strip()
     
     keyShift = 13
     print('Encrypted text:', end=' ')
     for i in s:
         if i.isalpha():
            encryptedCharacter = alphabet.index(i) + keyShift
            if encryptedCharacter > 25:
                 encryptedCharacter = alphabet.index(i) - keyShift
            print(alphabet[encryptedCharacter], end='')
         else:
            continue
     print()
     
ROT13(input('Enter a string: '))  
try:
     input('Press Enter to continue...')
except SyntaxError:
     pass
