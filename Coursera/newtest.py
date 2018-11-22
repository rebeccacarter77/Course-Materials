import random

list1 = ['Heavy', 'Chunky', 'Smelly', 'Evil', 'Awkward', 'Cute', 'Tiny', 'Purple']
list2 = ['Mongoose', 'Ballsack', 'Rectangle', 'Poopface', 'Adjective', 'Noun','Typewriter']
one = random.choice(list1)
two = random.choice(list2)
three = str(random.randrange(100))
password = one + two + three
print = ('Your new password is', password)
