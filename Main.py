max=0
min=101
sum=0

while True:
	n=int(input())
	if n>=100:
		print(sum)
		break
	else:
		if n>max:
			max=n
		if n<min:
			min=n
		sum=max+min
