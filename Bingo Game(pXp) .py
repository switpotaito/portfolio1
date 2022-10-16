# PxP Bingo Game

bingolist = []
p=int(input())

for i in range(p):
	bingolist.append(list(map(int, input().split())))
blanklist=[]

bingo=False

while bingo==False:
	n=int(input())
	if bingolist.count(n)>=1:
		continue
	elif blanklist.count(n)>0:
		continue
	else:
		blanklist.append(n)
		
	for i in range(0,p,1):
		for j in range(0,p,1):
			if n==bingolist[i][j]:
				bingolist[i][j]=0
				
	RowFlag=0
	ColFlag=0
	RCrossFlag=0
	LCrossFlag=0
	
	for i in range(0,p,1):
		RowFlag=0
		ColFlag=0
		for j in range(0,p,1):
			if bingolist[i][j]==0:
				RowFlag=RowFlag+1
			if bingolist[j][i]==0:
					ColFlag=ColFlag+1
		if RowFlag==p or ColFlag==p:
			print("Bingo")
			bingo=True
			break
		
		if bingolist[i][i]==0:
			LCrossFlag=LCrossFlag+1
		if bingolist[i][(p-1)-i]==0:
			RCrossFlag=RCrossFlag+1
	if RCrossFlag==p or LCrossFlag==p:
		print("Bingo")
		bingo=True
		break
