from Abstraction.Tool import Tool
from Abstraction.ToolParameter import ToolParameter
from Functions.ReadTextFile import read_text_file

def main():
    textFileReader = Tool("Text File Reader", "Tool used to read text files", [ToolParameter("filePath", "str", "Relative path of the file")], read_text_file)
    print(textFileReader.execute(filePath=r"C:\Users\fahad\OneDrive\Documents\changes in report.txt").content)
    print(textFileReader.toJson())
if __name__ == "__main__":
    main()