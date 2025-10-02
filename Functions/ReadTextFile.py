def read_text_file(filePath):
    try:
        with open(filePath, 'r') as f:
            content = f.read()
        return content
    except Exception as e:
        raise Exception(f"Encountered error: {str(e)} while reading text file: {filePath}")