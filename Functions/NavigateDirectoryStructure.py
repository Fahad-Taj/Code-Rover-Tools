import os

EXCLUDED_FOLDERS = ["node_modules", ".vscode", "venv", "__pycache__", ".git"]

def navigate_directory_structure(path):
    files = {}
    try:
        for item in os.listdir(path):
            if item not in EXCLUDED_FOLDERS:
                fullPath = os.path.join(path, item)
                if os.path.isdir(fullPath):
                    files[item] = navigate_directory_structure(fullPath)
                else:
                    files[item] = None
    except Exception as e:
        return None

    return files