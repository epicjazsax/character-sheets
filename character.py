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
        prof = self.proficiencies[prof_name]
        ability = getattr(self.abilities, prof.ability)
        prof_mod = int(level_to_proficiency(self.level) * prof.multiplier)
        return ability_modifier(ability) + prof_mod

    def get_ability_modifier(self, ability_name):
        return ability_modifier(getattr(self.abilities, ability_name))

    # TODO: Should we add methods "get_ability_check_target" and
    #       "get_proficiency_check_target" to return the actual roll required?


if __name__ == '__main__':
    brick = Character()
    brick.load_file('brick.json')

    print(brick.name)
    print(brick.abilities)
    print(brick.proficiencies)
    print(brick.get_proficiency_modifier('religion'))

    for ability in ABILITIES:
        print(f"{ability}: {getattr(brick.abilities, ability):2}  --  "
              f"mod: {brick.get_ability_modifier(ability):2}")

    for prof_name, prof in brick.proficiencies.items():
        if prof.multiplier:
            lhs = f"{prof_name}: {prof.ability}, x{prof.multiplier}"
            print(f"{lhs:25}  --  "
                  f"mod: {brick.get_proficiency_modifier(prof_name)}")

    # print(brick.get_proficiency_modifier('religion'))

