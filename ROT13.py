#ROT13 test

def ROT13(n):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	if(len(n) > 1):
		x = list(n)
		b = 13
		d = len(x)-1
		str1 = "Final result: "
		for i in range(len(x)):
			c = alphabet.index(x[i]) + b
			if(c > 25):
				c = alphabet.index(x[i]) - b

			g = alphabet[c]
			print(str1, g, end='')
			str1 = ''
		print()

	else:
		x = alphabet.index(n)
		b = 13

		c = x+b
		if(c > 25):
			c = x-b

		g = alphabet[c]
		print("Final result: ", g)

ROT13(str(input("Enter a string: ")))
