import random
import json
from pprint import pprint as pp

with open('brick.json', 'r') as character_file:
    character_string = character_file.read()

character = json.loads(character_string)
attr = character['attributes']

# todo
# add save roll block
# decide if want to add passive skills

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


def rolldice(quantity, die_sides, print_val=True):
    """ roll a quantity of dice, all with the same amount of sides
    ex. 4d20 as (4,20) """

    def rolldie(die_sides):
        r1, r2 = 1, die_sides
        die_thing = list(range(r1, r2 + 1))
        random.shuffle(die_thing)
        roll_die = die_thing[0]
        return roll_die

    dice = [rolldie(die_sides) for _ in range(0, quantity)]
    if print_val:
        print(f'rolls are: {dice}')
    return dice



def roll(stat=None, mod_type=None):
    # roll stat or skill check with possible advantage or disadvantage
    # mod_type should be 'advantage', 'disadvantage', or None
    if mod_type not in ('advantage', 'disadvantage', None):
        print('Error: invalid mod type. Choose "advantage", "disadvantage", or None')
        return
    mod_type_check_message = f'{stat} check with {mod_type}' if mod_type else f'{stat} check'
    if stat is None:
        stat = input(f'rolling {mod_type_check_message} - {", ".join(attributes)}')
    die1, die2 = rolldice(2, 20, print_val=False)
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
