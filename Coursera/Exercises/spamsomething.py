name=input('Enter file name:')
if name==('na na boo boo'):
    print("NA NA BOO BOO TO YOU- You have been punk'd")
    quit()
else:
    fh=open(name)

tot=0.0
count=0.0

for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        strt=line.index(' ')
        num=line[strt: ]
        num=float(num)
        tot=tot+num
        count=count+1



print(tot/count)
