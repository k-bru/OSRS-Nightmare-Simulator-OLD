import random
import time

def displayIntro():
    print('Welcome to the Nightmare of Ashihama simulator by Dembo')
    time.sleep(1)

def killTarget():
    print('Please enter how many kills you would like to do:')

def checkLoot():
    pet = 0
    mace = 0
    harm = 0
    vol = 0
    eldr = 0
    staff = 0
    helm = 0
    haub = 0
    skirt = 0
    kills = 0
    myName = 0
    myPets = 0
    gear = 0
    minutesTaken = 0
    killAmount = int(input(">>> "))
    teamsize = 0
    while teamsize == 0:
        print("Please enter your team size: (1-5)")
        teamsize = int(input(">>> "))
        while teamsize >= 6:
            print("Please enter a number between 1 and 5.")
            inputValue = input(">>> ")
            try:
                teamsize = int(inputValue)
            except ValueError:
                print("{input} is not a valid number. Please enter a number between 1 and 5.".format(input=inputValue))
    

    print('You begin to kill the Nightmare...')
    time.sleep(2)

    while kills < killAmount:
        kills = kills +1
        
        if teamsize == 1:
            minutesTaken = minutesTaken + 19
        if teamsize == 2:
            minutesTaken = minutesTaken + 11
        if teamsize == 3:
            minutesTaken = minutesTaken + 8
        if teamsize == 4:
            minutesTaken = minutesTaken + 6
        if teamsize == 5:
            minutesTaken = minutesTaken + 5
            
        if random.randint(1,120) == 120:
            print()
            gear = gear + 1
            staffLoot = random.randint(1,150)
            if staffLoot <= 15:
                mace = mace + 1
                print(f"Your team has received an Inquisitor's Mace at {kills} killcount")
                if random.randint(1,teamsize) == teamsize:
                    print("It was in your name!")
                    myName = myName + 1
            if staffLoot >= 16 and staffLoot <= 40:
                helm = helm + 1
                print(f"Your team has received an Inquisitor's Great Helm at {kills} killcount.")
                if random.randint(1,teamsize) == teamsize:
                    print("It was in your name!")
                    myName = myName + 1
            if staffLoot >= 41 and staffLoot <= 65:
                haub = haub + 1
                print(f"Your team has received an Inquisitor's Hauberk at {kills} killcount.")
                if random.randint(1,teamsize) == teamsize:
                    print("It was in your name!")
                    myName = myName + 1
            if staffLoot >= 66 and staffLoot <= 90:
                skirt = skirt + 1
                print(f"Your team has received an Inquisitor's Plateskirt at {kills} killcount.")
                if random.randint(1,teamsize) == teamsize:
                    print("It was in your name!")
                    myName = myName + 1
            if staffLoot >= 91 and staffLoot <= 150:
                staff = staff + 1
                print(f"Your team has received a Nightmare Staff at {kills} killcount.")
                if random.randint(1,teamsize) == teamsize:
                    print("It was in your name!")
                    myName = myName + 1
                    
        if random.randint(1,600) == 600:
            print()
            gear = gear + 1
            orbLoot = random.randint(1,3)
            if orbLoot == 1:
                harm = harm + 1
                print(f"Your team has received a Harmonised Orb at {kills} killcount.")
                if random.randint(1,teamsize) == teamsize:
                    print("It was in your name!")
                    myName = myName + 1
            if orbLoot == 2:
                eldr = eldr + 1
                print(f"Your team has received an Eldritch Orb at {kills} killcount.")
                if random.randint(1,teamsize) == teamsize:
                    print("It was in your name!")
                    myName = myName + 1
            if orbLoot == 3:
                vol = vol + 1
                print(f"Your team has received a Volatile Orb at {kills} killcount.")
                if random.randint(1,teamsize) == teamsize:
                    print("It was in your name!")
                    myName = myName + 1
                    
        if teamsize == 1:
            if random.randint(1,800) == 800:
                pet = pet + 1
                if random.randint(1,teamsize) == teamsize:
                    myPets = myPets + 1
                    if myPets == 1:
                        print()
                        print("You have a funny feeling like you're being followed.")
                    if myPets >= 2:
                        print()
                        print("You have a funny feeling like you would have been followed.")
                print(f"Your team has received a Little Nightmare at {kills} killcount!")
        if teamsize == 2:
            if random.randint(1,1600) == 1600:
                pet = pet + 1
                if random.randint(1,teamsize) == teamsize:
                    myPets = myPets + 1
                    if myPets == 1:
                        print()
                        print("You have a funny feeling like you're being followed.")
                    if myPets >= 2:
                        print()
                        print("You have a funny feeling like you would have been followed.")
                print(f"Your team has received a Little Nightmare at {kills} killcount!")
        if teamsize == 3:
            if random.randint(1,2400) == 2400:
                pet = pet + 1
                if random.randint(1,teamsize) == teamsize:
                    myPets = myPets + 1
                    if myPets == 1:
                        print()
                        print("You have a funny feeling like you're being followed.")
                    if myPets >= 2:
                        print()
                        print("You have a funny feeling like you would have been followed.")
                print(f"Your team has received a Little Nightmare at {kills} killcount!")         
        if teamsize == 4:
            if random.randint(1,3200) == 3200: 
                pet = pet + 1
                if random.randint(1,teamsize) == teamsize:
                    myPets = myPets + 1
                    if myPets == 1:
                        print()
                        print("You have a funny feeling like you're being followed.")
                    if myPets >= 2:
                        print()
                        print("You have a funny feeling like you would have been followed.")
                print(f"Your team has received a Little Nightmare at {kills} killcount!")    
        if teamsize >= 5:
            if random.randint(1,4000) == 4000:
                pet = pet + 1
                if random.randint(1,teamsize) == teamsize:
                    myPets = myPets + 1
                    if myPets == 1:
                        print()
                        print("You have a funny feeling like you're being followed.")
                    if myPets >= 2:
                        print()
                        print("You have a funny feeling like you would have been followed.")
                print(f"Your team has received a Little Nightmare at {kills} killcount!")

    print()
    print()
    print(f'Total loot from {killAmount} Nightmare:')

    if staff > 0:
        print(f"{staff} Nightmare Staff")
    if mace > 0:
        print(f"{mace} Inquisitor's Mace")
    if helm > 0:
        print(f"{helm} Inquisitor's Great Helm")
    if haub > 0:
        print(f"{haub} Inquisitor's Hauberk")
    if skirt > 0:
        print(f"{skirt} Inquisitor's Plateskirt")
    if eldr > 0:
        print(f"{eldr} Eldritch Orb")
    if vol > 0:
        print(f"{vol} Volatile Orb")
    if harm > 0:
        print(f"{harm} Harmonised Orb")
    if pet > 0:
        print(f'{pet} Little Nightmare, {myPets} in your name')
    if gear > 0:
        print(f"{gear} pieces of gear dropped with {myName} in your name.")
        
    
    
    print(f"On average, for {kills} kills, your team would have received {int(kills / 100)} items, with {int(kills / 100 / teamsize)} in your name.")
    
    if gear < kills / 100:
        print("Oof, better luck next time...")
    if gear >= kills / 100:
        print("Not bad!")
    print()
    print(f"Average time taken: {minutesTaken / 60} hours")
    print()
    
    
    
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':            
    displayIntro()
    killTarget()
    checkLoot()
   

    
        
        
    
