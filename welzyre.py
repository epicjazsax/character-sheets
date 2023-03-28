import random

strength = 11
dexterity = 16
constitution = 15
intelligence = 17
wisdom = 9
charisma = 12

strmod = (strength//2) - 5
dexmod = (dexterity//2) - 5
conmod = (constitution//2) - 5
intmod = (intelligence//2) - 5
wismod = (wisdom//2) - 5
chamod = (charisma//2) - 5

initmod = dexmod
#stat and modifier block

def roll(die):
    r1, r2 = 1, die
    die_thing = list(range(r1, r2 + 1))
    random.shuffle(die_thing)
    roll_die = die_thing[0]
    return roll_die

def rollinit():
    initdie = roll(20)
    print("roll is:", initdie)
    print("modifier is:", initmod)
    print("initiative is:", initdie + initmod)

def rollcheck():
    statcheck = input("Rolling stat check - str, dex, con, int, wis, or cha: ")
    die0 = roll(20)
    print("roll is:", die0)
    if statcheck == "str":
        print("modifier is:", strmod)
        print("stat check is:", die0 + strmod)
    elif statcheck == "dex":
        print("modifier is:", dexmod)
        print("stat check is:", die0 + dexmod)
    elif statcheck == "con":
        print("modifier is:", conmod)
        print("stat check is:", die0 + conmod)
    elif statcheck == "int":
        print("modifier is:", intmod)
        print("stat check is:", die0 + intmod)
    elif statcheck == "wis":
        print("modifier is:", wismod)
        print("stat check is:", die0 + wismod)
    elif statcheck == "cha":
        print("modifier is:", chamod)
        print("stat check is:", die0 + chamod)
    else:
        return "invalid input"
    #with "if" statements, always returns 'invalid input'
    #with "elif" statements, always returns 'none'
    #how to make it only print if input is false?

def rolladv():
    advcheck = input("Rolling check with advantage - str, dex, con, int, wis, or cha: ")
    die1, die2 = roll(20), roll(20)
    if die1 > die2:
        advdie = die1
    else:
        advdie = die2
    print("rolls are:", die1, die2)
    if advcheck == "str":
        print("modifier is:", strmod)
        print("advantage check is:", advdie + strmod)
    if advcheck == "dex":
        print("modifier is:", dexmod)
        print("advantage check is:", advdie + dexmod)
    if advcheck == "con":
        print("modifier is:", conmod)
        print("advantage check is:", advdie + conmod)
    if advcheck == "int":
        print("modifier is:", intmod)
        print("advantage check is:", advdie + intmod)
    if advcheck == "wis":
        print("modifier is:", wismod)
        print("advantage check is:", advdie + wismod)
    if advcheck == "cha":
        print("modifier is:", chamod)
        print("advantage check is:", advdie + chamod)
    else:
        return "invalid input"

def rolldis():
    discheck = input("Rolling check with disadvantage - str, dex, con, int, wis, or cha: ")
    die1, die2 = roll(20), roll(20)
    if die1 < die2:
        disdie = die1
    else:
        disdie = die2
    print("rolls are:", die1, die2)
    if discheck == "str":
        print("modifier is:", strmod)
        print("disadvantage check is:", disdie + strmod)
    if discheck == "dex":
        print("modifier is:", dexmod)
        print("disadvantage check is:", disdie + dexmod)
    if discheck == "con":
        print("modifier is:", conmod)
        print("disadvantage check is:", disdie + conmod)
    if discheck == "int":
        print("modifier is:", intmod)
        print("disadvantage check is:", disdie + intmod)
    if discheck == "wis":
        print("modifier is:", wismod)
        print("disadvantage check is:", disdie + wismod)
    if discheck == "cha":
        print("modifier is:", chamod)
        print("disadvantage check is:", disdie + chamod)
    else:
        return "invalid input"
