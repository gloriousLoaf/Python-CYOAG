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
      ' Midgard, \nland of the dreaded Jörmungandr serpeant.')
print(40 * '-')
print('The governor of Midgard, Firthquaddle of Falldale, was ordered by King'
      ' Trevius of Midgard,\nto exterminate the wicked Jörmungandr.'
      ' Something about cheating Ragnarok and living forever? \nAnyway,'
      ' Firthquaddle in his great wisdom decided to delegate the task of'
      ' choosing a hero \nfor this dangerous journey. With most of his army'
      ' legion away pillaging and looting, \nthe appointment has fallen to'
      ' the local comptroller, Dewey.')
print(40 * '-')
print('Greatings, I am Dewey, noble comptroller of this fair land.')
name = input('What is your name, adventurer? : ')
print(f'Your name is {name}? Well, you must be from a different realm.')

# Using input assumes values are str, so convert age to int. For now, program
# crashes if str values are entered. In the future, it would make sense to
# allow any input at first, and validate responses with a function

age = int(input(f'And what is your age, {name}? : '))
print(40 * '-')
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
start = input('Shall we depart? (y/n) : ').lower()
print(40 * '-')
if start == 'y' or start == 'yes':
    print(
        f'Glorious, another victim for the snake! \nI mean, victory awaits you, '
        f'{name}! Or whatever people say... \nYou are beginning your journey with'
        f' 10 health points.\nHead to the main road and begin your journey!')

    # ACT I: The River or the Swamp
    print(40 * '-')
    print('ACT I: The River or the Swamp')
    print(40 * '-')
    north_east = input('Will you go north or east? (north/east) : ').lower()
    print(40 * '-')
    if north_east == 'east':
        print(
            'You travel east until the road meets the woods. \nWolves descend'
            ' upon you, and you perish. Permadeath, harsh right?')
    elif north_east == 'north':
        print('Excellent, yes let\'s head straight towards the danger.')
        print(40 * '-')
        river = input(
            'After traveling many miles north, you encounter the great'
            ' Green River.\nWill you wait for a ferryman or attempt to cross?'
            ' (wait/cross) : ').lower()
        print(40 * '-')
        if river == 'wait':
            health += 3
            print(f'The ferryman arrives hours later, with rations.\nAfter'
                  f' eating and crossing the river, your health increased to'
                  f' {health}.')
        elif river == 'cross':
            health -= 3
            print(f'You swam across, but rough currents dashed you against the'
                  f' rocks.\nYour health decreased to {health}.')
        else:
            print(
                'I\'m calling this off. You lack basic communication skills.'
                '\nIf you cannot wield a keyboard, you surely cannot wield a sword.')

        # ACT II: The Village or the Market
        print(40 * '-')
        print('ACT II: The Village or the Market')
        print(40 * '-')
        resting_place = input(
            'After a long day of travelling you encounter a crossing path. \nA crude'
            ' sign indicates that going northeast leads to a market,\nwhile'
            ' going west will take you to a small village. \nWhich way'
            ' will you go to rest before continuing? (market/village) : ').lower()
        print(40 * '-')
        if resting_place == 'market':
            health -= 3
            sword = 'small'
            print(
                f'After haggling with merchants, you are offered a mat to sleep on'
                f' \nand a small sword which you can use to fight Jörmungandr. \nThe'
                f' mat is uncomfortable and hurts your back.\nYour health decreased'
                f' to {health}.')
        elif resting_place == 'village':
            health += 3
            sword = 'great'
            print(
                f'The villagers are poor but kind. You are offered a warm bed,'
                f'\nand meet a skilled ironsmith.\nHe gives you a great sword to fight'
                f' the wicked Jörmungandr. \nRested and armed, your health increased'
                f' to {health}.')
        else:
            print(
                'I\'m calling this off. You lack basic communication skills.'
                '\nIf you cannot wield a keyboard, you surely cannot wield a sword.')

        # ACT III: Deus Ex Machina
        print(40 * '-')
        print('ACT III: Deus Ex Machina')
        print(40 * '-')
        visitor = input(
            'It is morning, and time to face the beast.\nAfter returning to the road'
            ' north, you set out to slay Jörmungandr.\nThe sky turns grey and the wind'
            ' bites as you travel further north.\nAs the noon sun barely penetrates'
            ' the clouds, you find yourself before a mystic visitor.\nWill you'
            ' speak with this creature or runaway? (speak/runaway) : ').lower()
        print(40 * '-')
        if visitor == 'runaway':
            charm = False
            health -= 2
            print(f'You scamper past the stranger, squealing and sweating, hoping'
                  f' that they do not give chase.\nYou hear the stranger call'
                  f' out to you, but you dare not look back.\nAfter several minutes of'
                  f' sprinting, you feel safe to stop and get your bearings.\nThe'
                  f' stranger did not follow you, but the affair left you tired.'
                  f'\nYour health suffers from the exhaustion, and is now {health}.')
        elif visitor == 'speak':
            print(
                f'You call out to the vision, "I am {name}, \nvassal of Dewey the noble'
                f' comptroller to the wise Firthquaddle of Falldale,\ngovernor of this'
                f' land.\nUnder royal decree of the mighty Trevius, King of Midgard,'
                f'\nI am on a quest to slay the wicked serpeant Jörmungandr,\nso that my'
                f' liege might seek eternal life and the forstallment of human'
                f' suffering.\nAnd perhaps a luxurious snakeskin mantle and riding'
                f' boots.\nI beckon you, mystic stranger, reveal yourself and your'
                f' motives!"')
            print(40 * '-')
            accept = input(
                f'The stranger approaches, revealing it\'s form.\nStanding tall and'
                f' powerful, you recognize the smug confidence of a god before you.'
                f'\n"Quite an introduction, {name}. Your bravery is noted, though'
                f' very misguided,\nas the serpeant will not be felled so easily.'
                f'\nJörmungandr, born of Angrboda herself, will bring about Ragnarok'
                f'\nwhen it releases it\'s cruel tail, surely as the day becomes'
                f' night.\nI know this for I am Hermod, son of Odin and messenger'
                f' of Valhalla.\nI have been to Hel. It lacks many comforts,'
                f' to be sure.\nWill you accept the help of the gods of Valhalla?"'
                f' (y/n) : ').lower()
            print(40 * '-')
            if accept == 'y':
                charm = True
                health += 5
                print(f'"Wise decision, {name}. Take this charm, forged'
                      f' by the gifted Brokkr.\nIt will protect you from the'
                      f' poison of the wicked serpeant,\nthough you may yet'
                      f' perish by it\'s bite alone.\nAlso, drink this mead'
                      f' to replenish your strength and catch a buzz.\nGo with'
                      f' the gods, {name}! Oh, and bring me a bolt of the'
                      f' snake\'s skin. Brokkr owes me a belt."')
                print(40 * '-')
                print(
                    f'You put on the charm, and it glistens with an inner light.'
                    f'\nYou once felt that inner light too, but now only dread'
                    f' remains.\nYour health increased to {health}.')
            elif accept == 'n':
                charm = False
                health += 2
                print(f'"You refuse the help of Valhalla? I ought to end your'
                      f' journey now, foolish mortal.\nHowever it will be more'
                      f' enjoyable to watch you perish at the fang of Jörmungandr!'
                      f'\nUndeserving as you may be, {name}, I will share with'
                      f' you one gift out of pity.\nHave this apple. It is mealy,'
                      f' and I have reservations in the Mead Hall soon. anyway."')
                print(40 * '-')
                print(f'You nibble at the mealy apple and feel a curious mixture'
                      f' of sorrow,\nglucose and impending doom fill your veins.'
                      f'\nYour health has increased to {health}')
            else:
                print(
                    'I\'m calling this off. You lack basic communication skills.'
                    '\nIf you cannot wield a keyboard, you surely cannot wield a sword.')

        # ACT IV: Jörmungandr
        print(40 * '-')
        print('ACT IV: Jörmungandr')
        print(40 * '-')
        print('Having survived the encounter with the stranger, you resume'
              ' your journey north.\nOn the horizon looms the black clouds'
              ' of the serpeant\'s poisonous breath.\nAt least one assumes'
              ' it to be breath and not some other gaseous snake exhaust.'
              '\nYou will soon encouter the wicked Jörmungandr.')
        print(40 * '-')
        fight = input('You arrive at the half-frozen marsh the serpeant'
                      ' inhabits.\nThe snake is distracted, playing with it\'s'
                      ' latest kill, a mammoth.\nIt constricts and releases in'
                      ' rhythm, while the tortured creature gasps it\'s final'
                      ' breaths.\nWith this not-so-subtle look at your own'
                      ' potential fate, you must now choose.\nCall out to'
                      ' Jömungandr and fight, or runaway in shame?'
                      ' (fight/runaway) : ').lower()
        print(40 * '-')
        if fight == 'fight':
            print(f'You steel yourself, remembering the training you did'
                  f' not receive, and raise your voice.\n"Jömungandr! It'
                  f' is I, {name}, vassal of Dewey the noble comptroller\n'
                  f'to the wise Firthquaddle of Falldale, governor of this'
                  f' land.\nUnder royal decree of the mighty Trevius, King'
                  f' of Midgard,\nI am on a quest to slay thee, wicked'
                  f' serpeant!\nMy liege seeks eternal life, the forstallment'
                  f' of human suffering,\nand luxurious new garments hewn'
                  f' from your very scales.\nReptile is last season, but'
                  f' I am not his majesty\'s couturier.\nAnyway, prepare to'
                  f' perish, Jömungandr!"')
            print(40 * '-')
            print('The serpeant fixes its dead eyes on you, sending a'
                  ' chill to your core.\nWith a swiftness and silence that'
                  ' seems neigh impossible for its size,\nJömungandr'
                  ' lounges at you. You raise you sword and fight!')
            print(40 * '-')
            if charm == True:
                health -= 10
                print('You parry the first blow of the snake, surprising'
                      ' even yourself.\nThe second strike comes before you'
                      ' can raise you sword again,\n and you feel the painful'
                      ' bite of its powerful jaw.\nThe charm of Brokkr'
                      ' glows bright and protects you from the venom.\nYou'
                      ' lose 10 health.')
                print(40 * '-')
                print(f'Your health is now {health}.')
                print(40 * '-')
                if health <= 0:
                    print('Having lost all your health, you perish.')
                    print(40 * '-')
                elif health >= 0 and sword == 'small':
                    print(f'The serpeant moves fast, knowing it has only'
                          f' wounded you.\nThis next strike from the snake'
                          f' is rushed and off target, and you counter.'
                          f'\nYou swing you {sword} sword, dealing 25'
                          f' damage, and the beast recoils.')
                elif health >= 0 and sword == 'great':
                    print(f'The serpeant moves fast, knowing it has only'
                          f' wounded you.\nThis next strike from the snake'
                          f' is rushed and off target, and you counter.'
                          f'\nYou swing you {sword} sword, dealing 50'
                          f' damage, and the beast recoils.')
                print(40 * '-')
                print('Feeling weak and dazed, you decide to go for the kill'
                      ' lest you be struck again.\nDashing toward Jömungandr,'
                      ' you leap towards the snake\'s throat.\nThe swift serpeant'
                      ' is prepared and grabs your torso in its putrid mouth.'
                      ' You are trapped, and the bite deals 10 damage.')
                health -= 10
                print(40 * '-')
                print(f'Your health is now {health}.')
                print(40 * '-')
                if health <= 0:
                    print('Having lost all your health, you perish.')
                    print(40 * '-')
                elif health >= 0 and sword == 'small':
                    health -= 10
                    print(f'Knowing this is you last chance and you are near'
                          f' the snake\'s throat,\nyou plunge your {sword}'
                          f' sword to the hilt, dealing 25 more damage.\nThis'
                          f' however is not enough to stop Jömungandr.\nThe'
                          f' beast crushes down harder, dealing 10 more damage'
                          f' to you.')
                    print(40 * '-')
                    print(f'Your health is now {health}.\nHaving lost all'
                          f' your health, you perish.')
                    print(40 * '-')
                elif health >= 0 and sword == 'great':
                    print(f'Knowing this is you last chance and you are near'
                          f' the snake\'s throat,\nyou plunge your {sword}'
                          f' sword to the hilt, dealing 50 more damage.\nThe'
                          f' wicked Jömungandr loosens its grip as its life'
                          f' fades.\nThe beast falls defeated, and you wriggle'
                          f' free of its jaw, victorious!')
                    print(40 * '-')
                    # insert ascii art
            else:
                health -= 20
                print(f'You parry the first blow of the snake, surprising'
                      ' even yourself.\nThe second strike comes before you'
                      ' can raise you sword again,\n and you feel the painful'
                      ' bite of it\'s powerful jaw.\nThe venom burns your'
                      ' veins, and you lose 20 health.')
                print(40 * '-')
                print(f'Your health is now {health}.')
                print(40 * '-')
                if health <= 0:
                    print('Having lost all you health, you perish.')
                    print(40 * '-')
                elif health >= 0 and sword == 'small':
                    print(f'The serpeant moves fast, knowing it has only'
                          f' wounded you.\nThis next strike from the snake'
                          f' is rushed and off target, and you counter.'
                          f'\nYou swing your {sword} sword, dealing 25'
                          f' damage, and the beast recoils.')
                elif health >= 0 and sword == 'great':
                    print(f'The serpeant moves fast, knowing it has only'
                          f' wounded you.\nThis next strike from the snake'
                          f' is rushed and off target, and you counter.'
                          f'\nYou swing your {sword} sword, dealing 50'
                          f' damage, and the beast recoils.')
                # HERE
        elif fight == 'runaway':
            print('You decide that you will not suffer the fate of that'
                  ' furry beast.\nGathering yourself, you run with all the'
                  ' speed you can muster.\nUnbeknownst to you, Jömungandr'
                  ' was well aware of you presence and slithers behind you.'
                  '\nIn one swift strike, the serpeant snatches you from the'
                  ' earth in it\'s putrid jaw.\nYou life fades, and you'
                  ' perish a failure.')
        else:
            print(
                'I\'m calling this off. You lack basic communication skills.'
                ' If you cannot wield a keyboard, you surely cannot wield a sword.')
        # else:
        #     print(
        #         'I\'m calling this off. You lack basic communication skills.'
        #         ' If you cannot wield a keyboard, you surely cannot wield a sword.')
    else:
        print(
            'I\'m calling this off. You lack basic communication skills.'
            '\nIf you cannot wield a keyboard, you surely cannot wield a sword.')
else:
    print(f'I did not think you were ready either. Farewell, {name}.')
