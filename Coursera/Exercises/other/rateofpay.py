hrs=input('Enter hours')
rph=input('Enter rate of pay')
hrs=float(hrs)
rph=float(rph)
if hrs>40:
    print(((hrs-40)*1.5+40)*rph)
else:
    print(hrs*rph)
