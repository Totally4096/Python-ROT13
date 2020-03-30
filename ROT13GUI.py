from tkinter import *
from tkinter import messagebox

def ROT13():
    alphabet =  'abcdefghijklmnopqrstuvwxyz'

    nStr = str(n.get()).lower()
    keyShift = 13
    encryptedString = []
    for i in nStr:
        if i.isalpha():
            shiftLetter = alphabet.index(i) + keyShift
            if(shiftLetter > 25):
                shiftLetter = alphabet.index(i) - keyShift
            encryptedString.append(alphabet[shiftLetter])
        else:
            continue
    messagebox.showinfo("Encrypted text", ''.join(encryptedString))

top = Tk()
top.geometry("150x150")
top.resizable(FALSE, FALSE)

nLabel = Label(top, text="Input a string")
nLabel.pack()
n = Entry(top, bd=5)
n.pack()

Encrypt = Button(top, text="Encrypt", command=ROT13)
Quit = Button(top, text="Quit", command=top.destroy)

Quit.place(x=0, y=125)
Encrypt.place(x=100, y=125)

top.mainloop()
