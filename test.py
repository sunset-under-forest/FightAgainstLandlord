l = [3, 3, 3,4, 4, 4, 1,1 ,2, 2]
l.sort()
combo = [0]*16
for i in l:
    combo[i] +=1
pos = 0
for i in range(16):
    if combo[i]>=3:
        pos = i
        break

length = 0
pairs = 0
while combo[pos+length] >= 3:
    length+=1
print(combo,length)
