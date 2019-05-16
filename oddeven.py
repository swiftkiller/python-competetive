o=[]
e=[]
n=int(input("Enter no."))
for i in range(n):
	t=int(input("enter no."))
	if(type(t)==type(5)):
		if(t%2 == 0):
			e.append(t)
		else:
			o.append(t)
	else:
		print("Error")
print(len(o))
print(len(e))
