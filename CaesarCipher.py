#!/usr/bin/env python
from __future__ import print_function

def CC(s, keyShift):
     alphabet = 'abcdefghijklmnopqrstuvwxyz'
     s = s.lower()
     
     print('Encrypted text:', end=' ')
     for i in s:
         if i.isalpha():
            encryptedCharacter = alphabet.index(i) + keyShift
            if encryptedCharacter > 25:
                 encryptedCharacter = alphabet.index(i) - keyShift
            print(alphabet[encryptedCharacter], end='')
         else:
            print(i, end='')
     print()
     
CC(input('Enter a string: '), int(input('Enter key shift: ')))  
try:
     input('Press Enter to continue...')
except SyntaxError:
     pass
