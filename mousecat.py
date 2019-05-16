q=int(input())
for i in range(q):
	x=int(input())
	y=int(input())
	z=int(input())
	a=abs(x-z)
	b=abs(y-z)
	if(b>a):
		print("Cat A")
	elif(b<a):
		print("Cat B")
	else:
		print("Mouse C")