# def update_parent_ids(data, parent_id=None):
#     for item in data:
#         if parent_id is not None:
#             item["id"] = f"{parent_id}{item['id']}"
#         if "subfolder" in item and item["subfolder"]:
#             update_child_ids(item["subfolder"], item["id"])

# def update_child_ids(data, parent_id=None):
#     for item in data:
#         if parent_id is not None:
#             item["id"] = f"{parent_id}{item['id']}"

data_json = {
  "folder": [
    {
      "id": "",
      "name": "IA",
      "subfolder": [
        { "id": "", "name": "Identity" },
        { "id": "", "name": "Access" },
        { "id": "", "name": "Credential" }
      ]
    },
    {
      "id": "",
      "name": "Data Protection",
      "subfolder": [
        { "id": "", "name": "Data" },
        { "id": "", "name": "Data" },
        { "id": "", "name": "Data" },
        { "id": "", "name": "Data" }
      ]
    },
    {
      "id": "",
      "name": "Electr",
      "subfolder": []
    },
    {
      "id": "",
      "name": "Misc",
      "subfolder": []
    }
  ]
}


import json

# # Parse the JSON data into a Python dictionary
# data_dict = json.loads(data_json)

# # Start updating the "id" values for parent folders
# update_parent_ids(data_dict["folder"])

# # Convert the updated dictionary back to JSON
# updated_data_json = json.dumps(data_dict, indent=2)

# print(updated_data_json)

id_mapping = {
    "IA": "550",
    "Data": "551",
    "Elect": "552",
    "Misc": "553"
}

# Update the "id" values for the top-level folders
for folder in data_json["folder"]:
    folder_name = folder["name"]
    if folder_name in id_mapping:
        folder["id"] = id_mapping[folder_name]

print(data_json)