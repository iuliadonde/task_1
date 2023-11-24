a=[]
with open('out.csv') as f:
    for line in f.readlines():
        s=line.strip().split(',')
        a.append(s[2])

k=[]
for i in a:
    k.append(i.split('@')[-1])

d={}
c=0
for j in k:
    if j not in d:
        d[j] = 1
    else:
        d[j]+=1
print(d.items())