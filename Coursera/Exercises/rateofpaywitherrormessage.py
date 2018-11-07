hrs=input('Enter hours')
rph=input('Enter rate of pay')
try:
    hrs=float(hrs)
    rph=float(rph)
except:
    print('Error, please enter numeric input')
    quit()

if hrs>40:
    print(((hrs-40)*1.5+40)*rph)
else:
    print(hrs*rph)
