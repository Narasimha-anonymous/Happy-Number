n=int(input("Enter a num:"))
a=0
while n!=1 and n!=4:
	while n:
		r=n%10
		a+=r*r
		n//=10
	n=a
	a=0
if n==1:
	print("Happy number")
else:
	print("Unhappy number")