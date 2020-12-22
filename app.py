# A Python 'Choose Your Own Adventure' text game, by David Metcalf
# www.metcalf.dev
# This is my first project in Python, based on a tutorial by 'Tech with Tim'
# https://www.youtube.com/watch?v=7R-CfL21zIY


# INTRO: Welcome to Midgard. Riffing on some old Norse stuff that I actually
# don't know much about. Just pulling some context from Wikipedia. Though I
# suddenly understand Midgar and the snake in FF7...
print(40 * '-')
print('Welcome to Py-nal Fantasy!')
print(40 * '-')
print('Your adventure and many more bad puns begins in the slithering world of'
      ' Midgard, \nland of the dreaded Jörmgandr serpeant.')
print(40 * '-')
print('The governor of Midgard,Trevius of Falldale, was ordered by King'
      ' Firthquaddle of Midgard, \nto exterminate the wicked Jörmgandr.'
      ' Something about cheating Ragnarok and living forever? \nAnyway, Trevius'
      ' in his great wisdom decided to delegate the task of choosing a hero \nfor'
      ' this dangerous journey. With most of his army legion away pillaging and'
      ' looting, \nthe appointment has fallen to the local comptroller, Dewey.')
print(40 * '-')
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

# Shall we begin?
health = 10
start = input('Shall we depart? Y / N ').lower()
if start == 'y' or start == 'yes':
    print(
        f'Glorious, another victim for the snake! \nI mean, victory awaits you, '
        f'{name}! Or whatever people say... \nYou are beginning your journey with'
        f' 10 health points.')

    # ACT I: The River or the Swamp
    print(40 * '-')
    print('ACT I: The River or the Swamp')
    print(20 * '-')
    north_east = input('Will you go north or east? (north/east) ').lower()
    if north_east == 'east':
        print(
            'You travel east until the road meets the marsh. \nWolves descend'
            ' upon you, and you perish. Permadeath, harsh right?')
    elif north_east == 'north':
        print('Excellent, yes let\'s head straight towards the danger.')
        print(40 * '-')
        river = input(
            'After traveling many miles north, you encounter the great'
            ' Green River. \nWill you wait for a ferryman or attempt to cross?'
            ' (wait/cross) ')
        if river == 'wait':
            health += 3
            print(f'The ferryman arrives hours later, with rations. After'
                  f' eating and crossing the river, \nyour health is now {health}.')
        elif river == 'cross':
            health -= 3
            print(f'You swam across, but rough currents dashed you against the'
                  f' rocks. Your health is now {health}.')
        else:
            print(
                'I\'m calling this off. You lack basic communication skills.'
                ' If you cannot wield a keyboard, you surely cannot wield a sword.')

        # ACT II: The Village or the Market
        print(40 * '-')
        print('ACT II: The Village or the Market')
        print(40 * '-')
        resting_place = input(
            'After a long day of travelling you encounter a crossing path. \nA crude'
            ' sign indicates that going northeast leads to a market,\nwhile'
            ' going west will take you to a small village. \nWhich way'
            ' will you go to rest before continuing? (market/village) ')
        if resting_place == 'market':
            health -= 3
            print(
                f'After haggling with merchants, you are offered a mat to sleep on'
                f' \nand a small sword which you can use to fight Jörmgandr. \nThe'
                f' mat is uncomfortable and hurts your back. You health is now {health}.')
        elif resting_place == 'village':
            health += 3
            print(
                f'The villagers are poor but kind. You are offered a warm bed,'
                f'\nand meet a skilled ironsmith. He gives you a great sword to fight'
                f' the wicked Jörmgandr. \nRested and armed, you health is now {health}.')
        else:
            print(
                'I\'m calling this off. You lack basic communication skills.'
                ' If you cannot wield a keyboard, you surely cannot wield a sword.')

        # ACT III: Deus Ex Machina
        print(40 * '-')
        print('ACT III: Deus Ex Machina')
        print(40 * '-')
        power_up = input(
            'It is morning, and time to face the beast. After returning to the road'
            ' north,\nyou set out to slay Jörmgandr. The sky turns grey and the wind'
            ' bites as you travel further north.\nAs noon sun barely penetrates'
            ' the clouds, you find yourself by an unearthly visitor.')

    else:
        print(
            'I\'m calling this off. You lack basic communication skills.'
            ' If you cannot wield a keyboard, you surely cannot wield a sword.')
else:
    print(f'I did not think you were ready either. Farewell, {name}.')
