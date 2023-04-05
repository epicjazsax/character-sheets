import random
import json

with open("brick.json", "r") as character_file:
    character_string = character_file.read()

character = json.loads(character_string)
attr = character["attributes"]
mods = {
    "str": (attr["str"] // 2) - 5,
    "dex": (attr["dex"] // 2) - 5,
    "con": (attr["con"] // 2) - 5,
    "int": (attr["int"] // 2) - 5,
    "wis": (attr["wis"] // 2) - 5,
    "cha": (attr["cha"] // 2) - 5,
}

mods["prof"] = (character["level"] + 7) // 4
mods["dblprof"] = mods["prof"] * 2
mods["halfprof"] = mods["prof"] // 2
mods["init"] = mods["dex"]
mods["acrobatics"] = mods["dex"]
mods["animal_handling"] = mods["wis"]
mods["arcana"] = mods["int"]
mods["athletics"] = mods["str"]
mods["deception"] = mods["cha"]
mods["history"] = mods["int"]
mods["insight"] = mods["wis"]
mods["intimidation"] = mods["cha"]
mods["investigation"] = mods["int"]
mods["medicine"] = mods["wis"]
mods["nature"] = mods["int"]
mods["perception"] = mods["wis"]
mods["performance"] = mods["cha"]
mods["persuasion"] = mods["cha"]
mods["religion"] = mods["int"]
mods["sleight"] = mods["dex"]
mods["stealth"] = mods["dex"]
mods["survival"] = mods["wis"]

for item in character["proficiencies"]:
    if "_dbl" in item:
        item = item.strip("_dbl")
        mods[item] = mods[item] + mods["dblprof"]
    elif "_half" in item:
        item = item.strip("_half")
        mods[item] = mods[item] + mods["halfprof"]
    else:
        mods[item] = mods[item] + mods["prof"]


print(f"Character attributes are {attr}")
print(f"Attribute and skill mods are {mods}")