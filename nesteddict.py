# Creating a nested dictionary for folder structure
folder_structure = {
    'parent_folder1': {
        'id': 1,
        'subfolders': {
            'subfolder1': {
                'id': 101
            },
            'subfolder2': {
                'id': 102
            },
            'subfolder3': {
                'id': 103
            }
        }
    },
    'parent_folder2': {
        'id': 2,
        'subfolders': {
            'subfolder1': {
                'id': 201
            },
            'subfolder2': {
                'id': 202
            }
        }
    },
    'parent_folder3': {
        'id': 3
    },
    'parent_folder4': {
        'id': 4
    }
}

# Accessing nested dictionary values
print(folder_structure['parent_folder1']['id'])  # Output: 1
print(folder_structure['parent_folder2']['subfolders']['subfolder2']['id'])  # Output: 202

# Modifying nested dictionary values
folder_structure['parent_folder1']['subfolders']['subfolder1']['id'] = 303

# Adding a new subfolder to an existing parent folder
folder_structure['parent_folder2']['subfolders']['subfolder2'] = {'id': 203}

# Printing the updated folder structure
print(folder_structure)
