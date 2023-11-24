a=[]
with open('example_100kb.csv') as f:
    for line in f:
        a.append(line)
print(a)