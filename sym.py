n=input()
alphabets = digits = special = 0

for i in range(len(n)):
    if((n[i] >= 'a' and n[i] <= 'z') or (n[i] >= 'A' and n[i] <= 'Z')): 
        alphabets = alphabets + 1 
    elif(n[i] >= '0' and n[i] <= '9'):
        digits = digits + 1
    else:
        special = special + 1
print(special)
