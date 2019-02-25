#ROT13 test

def ROT13(n):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	if(len(n) > 1):
		x = list(n)
		b = 13
		d = x.index(max(x))
		for i in range(d+1):
			c = alphabet.index(x[i]) + b
			if(c>25):
				c = alphabet.index(x[i]) - b
			g = alphabet[c]
			print(g, end='')
		print()

	else:
		x = alphabet.index(n)
		b = 13

		c = x+b
		if(c > 25):
			c = x-b

		g = alphabet[c]
		print(g)

ROT13(str(input()))

