# A Python 'Choose Your Own Adventure' text game, by David Metcalf
# www.metcalf.dev
# This is my first project in Python, based on a tutorial by 'Tech with Tim'
# https://www.youtube.com/watch?v=7R-CfL21zIY


# INTRO: Welcome to Midgard. Riffing on some old Norse stuff that I actually
# don't know much about. Just pulling some context from Wikipedia. Though I
# suddenly understand Midgar and the snake in FF7...
print(20 * '-')
print('Welcome to Py-nal Fantasy!')
print(20 * '-')
print('Your adventure and many more bad puns begins in the slithering world of'
      ' Midgard, \nland of the dreaded Jörmgandr serpeant.')
print(20 * '-')
print('The governor of Midgard,Trevius of Falldale, was ordered by King'
      ' Firthquaddle of Midgard, \nto exterminate the wicked Jörmgandr.'
      ' Something about cheating Ragnarok and living forever? \nAnyway, Trevius'
      ' in his great wisdom decided to delegate the task of choosing a hero \nfor'
      ' this dangerous journey. With most of his army legion away pillaging and'
      ' looting, \nthe appointment has fallen to the local comptroller, Dewey.')
print(20 * '-')
print('Greatings, I am Dewey, noble comptroller of this fair land.')
name = input('What is your name, adventurer? ')
print(f'Your name is {name}? Well, you must be from a different realm. ')

# Using input assumes values are str, so convert age to int. For now, program
# crashes if str values are entered. In the future, it would make sense to
# allow any input at first, and validate responses with a function

age = int(input(f'And what is your age, {name}? '))

if age < 15:
    print(f'Only {age} years old? This will be arduous, youngster!')
elif age >= 15 and age < 50:
    print(f'Ah, {age}, a fine time in life to fritter away playing games.')
else:
    print(
        f'Hmph, I hope you\'ve had your vitamins, {name}, this will be tough!')

print(f'Alright {name} who claims to be {age} years old. Your journey awaits!')
start = input('Shall we depart? Y / N ').lower()

if start == 'n' or 'no':
    print(f'I did not think you were ready either, {name}. Farewell.')
else:
    print(
        f'Glorious, another victim for the snake! \nI mean, victory awaits you, '
        f'{name}! Or whatever people say...')


# ACT I: The river or the swamp.
# north_east = input('Will you go North or East? (north/east)?')
# if north_east == 'east':
#     print('You travel east until the road meets the marsh. \nWolves descend upon you,'
#           f' and you perish.')
# else:
