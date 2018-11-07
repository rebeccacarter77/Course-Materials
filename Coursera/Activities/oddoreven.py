num=input('Please enter any number')
num=float(num)
res=num%4
if res==0:
    print('This number is divisible by four!')
else:
    res=num%2
    if res==0:
        print('This number is even')
    else:
        print('This number is odd')

num=input('Please enter one number')
check=input('Please enter another number')
num=float(num)
check=float(check)
res=num%check
if res==0:
    print(num,'is divisible by',check)
else:
    print(num,'is not divisible by', check)
