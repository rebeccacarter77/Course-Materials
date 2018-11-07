fh=input('Enter file name:')

bloop=open(fh)
counts=dict()

for line in bloop:
    line=line.rstrip()
    words=line.split()
    if len(words) <1:
        continue
    if words[0] != 'From':
        continue
    else:
        new=words[1]
        counts[new]=counts.get(new,0)+1

mostcount=None
mostemail=None
for key,value in counts.items():
    if mostcount is None or value>mostcount:
        mostcount=value
        mostemail=key

print(mostemail, mostcount)
