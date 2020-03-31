#!/usr/bin/env python
from __future__ import print_function

def CC(s, keyShift=1):
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
            continue
     print()
     
CC(input('Enter a string: '), int(input('Enter key shift: ')))  
try:
     input('Press Enter to continue...')
except SyntaxError:
     pass
