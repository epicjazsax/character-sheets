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


mods = {
    "str": (strength//2) - 5,
    "dex": (dexterity//2) - 5,
    "con": (constitution//2) - 5,
    "int": (intelligence//2) - 5,
    "wis": (wisdom//2) - 5,
    "cha": (charisma//2) - 5,
}

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

    mod = mods[statcheck]
    print(f"modifier is: {mod}")
    print(f"stat check is: {die0 + mod}")

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

    mod = mods[advcheck]
    print(f"modifier is: {mod}")
    print(f"advantage check is: {advdie + mod}")


def rolldis():
    discheck = input("Rolling check with disadvantage - str, dex, con, int, wis, or cha: ")
    die1, die2 = roll(20), roll(20)
    if die1 < die2:
        disdie = die1
    else:
        disdie = die2
    print("rolls are:", die1, die2)

    mod = mods[discheck]
    print(f"modifier is: {mod}")
    print(f"disadvantage check is: {disdie + mod}")

