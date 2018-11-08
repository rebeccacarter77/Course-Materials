fh=input('Enter file name:')

bloop=open(fh)
count=0
for line in bloop:
    line=line.rstrip()
    words=line.split()
    if len(words) <1:
        continue
    if words[0] != 'From':
        continue
    else:
        print(words[1])
        count=count+1


print('There were',count,'lines in the file with From as the first word')
