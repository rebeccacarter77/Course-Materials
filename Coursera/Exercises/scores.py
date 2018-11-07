score=input('Enter score')
try:
    score=float(score)
except:
    print('Bad score')
    quit()

if score>1.0:
    print('Bad score')
    quit()
elif score>=0.9:
    print('A')
elif score>=0.8:
    print('B')
elif score>=0.7:
    print('C')
elif score>=0.6:
    print('D')
elif score<0.6:
    if score<=0.0:
        print('F')
    else:
        print('Bad score')
else:
    print('Bad score')
