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

check_types = {
    'advantage' : max,
    'disadvantage': min,
    None: lambda a, b : a  # 'function' that given a and b will return a (the first)
}

initmod = dexmod


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
    check()


def rolladv():
    check('advantage')


def rolldis():
    check('disadvantage')


def check(mod_type=None):
    """Roll a check with a possible advantage or disadvantage.
       mod_type should be 'advantage', 'disadvantage' or None
    """

    if mod_type not in ('advantage', 'disadvantage', None):
        print("Error: invalid mod type")
        return

    mod_type_check_messge = f"{mod_type} check" if mod_type else "check"

    stat = input(f"Rolling {mod_type_check_messge} - str, dex, con, int, wis, or cha: ")
    die1, die2 = roll(20), roll(20)
    print("rolls are:", die1, die2)

    f = check_types[mod_type]
    die = f(die1, die2)

    mod = mods[stat]
    print(f"modifier is: {mod}")
    print(f"{mod_type_check_messge} is: {die + mod}")
