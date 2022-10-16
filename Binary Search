#how to find key in the given list

searchList=[]
for i in range(1,101,1):
	searchList.append(i)

key=int(input())

count=0
low=0
high=len(searchList)-1

while high>=low:
	mid=(low+high)//2
	count=count+1
	if key==searchList[mid]:
		print("%d places %dth index on the list." % (key,mid))
		break
	elif key<searchList[mid]:
		high=mid-1
	elif key>searchList[mid]:
		low=mid+1
	
	
print("Trial: %d" % (count))
