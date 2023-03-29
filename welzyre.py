import random

print("type: roll(#), rollinit(), rollcheck(), rollsave(), rolladv(), or rolldis()")
#any way to make this print line automatically update with other added functions?

level = 5

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

pass_perception = 10 + wismod
pass_investigation = 10 + intmod
pass_insight = 10 + wismod
darkvision = 60
walking = 25

initmod = dexmod
profmod = (level + 7)//4
dblprof = profmod * 2
halfprof = profmod // 2

acrobatics_mod = dexmod + profmod
animal_handling_mod = wismod
arcana_mod = intmod
athletics_mod = strmod + profmod
deception_mod = chamod + profmod
history_mod = intmod
insight_mod = wismod
intimidation_mod = chamod
investigation_mod = intmod
medicine_mod = wismod
nature_mod = intmod
perception_mod = wismod
performance_mod = chamod + dblprof
persuasion_mod = chamod
religion_mod = intmod
sleight_mod = dexmod + dblprof
stealth_mod = dexmod + profmod
survival_mod = wismod
tech_mod = intmod + halfprof
#stat and modifier block


#moddict = {strn: strmod, dex: dexmod, con: conmod, intl: intmod, wis: wismod, cha: chamod, init: initmod}


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
    checkdie = roll(20)
    print("roll is:", checkdie)
    if statcheck == "str":
        print("modifier is:", strmod)
        print("stat check is:", checkdie + strmod)
    elif statcheck == "dex":
        print("modifier is:", dexmod)
        print("stat check is:", checkdie + dexmod)
    elif statcheck == "con":
        print("modifier is:", conmod)
        print("stat check is:", checkdie + conmod)
    elif statcheck == "int":
        print("modifier is:", intmod)
        print("stat check is:", checkdie + intmod)
    elif statcheck == "wis":
        print("modifier is:", wismod)
        print("stat check is:", checkdie + wismod)
    elif statcheck == "cha":
        print("modifier is:", chamod)
        print("stat check is:", checkdie + chamod)
    else:
        return "invalid input"
    #with "if" statements, always returns 'invalid input'
    #with "elif" statements, always returns 'none'
    #how to make it only print if input is false?
def rollsave():
    savecheck = input("Rolling save - str, dex, con, int, wis, or cha: ")
    savedie = roll(20)
    print("roll is:", savedie)
    if savecheck == "str":
        print("modifier is:", strmod)
        print("stat check is:", savedie + strmod)
    elif savecheck == "dex":
        print("modifier is:", dexmod, "+", profmod)
        print("stat check is:", savedie + dexmod + profmod)
    elif savecheck == "con":
        print("modifier is:", conmod)
        print("stat check is:", savedie + conmod)
    elif savecheck == "int":
        print("modifier is:", intmod, "+", profmod)
        print("stat check is:", savedie + intmod + profmod)
    elif savecheck == "wis":
        print("modifier is:", wismod)
        print("stat check is:", savedie + wismod)
    elif savecheck == "cha":
        print("modifier is:", chamod)
        print("stat check is:", savedie + chamod)
    else:
        return "invalid input"

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
    elif advcheck == "dex":
        print("modifier is:", dexmod)
        print("advantage check is:", advdie + dexmod)
    elif advcheck == "con":
        print("modifier is:", conmod)
        print("advantage check is:", advdie + conmod)
    elif advcheck == "int":
        print("modifier is:", intmod)
        print("advantage check is:", advdie + intmod)
    elif advcheck == "wis":
        print("modifier is:", wismod)
        print("advantage check is:", advdie + wismod)
    elif advcheck == "cha":
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
    elif discheck == "dex":
        print("modifier is:", dexmod)
        print("disadvantage check is:", disdie + dexmod)
    elif discheck == "con":
        print("modifier is:", conmod)
        print("disadvantage check is:", disdie + conmod)
    elif discheck == "int":
        print("modifier is:", intmod)
        print("disadvantage check is:", disdie + intmod)
    elif discheck == "wis":
        print("modifier is:", wismod)
        print("disadvantage check is:", disdie + wismod)
    elif discheck == "cha":
        print("modifier is:", chamod)
        print("disadvantage check is:", disdie + chamod)
    else:
        return "invalid input"
