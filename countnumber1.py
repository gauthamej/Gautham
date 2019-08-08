n=input()
count=0

b=len(n)
for i in range(0,b):
    if (n[i]>='0' and n[i]<='9'):
        count=count+1
print(count)
