import json
from Abstraction.Tool import Tool
from Abstraction.ToolParameter import ToolParameter
from Abstraction.ToolResult import ToolResult
from Functions.WriteFile import write_file

fileWriter = Tool(
    name="File Writer",
    description="Creates a file if it does not exist and writes content to it. If a file already exists, this tool will replace existing contents of the file with new contents.",
    parameters=[
        ToolParameter(
            paramName="filePath",
            paramDescription="Complete path to a file in raw format.",
            paramType="str",
        ),
        ToolParameter(
            paramName="content",
            paramDescription="Content in string format that has to be written to a file",
            paramType="str"
        ),
    ],
    func=write_file
)

def main():
    try:
        result = fileWriter.execute(filePath=r"C:\Users\fahad\OneDrive\Documents\python-projects\Code-Rover-Tools\shitcode\helloWorld2.py", content="print('Hello World for the second time')")
        print(result.to_json())
    except Exception as e:
        print(str(e))

    print(fileWriter.toJson())
if __name__ == "__main__":
    main()