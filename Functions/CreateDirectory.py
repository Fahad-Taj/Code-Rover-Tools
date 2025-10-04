import os
BASE_DIR = os.getenv("BASE_DIR")

def create_directory(dirPath):
    try:
        dirPath = os.path.join(BASE_DIR, dirPath)
        os.makedirs(dirPath)
    except Exception as e:
        raise Exception(str(e))