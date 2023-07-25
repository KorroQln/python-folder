id_mapping = {
    "PARENT1": None,
        "child1": None,
        "child2": None,
        "child3": None,
    "PARENT2": None,
        "child3": None,
        "child4": None,
        "child5": None,
        "child6": None,
    "PARENT3": None,
    "PARENT4": None
}

idResp = 123
nameMap = "PARENT1"

for item in id_mapping:
    if item == nameMap:
        id_mapping[item] = idResp

print(id_mapping)