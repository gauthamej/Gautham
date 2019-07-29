a=input()
b=a.split()
for i in range(int(b[0])+1,int(b[1])+1):
  for j in range(2,i):
    if(i%j==0):
      break
  else:
    print(i,end=" ")
