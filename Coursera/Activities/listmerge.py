import random

a = random.sample(range(100),10)
b = random.sample(range(100), 12)

print('list a:', a)
print('list b:', b)

c=[]
for all in b:
    if all not in a:
        continue
    else:
        if all in c:
            continue
        else:
            c.append(all)

print(c)
