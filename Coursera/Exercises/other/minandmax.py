big=None
smol=None
tot=0
while True:
    sval=input("Enter a number or 'done' to finish: ")
    if sval=='done':
        break
    else:
        try:
            fval=float(sval)
        except:
            print('invalid input')
            continue
        if big is None:
            big=fval
            smol=fval
            tot=tot+fval
        elif fval>big:
            big=fval
            tot=tot+fval
        elif fval<smol:
            smol=fval
            tot=tot+fval
        else:
            continue

print('Total:',tot)
print('Largest number:',big)
print('Smallest number:',smol)
