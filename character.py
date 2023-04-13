#!/usr/bin/env python3

"""DnD Character File"""

import json
from collections import namedtuple  # for immutable
from dataclasses import dataclass  # for mutable


# Note: See https://roll20.net/compendium/dnd5e/Ability%20Scores#content for
# terminology used for data structure

ABILITIES = ('str', 'int', 'wis', 'dex', 'con', 'cha')


def ability_modifier(ability):
    return (ability // 2) - 5


def level_to_proficiency(level):
    return (level + 7) // 4


Abilities = namedtuple("Abilities", " ".join(ABILITIES))


# @dataclass
# class Abilities:
#     """Class for keeping track of character abilities"""
#     str: int
#     int: int
#     wis: int
#     dex: int
#     con: int
#     cha: int


@dataclass
class Proficiency:
    """Class for keeping track of related ability and degree of expertise"""
    ability: str
    multiplier: int = 0


class Character:
    def __init__(self):
        self.name = None
        self.level = None
        self.dnd_id = None
        self.abilities = None
        self.proficiencies = None

    def load_dict(self, data):
        self.name = data['name']
        self.level = data['level']
        self.dnd_id = data['dnd_id']
        self.abilities = Abilities(*(data['abilities'][k] for k in ABILITIES))
        self.proficiencies = {
            'init': Proficiency('dex'),
            'acrobatics': Proficiency('dex'),
            'animal_handling': Proficiency('wis'),
            'arcana': Proficiency('int'),
            'athletics': Proficiency('str'),
            'deception': Proficiency('cha'),
            'history': Proficiency('int'),
            'insight': Proficiency('wis'),
            'intimidation': Proficiency('cha'),
            'investigation': Proficiency('int'),
            'medicine': Proficiency('wis'),
            'nature': Proficiency('int'),
            'perception': Proficiency('wis'),
            'performance': Proficiency('cha'),
            'persuasion': Proficiency('cha'),
            'religion': Proficiency('int'),
            'sleight': Proficiency('dex'),
            'stealth': Proficiency('dex'),
            'survival': Proficiency('wis'),
        }

        for p in data['proficiencies']:
            if '_dbl' in p:
                p = p.strip('_dbl')
                multiplier = 2
            elif '_half' in p:
                p = p.strip('_half')
                multiplier = 0.5
            else:
                multiplier = 1

            self.proficiencies[p].multiplier = multiplier

    def load_file(self, filename):
        with open(filename, 'r') as f:
            self.load_dict(json.loads(f.read()))

    def get_proficiency_modifier(self, prof_name):
        if prof_name in ABILITIES:
            ability = getattr(self.abilities, prof_name)
            prof_mod = 0
        else:
            prof = self.proficiencies[prof_name]
            ability = getattr(self.abilities, prof.ability)
            prof_mod = int(level_to_proficiency(self.level) * prof.multiplier)
        return ability_modifier(ability) + prof_mod



if __name__ == '__main__':
    brick = Character()
    brick.load_file('brick.json')

    print(brick.name)
    print(brick.abilities)
    print(brick.proficiencies)
    print(brick.get_proficiency_modifier('religion'))

    for ability in ABILITIES:
        print(f"{ability}: {getattr(brick.abilities, ability):2}  --  "
              f"mod: {brick.get_proficiency_modifier(ability):2}")

    for prof_name, prof in brick.proficiencies.items():
        if prof.multiplier:
            lhs = f"{prof_name}: {prof.ability}, x{prof.multiplier}"
            print(f"{lhs:25}  --  "
                  f"mod: {brick.get_proficiency_modifier(prof_name)}")

    # print(brick.get_proficiency_modifier('religion'))

