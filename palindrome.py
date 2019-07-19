num = raw_input()
rev_num = reversed(num)
if list(num) == list(rev_num):
    print("yes")
else:
    print("No")
