a=input()
b=a.split()
for i in range(int(b[0])+1,int(b[1])):
    if(i%2==0):
        print (i,end=" ")
