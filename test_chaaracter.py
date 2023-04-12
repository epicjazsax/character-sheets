"""Unit tests for character.py"""
import character


def test_score_to_modifier():
    assert character.ability_modifier(18) == 4
    assert character.ability_modifier(11) == 0
    assert character.ability_modifier(10) == 0


def test_level_to_proficiency():
    assert character.level_to_proficiency(5) == 3
