#!/usr/bin/env python3

"""DnD Character File"""

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


class Character:
    def __init__(self):
        self.name = None
        self.level = None
        self.dnd_id = None
        self.attrs = None
        self.proficiencies = {
            'init': Proficiency("dex", 0),
            'acrobatics': Proficiency('dex', 0),
            'animal_handling': Proficiency('wis', 0),
            'arcana': Proficiency('int', 0),
            'athletics': Proficiency('str', 0),
            'deception': Proficiency('cha', 0),
            'history': Proficiency('int', 0),
            'insight': Proficiency('wis', 0),
            'intimidation': Proficiency('cha', 0),
            'investigation': Proficiency('int', 0),
            'medicine': Proficiency('wis', 0),
            'nature': Proficiency('int', 0),
            'perception': Proficiency('wis', 0),
            'performance': Proficiency('cha', 0),
            'persuasion': Proficiency('cha', 0),
            'religion': Proficiency('int', 0),
            'sleight': Proficiency('dex', 0),
            'stealth': Proficiency('dex', 0),
            'survival': Proficiency('wis', 0),
        }

    def load_dict(self, data):
        self.name = data['name']
        self.level = data['level']
        self.dnd_id = data['dnd_id']

        a = data['attributes']
        self.attrs = Attributes(a['str'], a['int'], a['wis'], a['dex'],
                                a['con'], a['cha'])

        for p in data['proficiencies']:
            if '_dbl' in p:
                p = p.strip('_dbl')
                multiplier = 2
            elif '_half' in p:
                p = p.strip('_half')
                multiplier = 0.5
            else:
                multiplier = 1
            self.proficiencies[p] = Proficiency(
                self.proficiencies[p].attr,
                multiplier
            )

    def load_file(self, filename):
        with open(filename, 'r') as f:
            self.load_dict(json.loads(f.read()))

    def get_proficiency_modifier(self, prof_name):
        prof = self.proficiencies[prof_name]
        attr = getattr(self.attrs, prof.attr)
        attr_mod = attr_to_modifier(attr)
        prof_mod = level_to_proficiency(self.level) * prof.multiplier
        return attr_mod + int(prof_mod)


if __name__ == '__main__':
    brick = Character()
    brick.load_file('brick.json')

    print(brick.name)
    print(brick.attrs)
    print(brick.proficiencies)
    print(brick.get_proficiency_modifier('religion'))

