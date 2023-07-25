id_mapping = {
    "IAM": None,
        "Identity": None,
        "Access": None,
        "Credential Management": None,
    "Data Protection": None,
        "Data Storage": None,
        "Data Communication": None,
        "Data Retention": None,
        "Data Processing": None,
    "Electronic Mail": None,
    "Miscellany": None
}

idResp = 123
nameMap = "Miscellany"

for item in id_mapping:
    if item == nameMap:
        id_mapping[item] = idResp

print(id_mapping)