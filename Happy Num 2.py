n=input('Enter a num:')
a=0
while int(n)!=1 and int(n)!=4:
	for i in n:
		a+=int(i)**2
	n=str(a)
	a=0
if int(n)==1:
	print("Happy")
else:
	print("Unhappy")