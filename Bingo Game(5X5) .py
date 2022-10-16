bingolist=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
blanklist=[]

bingo=False

while bingo==False:
	n=int(input())
	if n<1 or n>25:
		continue
	elif blanklist.count(n)>0:
		continue
	else:
		blanklist.append(n)
		
	for i in range(0,5,1):
		for j in range(0,5,1):
			if n==bingolist[i][j]:
				bingolist[i][j]=0
				
	RowFlag=0
	ColFlag=0
	RCrossFlag=0
	LCrossFlag=0
	
	for i in range(0,5,1):
		RowFlag=0
		ColFlag=0
		for j in range(0,5,1):
			if bingolist[i][j]==0:
				RowFlag=RowFlag+1
			if bingolist[j][i]==0:
					ColFlag=ColFlag+1
		if RowFlag==5 or ColFlag==5:
			print("Bingo")
			bingo=True
			break
		
		if bingolist[i][i]==0:
			LCrossFlag=LCrossFlag+1
		if bingolist[i][4-i]==0:
			RCrossFlag=RCrossFlag+1
	if RCrossFlag==5 or LCrossFlag==5:
		print("Bingo")
		bingo=True
		break
