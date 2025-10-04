import os

def create_directory(dirPath):
    try:
        os.makedirs(dirPath)
    except Exception as e:
        raise Exception(str(e))