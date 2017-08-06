prec = 2**25
i = -1
num = 22
denum = 7

show = ""
while i < prec:
	res = num // denum #3
	rem = num % denum #1
	num = rem *10
	i += 1
	show += str(res)
print(show[0] + "." + show[1:])