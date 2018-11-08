a=[1,1,2,3,5,8,13,21,34,55,89]
lessthan=[]
num=input('Enter a number')
num=int(num)
for i in a:
    if i<num:
        lessthan.append(i)
    else:
        continue

print(lessthan)
