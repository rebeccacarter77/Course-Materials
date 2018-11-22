import random

name = input('Please enter your name: ')
print('Hello', name)
choice = input('Would you like a weak, medium or strong password? ')

choice = choice.lower()

if choice == 'weak':
    password = name + (str(random.randrange(100)))
    print('Your new password is',password)

elif choice == 'medium':
    list1 = ['Heavy', 'Chunky', 'Smelly', 'Evil', 'Awkward', 'Cute', 'Tiny', 'Purple']
    list2 = ['Mongoose', 'Ballsack', 'Rectangle', 'Poopface', 'Adjective', 'Noun','Typewriter']
    password = (random.choice(list1)) + (random.choice(list2)) + (str(random.randrange(100)))
    print('Your new password is', password)

elif choice == 'strong':
    first = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    second = random.choice('abcdefghijklmnopqrstuvwxyz')
    third = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    fourth = random.choice('abcdefghijklmnopqrstuvwxyz')
    fifth = random.choice('!@#$%^&*()')
    sixth = str(random.randrange(10))
    seventh = str(random.randrange(10))
    eighth = str(random.randrange(10))
    password = first + second + third + fourth + fifth + sixth + seventh + eighth
    print('Your new password is', password)

else:
    print('Invalid selection')
    quit()
