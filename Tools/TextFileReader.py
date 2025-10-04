from Abstraction.Tool import Tool
from Abstraction.ToolParameter import ToolParameter
from Functions.ReadTextFile import read_text_file

textFileReader = Tool(
    name="Text File Reader",
    description="Tool used to read text files. Can also be used to read code files such as Python and JavaScript files.",
    parameters=[
        ToolParameter(
            paramName="filePath",
            paramType="str",
            paramDescription="Complete path to a file in raw format."
        )
    ],
    func=read_text_file
)


def main():
    print(textFileReader.execute(filePath=r"C:\Users\fahad\OneDrive\Documents\changes in report.txt").content)
    print(textFileReader.to_json())

if __name__ == "__main__":
    main()