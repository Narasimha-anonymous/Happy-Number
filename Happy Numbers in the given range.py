p,q=map(int,input("Enter the range: ").split())
a=0
if p>q:
	p,q=q,p
for n in range(p,q+1):
		t=n
		n=str(n)
		while int(n)!=1 and int(n)!=4:
			for i in n:
				a+=int(i)**2
			n=str(a)
			a=0
		if int(n)==1:
			print(t)
