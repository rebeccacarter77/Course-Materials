def computepay(hrs, rate):
    if hrs>40:
        print(((hrs-40)*1.5+40)*rate)
    else:
        return(hrs*rate)

hrs=input('Hours worked')
rate=input('Rate of pay')

try:
    hrs=float(hrs)
    rate=float(rate)
except:
    print('Error, please enter numeric input')
    quit()

computepay(hrs,rate)
