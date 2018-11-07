file=input('Enter a file name:')

try:
    fh=open(file)

except:
    print('File name invalid')
    quit()

counts=dict()

for line in fh:
    line=line.rstrip()
    words=line.split()
    if len(words) <1:
        continue
    if words[0] != 'From':
        continue
    else:
        timestamp=words[5]
        hour=timestamp.split(':')
        hour=hour[0]
        counts[hour]=counts.get(hour,0)+1

final=list()
for key, val in counts.items():
    final.append((key, val))

final.sort()

for x, y in final:
    print(x, y)
