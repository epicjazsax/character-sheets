#!/usr/bin/env python3

import json
from pprint import pprint as pp
from collections import namedtuple

def attr_to_modifier(attr):
    return (attr // 2) - 5


def level_to_proficiency(level):
    return (level + 7) // 4


def is_valid_attr(attr):
    if attr in ('str', 'int', 'wis', 'dex', 'con', 'con', 'cha'):
        return True
    return False


Attributes = namedtuple("Attributes", "str int wis dex con cha")
Proficiency = namedtuple("Proficiency", "attr multiplier")

# PROFICIENCIES = {
#     'init': Proficiency("dex", 1.0),
#     'acrobatics': Proficiency('dex', 0.0),
#     'animal_handling': Proficiency('wis', 0.0),
#     'arcana': Proficiency('int', 0.0),
#     'athletics': Proficiency('str', 0.0),
#     'deception': Proficiency('cha', 0.0),
#     'history': Proficiency('int', 0.0),
#     'insight': Proficiency('wis', 0.0),
#     'intimidation': Proficiency('cha', 0.0),
#     'investigation': Proficiency('int', 0.0),
#     'medicine': Proficiency('wis', 0.0),
#     'nature': Proficiency('int', 0.0),
#     'perception': Proficiency('wis', 0.0),
#     'performance': Proficiency('cha', 0.0),
#     'persuasion': Proficiency('cha', 0.0),
#     'religion': Proficiency('int', 0.0),
#     'sleight': Proficiency('dex', 0.0),
#     'stealth': Proficiency('dex', 0.0),
#     'survival': Proficiency('wis', 0.0),
# }


key_attr = {
    'init': 'dex',
    'acrobatics': 'dex',
    'animal_handling': 'wis',
    'arcana': 'int',
    'athletics': 'str',
    'deception': 'cha',
    'history': 'int',
    'insight': 'wis',
    'intimidation': 'cha',
    'investigation': 'int',
    'medicine': 'wis',
    'nature': 'int',
    'perception': 'wis',
    'performance': 'cha',
    'persuasion': 'cha',
    'religion': 'int',
    'sleight': 'dex',
    'stealth': 'dex',
    'survival': 'wis',
}


class Proficiency:
    def __init__(self, name, multiplier=1):
        self.name = name
        self.attr = key_attr[name]
        self.multiplier = multiplier

    # def __str__(self):
    #     return f'{self.name} ({self.modifier})'

    def __repr__(self):
        return f'{self.name} ({self.multiplier})'


class Character:
    def __init__(self):
        self.name = None
        self.level = None
        self.dnd_id = None
        self.attrs = None
        self.proficiencies = dict()

    def load_dict(self, data):
        self.name = data['name']
        self.level = data['level']
        self.dnd_id = data['dnd_id']

        a = data['attributes']
        self.attrs = Attributes(a['str'], a['int'], a['wis'], a['dex'],
                                a['con'], a['cha'])

        # TODO
        # CHANGE self.proficiencies to use the named_tuple
        # (attr, multiplier) instead of (name, multiplier)
        # THEN ADD TESTS!!!!!!!

        for p in data['proficiencies']:
            if '_dbl' in p:
                p = p.strip('_dbl')
                multiplier = 2
            elif '_half' in p:
                p = p.strip('_half')
                multiplier = 0.5
            else:
                multiplier = 1
            self.proficiencies[p] = Proficiency(p, multiplier)

    def load_file(self, filename):
        with open(filename, 'r') as f:
            self.load_dict(json.loads(f.read()))

    def get_proficiency_modifier(self, prof_name):
        prof = self.proficiencies[prof_name]
        # attr = self.attrs[self.attrs._fields.index(prof.attr)]
        # attr = self.attrs._asdict()[prof.attr]
        attr = getattr(self.attrs, prof.attr)
        attr_mod = attr_to_modifier(attr)
        prof_mod = level_to_proficiency(self.level) * prof.multiplier
        return attr_mod + int(prof_mod)


class Tester:
    def __init(self):
        self.vals = dict()

    def __getitem__(self, item):
        return self.vals[item]

    def __setitem__(self, item, value):
        self.vals[item] = value


if __name__ == '__main__':
    brick = Character()
    brick.load_file('brick.json')

    # attributes = {
    #     "str": 18,
    #     "dex": 7,
    #     "con": 17,
    #     "int": 14,
    #     "wis": 12,
    #     "cha": 10,
    #     "dark_vision": 0,
    #     "walking_speed": 30
    # },
    #
    # t = Tester()
    # t.attrs = attributes
    # t.str = "18"
    # t.int = "14"
    # t.profs = Tester()
    # t.profs.athletics = {'enabled': True, 'multiplier': 1}
    #
    # print(t.attrs)
    # print(t.str)
    # print(t.int)
    # print(t.profs)
    # print(t.profs.athletics)

    print(brick.name)
    print(brick.attrs)

    # brick.attrs.str = brick.attrs['str']
    # brick.attrs.int = brick.attrs['int']
    # brick.attrs.wis = brick.attrs['wis']
    # brick.attrs.dex = brick.attrs['dex']
    # brick.attrs.con = brick.attrs['con']
    # brick.attrs.cha = brick.attrs['cha']

    print(brick.attrs.str)
    print(brick.attrs.int)
    print(brick.attrs.wis)
    print(brick.attrs.dex)
    print(brick.attrs.con)
    print(brick.attrs.cha)
    # print(brick.attrs.vals)
    print(brick.proficiencies)
    print(brick.get_proficiency_modifier('religion'))

