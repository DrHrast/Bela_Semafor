import random

karte = ['7 Herc', '8 Herc', '9 Herc', '10 Herc', 
        'J Herc', 'Q Herc', 'K Herc', 'A Herc',
        '7 Karo', '8 Karo', '9 Karo', '10 Karo',
        'J Karo', 'Q Karo', 'K Karo', 'A Karo',
        '7 Pik', '8 Pik', '9 Pik', '10 Pik',
        'J Pik', 'Q Pik', 'K Pik', 'A Pik',
        '7 Tref', '8 Tref', '9 Tref', '10 Tref',
        'J Tref', 'Q Tref', 'K Tref', 'A Tref']
odigrane = list()
brojac = 0
karta_igraca1 = ''
karta_igraca2 = ''
karta_igraca3 = ''
karta_igraca4 = ''
af1 = 0
af2 = 0
af3 = 0
af4 = 0

while True:
    if karta_igraca1 == 'K Herc' or karta_igraca1 == 'K Karo' or karta_igraca1 == 'K Pik' or karta_igraca1 == 'K Tref':
        pass
    else:
        igrac1 = random.randint(0, len(karte) - 1)
        print('Igrač 1 : ' + karte[igrac1])
        karta_igraca1 = karte[igrac1]
        if karta_igraca1 == 'K Herc' or karta_igraca1 == 'K Karo' or karta_igraca1 == 'K Pik' or karta_igraca1 == 'K Tref':
            brojac += 1
            af1 = 1
        odigrane = karte.pop(igrac1)

    if brojac == 2:
        break

    if karta_igraca2 == 'K Herc' or karta_igraca2 == 'K Karo' or karta_igraca2 == 'K Pik' or karta_igraca2 == 'K Tref':
        pass
    else:
        igrac2 = random.randint(0, len(karte) - 1)
        print('Igrač 2 : ' + karte[igrac2])
        karta_igraca2 = karte[igrac2]
        if karta_igraca2 == 'K Herc' or karta_igraca2 == 'K Karo' or karta_igraca2 == 'K Pik' or karta_igraca2 == 'K Tref':
            brojac += 1
            af2 = 1
        odigrane = karte.pop(igrac2)

    if brojac == 2:
        break

    if karta_igraca3 == 'K Herc' or karta_igraca3 == 'K Karo' or karta_igraca3 == 'K Pik' or karta_igraca3 == 'K Tref':
        pass
    else:
        igrac3 = random.randint(0, len(karte) - 1)
        print('Igrač 3 : ' + karte[igrac3])
        karta_igraca3 = karte[igrac3]
        if karta_igraca3 == 'K Herc' or karta_igraca3 == 'K Karo' or karta_igraca3 == 'K Pik' or karta_igraca3 == 'K Tref':
            brojac += 1
            af3 = 1
        odigrane = karte.pop(igrac3)

    if brojac == 2:
        break

    if karta_igraca4 == 'K Herc' or karta_igraca4 == 'K Karo' or karta_igraca4 == 'K Pik' or karta_igraca4 == 'K Tref':
        pass
    else:
        igrac4 = random.randint(0, len(karte) - 1)
        print('Igrač 4 : ' + karte[igrac4])
        karta_igraca4 = karte[igrac4]
        if karta_igraca4 == 'K Herc' or karta_igraca4 == 'K Karo' or karta_igraca4 == 'K Pik' or karta_igraca4 == 'K Tref':
            brojac += 1
            af4 = 1
        odigrane = karte.pop(igrac4)
    
    print()

    if brojac == 2:
        break

print()
print('*' * 16)
print(f'Igrač 1: {karta_igraca1}\nIgrač 2: {karta_igraca2}\nIgrač 3: {karta_igraca3}\nIgrač 4: {karta_igraca4}')
print('U timu 1 su:', end = ' ')
if af1 == 1:
    print('Igrač 1', end = ' ')
if af2 == 1:
    print('Igrač 2', end = ' ')
if af3 == 1:
    print('Igrač 3', end = ' ')
if af4 == 1:
    print('Igrač 4', end = '')
print('\n' + '*' * 16)