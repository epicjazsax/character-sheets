import random
import json
from pprint import pprint as pp

with open('brick.json', 'r') as character_file:
    character_string = character_file.read()

character = json.loads(character_string)
attr = character['attributes']


mods = {
    'str': (attr['str'] // 2) - 5,
    'dex': (attr['dex'] // 2) - 5,
    'con': (attr['con'] // 2) - 5,
    'int': (attr['int'] // 2) - 5,
    'wis': (attr['wis'] // 2) - 5,
    'cha': (attr['cha'] // 2) - 5,
    'prof': (character['level'] + 7) // 4
}

mods['init'] = mods['dex']
mods['acrobatics'] = mods['dex']
mods['animal_handling'] = mods['wis']
mods['arcana'] = mods['int']
mods['athletics'] = mods['str']
mods['deception'] = mods['cha']
mods['history'] = mods['int']
mods['insight'] = mods['wis']
mods['intimidation'] = mods['cha']
mods['investigation'] = mods['int']
mods['medicine'] = mods['wis']
mods['nature'] = mods['int']
mods['perception'] = mods['wis']
mods['performance'] = mods['cha']
mods['persuasion'] = mods['cha']
mods['religion'] = mods['int']
mods['sleight'] = mods['dex']
mods['stealth'] = mods['dex']
mods['survival'] = mods['wis']

for skill in character['proficiencies']:
    if '_dbl' in skill:
        skill = skill.strip('_dbl')
        mods[skill] = mods[skill] + (mods['prof'] * 2)
    elif '_half' in skill:
        skill = skill.strip('_half')
        mods[skill] = mods[skill] + (mods['prof'] // 2)
    else:
        mods[skill] = mods[skill] + mods['prof']

attributes = mods.keys()
check_types = {
    'advantage': max,
    'disadvantage': min,
    None: lambda a, b: a  # when in doubt, return a
}


def roll(die, print_val=True):
    r1, r2 = 1, die
    die_thing = list(range(r1, r2 + 1))
    random.shuffle(die_thing)
    roll_die = die_thing[0]
    if print_val:
        print(f'roll is: {roll_die}')
    return roll_die



def rollinit():
    # roll initiative
    initdie = roll(20)
    print(f'modifier is: {mods["init"]}')
    print(f'initiative is: {initdie + mods["init"]}')


def rolladv(stat=None):
    # roll with advantage
    rollcheck(stat=stat, mod_type='advantage')


def rolldis(stat=None):
    # roll with disadvantage
    rollcheck(stat=stat, mod_type='disadvantage')


def rollcheck(stat=None, mod_type=None):
    # roll stat or skill check with possible advantage or disadvantage
    # mod_type should be 'advantage', 'disadvantage', or None
    if mod_type not in ('advantage', 'disadvantage', None):
        print('Error: invalid mod type. Choose "advantage", "disadvantage", or None')
        return
    mod_type_check_message = f'{mod_type} check' if mod_type else 'check'
    if stat is None:
        stat = input(f'rolling {mod_type_check_message} - {", ".join(attributes)}')
    die1, die2 = roll(20, print_val=False), roll(20, print_val=False)
    if mod_type is None:
        print(f'roll is {die1}')
    else:
        print(f'rolls are {die1}, {die2}')

    f = check_types[mod_type]
    die = f(die1, die2)

    mod = mods[stat]
    print(f'modifier is: {mod}')
    print(f'{mod_type_check_message} is: {die + mod}')


# pp(f'Character attributes are {attr}')
# pp(f'Attribute and skill mods are {mods}')
