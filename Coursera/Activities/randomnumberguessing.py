import random

print('Number guessing game!!!')
count=0
correct=0
wrong=0

while True:
    guess=input('Pick a number between 1 and 10:\n')
    guess=guess.lower()
    if guess=='exit':
        break
    else:
        try:
            guess=int(guess)
        except:
            print('Please enter a valid nummber or type "exit" to end game')

    a=random.randint(1,11)
    if guess>10 or guess<1:
        print('You chose a number too high or low, please try again')
        count=count+1
        wrong=wrong+1
        continue

    elif guess==a:
        print('Congratulations, you guessed right!')
        count=count+1
        correct=correct+1
        continue

    else:
        print('Sorry, your guess was not correct, better luck next time')
        count=count+1
        wrong=wrong+1
        continue

print('You got', correct, 'guesses right and', wrong,'guesses wrong, after a total of', count,'guesses.')
