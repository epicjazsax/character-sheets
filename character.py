#!/usr/bin/env python3

import json
from pprint import pprint as pp


def attr_to_modifier(attr):
    return (attr // 2) - 5


def level_to_proficiency(level):
    return (level + 7) // 4


def is_valid_attr(attr):
    if attr in ('str', 'int', 'wis', 'dex', 'con', 'con', 'cha'):
        return True
    return False


class Attributes:
    def __init__(self, vals=None):
        if vals is None:
            self.vals = dict()
            self.str = None
            self.int = None
            self.wis = None
            self.dex = None
            self.con = None
            self.cha = None
        else:
            self.vals = vals
            self.str = vals['str']
            self.int = vals['int']
            self.wis = vals['wis']
            self.dex = vals['dex']
            self.con = vals['con']
            self.cha = vals['cha']

    def __repr__(self):
        return f"{self.str}"


class OldAttributes:
    def __init__(self, vals=None):
        if vals is None:
            self.vals = dict()
        else:
            # print(vals)
            # assert len(vals) == 6
            self.vals = vals

    @property
    def str(self):
        return self.vals['str']

    @property
    def int(self):
        return self.vals['int']

    @property
    def wis(self):
        return self.vals['wis']

    @property
    def dex(self):
        return self.vals['dex']

    @property
    def con(self):
        return self.vals['con']

    @property
    def cha(self):
        return self.vals['cha']

    @str.setter
    def str(self, val):
        self.vals['str'] = val

    @int.setter
    def int(self, val):
        self.vals['int'] = val

    @wis.setter
    def wis(self, val):
        self.vals['wis'] = val

    @dex.setter
    def dex(self, val):
        self.vals['dex'] = val

    @con.setter
    def con(self, val):
        self.vals['con'] = val

    @cha.setter
    def cha(self, val):
        self.vals['cha'] = val


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
        self.attrs = Attributes()
        self.proficiencies = dict()

    def load_dict(self, data):
        self.name = data['name']
        self.level = data['level']
        self.dnd_id = data['dnd_id']

        self.attrs = Attributes(data['attributes'])

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

    def prof_mod(self, prof_name):
        prof = self.proficiencies[prof_name]
        attr_mod = attr_to_modifier(self.attrs.vals[prof.attr])
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
    print(brick.attrs.vals)
    print(brick.proficiencies)
    print(brick.prof_mod('religion'))

