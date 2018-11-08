count=0
tot=0
while True:
    sval=input("Enter a number or 'done' to finish: ")
    if sval=='done':
        break
    else:
        try:
            fval=float(sval)
            count=count+1
            tot=tot+fval
        except:
            print('invalid input')
            continue

print('Total:',tot)
print('Numbers entered:',count)
print('Average:',tot/count)
