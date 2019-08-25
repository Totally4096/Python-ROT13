from tkinter import *
from tkinter import messagebox

def ROT13():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
				'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    nStr = str(n.get())
    keyShift = 13
    encryptedString = []
    for i in range(len(nStr)):
        shiftLetter = alphabet.index(nStr[i]) + keyShift
        if(shiftLetter > 25):
            shiftLetter = alphabet.index(nStr[i]) - keyShift
        encryptedString.append(alphabet[shiftLetter])
    messagebox.showinfo("Encrypted text", ''.join(encryptedString))

top = Tk()
top.geometry("200x200")
top.resizable(FALSE, FALSE)

nLabel = Label(top, text="Input a string")
nLabel.pack()
n = Entry(top, bd=5)
n.pack()

Encrypt = Button(top, text="Encrypt", command=ROT13)
Quit = Button(top, text="Quit", command=top.destroy)

Quit.place(x=0, y=175)
Encrypt.place(x=150, y=175)
