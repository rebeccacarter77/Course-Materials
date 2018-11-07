text=open('romeo.txt')
list=[]
for line in text:
    words=line.split()
    for i in words:
        if i in list:
            continue
        else:
            list.append(i)


list.sort()
print(list)
