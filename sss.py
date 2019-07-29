a=input()
b=a.split()
c=[]
c=[int(b[i]) for i in range(0,3)]
s=(c[0] * (2 *c[1] + ((c[0] - 1) * c[2]))) / 2

print(round(s))
