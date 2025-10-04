def write_file(filePath, content):
    try:
        with open(filePath, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        raise Exception(f"Encountered error: {str(e)} while writing file: {filePath}")

