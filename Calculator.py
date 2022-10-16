def add(x,y):
	res=x+y
	return res

def sub(x,y):
	res=x-y
	return res

def mul(x,y):
	res=x*y
	return res

def div(x,y):
	res=x/y
	return res

def calc(x,op,y):
	if op=='+':
		res=add(x,y)
	elif op=='-':
		res=sub(x,y)
	elif op=='*':
		res=mul(x,y)
	elif op=='/':
		res=div(x,y)
	
	return res
  
num1 = int(input())
num2 = int(input())
op = input()

print(calc(num1,op,num2))
